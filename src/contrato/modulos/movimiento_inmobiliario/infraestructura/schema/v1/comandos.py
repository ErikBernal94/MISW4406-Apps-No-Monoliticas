from pulsar.schema import *
from dataclasses import dataclass, field
from contrato.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearMovimientoPayload(ComandoIntegracion):
    ...

class ComandoCrearMovimiento(ComandoIntegracion):
    data = ComandoCrearMovimientoPayload()