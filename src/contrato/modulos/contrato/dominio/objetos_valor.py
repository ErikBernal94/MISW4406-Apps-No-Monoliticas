from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

class EstadoContrato(Enum):
    ACTIVO = "activo"
    CERRADO = "cerrado"

class TipoContrato(Enum):
    ARRENDAMIENTO = "arrendamiento"
    VENTA = "venta"

