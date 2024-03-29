import pulsar
from pulsar.schema import *

from contrato.modulos.contrato.infraestructura.schema.v1.eventos import EventoContratoCreada, ContratoCreadaPayload
from contrato.modulos.contrato.infraestructura.schema.v1.comandos import ComandoCrearContrato, ComandoCrearContratoPayload
from contrato.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoContratoCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ContratoCreadaPayload(
            id_contrato=str(evento.id_contrato), 
            correo_electronico=str(evento.correo_electronico), 
            direccion=str(evento.direccion) 
        )
        evento_integracion = EventoContratoCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoContratoCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearContratoPayload(
        )
        comando_integracion = ComandoCrearContrato(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearContrato))
