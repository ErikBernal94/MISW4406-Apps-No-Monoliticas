from __future__ import annotations
from dataclasses import dataclass, field
from contrato.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class MovimientoRegistrado(EventoDominio):
    id_movimiento: uuid.UUID = None