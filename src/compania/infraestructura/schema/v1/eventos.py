from pulsar.schema import *
from compania.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class CompaniaCreadaPayload(Record):
    id_compania = String()
    correo_electronico = Object()
    direccion = Object()

class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()