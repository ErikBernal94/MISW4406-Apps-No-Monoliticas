from pulsar.schema import *
from compania.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class CompaniaCreadaPayload(Record):
    id_compania = String()
    correo_electronico = String()
    direccion = String()

class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()
