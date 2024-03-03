from pulsar.schema import *
from contrato.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ContratoCreadaPayload(Record):
    id_contrato = String()
    estado_contrato = String()
    tipo_contrato = String()

class EventoContratoCreada(EventoIntegracion):
    data = ContratoCreadaPayload()