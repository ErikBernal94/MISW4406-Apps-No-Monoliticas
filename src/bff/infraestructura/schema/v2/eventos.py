from pulsar.schema import *
from bff.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class CompaniaCreadaPayload(Record):
    id_compania = String()
    correo_electronico = String()
    direccion = String()

class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()

class CompaniaActualizadaPayload(Record):
    id_compania = String()
    correo_electronico = String()
    direccion = String()

class EventoCompaniaActualizada(EventoIntegracion):
    data = CompaniaActualizadaPayload()

class ContratoCreadaPayload(Record):
    id_contrato = String()
    estado_contrato = String()
    tipo_contrato = String()

class EventoContratoCreada(EventoIntegracion):
    data = ContratoCreadaPayload()

class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    descripcion_propiedad = String()
    tipo_propiedad = String()

class EventoPropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()