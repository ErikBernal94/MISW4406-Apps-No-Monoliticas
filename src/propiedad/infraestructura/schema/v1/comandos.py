from pulsar.schema import *
from dataclasses import dataclass, field
from propiedad.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearPropiedadPayload(ComandoIntegracion):
    ...

class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()