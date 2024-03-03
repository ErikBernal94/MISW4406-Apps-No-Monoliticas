import pulsar
from pulsar.schema import *

from bff.infraestructura.schema.v1.eventos import EventoCompaniaCreada, CompaniaCreadaPayload, ContratoCreadaPayload, EventoContratoCreada
from bff.infraestructura.schema.v1.comandos import ComandoCrearCompania, ComandoCrearCompaniaPayload, ComandoCrearContrato, ComandoCrearContratoPayload
from bff.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje_compania(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoCompaniaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento_compania(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = CompaniaCreadaPayload(
            id_compania=str(evento.id_compania), 
            correo_electronico=str(evento.correo_electronico), 
            direccion=str(evento.direccion) 
        )
        evento_integracion = EventoCompaniaCreada(data=payload)
        self._publicar_mensaje_compania(evento_integracion, topico, AvroSchema(EventoCompaniaCreada))

    def publicar_comando_compania(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearCompaniaPayload(
        )
        comando_integracion = ComandoCrearCompania(data=payload)
        self._publicar_mensaje_compania(comando_integracion, topico, AvroSchema(ComandoCrearCompania))

    def _publicar_mensaje_contrato(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoContratoCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento_contrato(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ContratoCreadaPayload(
            id_contrato=str(evento.id_contrato), 
            correo_electronico=str(evento.correo_electronico), 
            direccion=str(evento.direccion) 
        )
        evento_integracion = EventoContratoCreada(data=payload)
        self._publicar_mensaje_contrato(evento_integracion, topico, AvroSchema(EventoContratoCreada))

    def publicar_comando_contrato(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearContratoPayload(
        )
        comando_integracion = ComandoCrearContrato(data=payload)
        self._publicar_mensaje_contrato(comando_integracion, topico, AvroSchema(ComandoCrearContrato))

    def _publicar_mensaje_propiedad(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento_propiedad(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = PropiedadCreadaPayload(
            id_propiedad=str(evento.id_contrato),
            direccion=str(evento.direccion)
        )
        evento_integracion = EventoPropiedadCreada(data=payload)
        self._publicar_mensaje_propiedad(evento_integracion, topico, AvroSchema(EventoPropiedadCreada))

    def publicar_comando_propiedad(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearPropiedadPayload(
        )
        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje_propiedad(comando_integracion, topico, AvroSchema(ComandoCrearPropiedad))