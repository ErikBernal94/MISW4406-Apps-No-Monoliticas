from __future__ import annotations
from dataclasses import dataclass, field
from bff.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class CompaniaRegistrada(EventoDominio):
    id_compania: uuid.UUID = None
    correo_electronico: object = None
    direccion: object = None

@dataclass
class ContratoRegistrado(EventoDominio):
    id_contrato: uuid.UUID = None
    estado_contrato: str = None
    tipo_contrato: str = None