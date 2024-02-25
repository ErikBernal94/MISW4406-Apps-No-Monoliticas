from __future__ import annotations
from dataclasses import dataclass, field
from contrato.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class ContratoRegistrado(EventoDominio):
    id_contrato: uuid.UUID = None
    estado_contrato: str = None
    tipo_contrato: str = None