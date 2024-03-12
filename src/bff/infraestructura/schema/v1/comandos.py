from pulsar.schema import *
from dataclasses import dataclass, field
from bff.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearCompaniaPayload(ComandoIntegracion):
    ...

class ComandoCrearCompania(ComandoIntegracion):
    data = ComandoCrearCompaniaPayload()

class ComandoCrearContratoPayload(ComandoIntegracion):
    ...

class ComandoCrearContrato(ComandoIntegracion):
    data = ComandoCrearContratoPayload()

class RegistrarPropiedad(Record):
    id_propiedad = String()
    descripcion_propiedad = String()
    tipo_propiedad = String()
    fecha_creacion = Long()

class ComandoRegistrarPropiedad(ComandoIntegracion):
    id_propiedad = String()
    descripcion_propiedad = String()
    tipo_propiedad = String()
    type = String(default="RegistrarPropiedad")
    datacontenttype = String()
    service_name = String(default="propiedades.alpes")
    data = RegistrarPropiedad

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ComandoCrearPropiedadPayload(ComandoIntegracion):
    ...

class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()