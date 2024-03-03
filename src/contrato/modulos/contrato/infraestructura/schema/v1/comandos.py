from pulsar.schema import *
from dataclasses import dataclass, field
from contrato.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearContratoPayload(ComandoIntegracion):
    ...

class ComandoCrearContrato(ComandoIntegracion):
    data = ComandoCrearContratoPayload()