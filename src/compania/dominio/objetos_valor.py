from __future__ import annotations

from dataclasses import dataclass, field
from compania.seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class NombreUsuario(ObjetoValor):
    primer_nombre: str
    segundo_nombre: str
    apellidos: str

@dataclass(frozen=True)
class DocumentoIdentidad(ObjetoValor):
    numero: str

@dataclass(frozen=True)
class Cedula(DocumentoIdentidad):
    ...

@dataclass(frozen=True)
class Rut(DocumentoIdentidad):
    ...

@dataclass(frozen=True)
class NombreCompania(ObjetoValor):
    nombre: str

@dataclass(frozen=True)
class CorreoElectronico(ObjetoValor):
    correo: str

@dataclass(frozen=True)
class Direccion(ObjetoValor):
    pais: str
    estado: str
    ciudad: str
    direccion: str

class TipoCompania(Enum):
    ARRENDATARIO = "arrendatario"
    INQUILINO = "inquilino"
    VENDEDOR = "vendedor"
    COMPRADOR = "comprador"

class TipoIndustria(Enum):
    PUBLICA = "publica"
    PRIVADA = "privada"
    HIBRIDA = "hibrida"
    



