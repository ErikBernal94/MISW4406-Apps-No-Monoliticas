from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

class TipoPropiedad(Enum):
    COMERCIAL = "comercial"
    RESIDENCIAL = "residencial"
