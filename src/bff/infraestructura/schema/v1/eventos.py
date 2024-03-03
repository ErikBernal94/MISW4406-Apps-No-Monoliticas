from pulsar.schema import *
from bff.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class CompaniaCreadaPayload(Record):
    id_compania = String()
    correo_electronico = String()
    direccion = String()

class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()

class ContratoCreadaPayload(Record):
    id_contrato = String()
    estado_contrato = String()
    tipo_contrato = String()

class EventoContratoCreada(EventoIntegracion):
    data = ContratoCreadaPayload()