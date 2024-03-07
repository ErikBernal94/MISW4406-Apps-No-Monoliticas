import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from datetime import datetime

from compania.infraestructura.proyecciones import ProyeccionReservasLista, ProyeccionReservasTotales
from compania.seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from compania.infraestructura.schema.v1.eventos import EventoCompaniaCreada
from compania.infraestructura.schema.v1.comandos import ComandoCrearCompania
from compania.seedwork.infraestructura import utils

def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='pda-sub-eventos', schema=AvroSchema(EventoCompaniaCreada))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            fecha_creacion = utils.current_milli_time()
            fecha_actualizacion = utils.current_milli_time()
            print(f'Evento recibido: {datos}')

            # TODO Identificar el tipo de CRUD del evento: Creacion, actualización o eliminación.
            ejecutar_proyeccion(ProyeccionReservasTotales(fecha_creacion, ProyeccionReservasTotales.ADD), app=app)
            ejecutar_proyeccion(ProyeccionReservasLista(datos.id_compania, datos.correo_electronico, datos.direccion, fecha_creacion, fecha_actualizacion), app=app)

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-compania', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoCrearCompania))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
