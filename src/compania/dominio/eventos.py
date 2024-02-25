from __future__ import annotations
from dataclasses import dataclass, field
from compania.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class CompaniaRegistrada(EventoDominio):
    id_compania: uuid.UUID = None
    correo_electronico: object = None
    direccion: object = None

