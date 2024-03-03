from pulsar.schema import *
from propiedad.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    estado_propiedad = String()
    tipo_propiedad = String()

class EventoPropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()