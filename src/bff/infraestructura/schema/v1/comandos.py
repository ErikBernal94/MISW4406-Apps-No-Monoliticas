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