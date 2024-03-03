from __future__ import annotations
from dataclasses import dataclass, field
from propiedad.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class PropiedadRegistrada(EventoDominio):
    id_propiedad: uuid.UUID = None
    descripcion_propiedad: str = None
    tipo_propiedad: str = None