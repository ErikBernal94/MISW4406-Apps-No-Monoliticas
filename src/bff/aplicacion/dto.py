from dataclasses import dataclass, field
from bff.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class CompaniaDTO(DTO):
    direccion: str = field(default_factory=str)
    correo_electronico: str = field(default_factory=str)
    id_compania: str = field(default_factory=str)

@dataclass(frozen=True)
class ContratoDTO(DTO):
    tipo_contrato: str = field(default_factory=str)
    estado_contrato: str = field(default_factory=str)
    id_contrato: str = field(default_factory=str)