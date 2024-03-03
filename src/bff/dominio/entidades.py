from __future__ import annotations
from dataclasses import dataclass, field

from compania.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Compania(Entidad):
    id_compania: uuid.UUID = field(hash=True, default=None)
    correo_electronico: str = None
    direccion: str = None

@dataclass
class Contrato(Entidad):
    id_compania: uuid.UUID = field(hash=True, default=None)
    tipo_contrato: str = None
    estado_contrato: str = None

@dataclass
class Propiedad(Entidad):
    id_propiedad: uuid.UUID = field(hash=True, default=None)
    tipo_propiedad: str = None
    descripcion_propiedad: str = None



