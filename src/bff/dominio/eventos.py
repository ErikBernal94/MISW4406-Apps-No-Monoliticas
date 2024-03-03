from __future__ import annotations
from dataclasses import dataclass, field
from bff.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class CompaniaRegistrada(EventoDominio):
    id_compania: uuid.UUID = None
    correo_electronico: String = None
    direccion: String = None

@dataclass
class ContratoRegistrado(EventoDominio):
    id_contrato: uuid.UUID = None
    estado_contrato: str = None
    tipo_contrato: str = None
@dataclass
class PropiedadRegistrada(EventoDominio):
    id_propiedad: uuid.UUID = None
    descripcion_propiedad: str = None
    tipo_propiedad: str = None