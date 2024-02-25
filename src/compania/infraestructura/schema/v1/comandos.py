from pulsar.schema import *
from dataclasses import dataclass, field
from compania.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearCompaniaPayload(ComandoIntegracion):
    ...

class ComandoCrearCompania(ComandoIntegracion):
    data = ComandoCrearCompaniaPayload()