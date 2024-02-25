from __future__ import annotations
from dataclasses import dataclass, field

from compania.dominio.objetos_valor import NombreUsuario, NombreCompania, Cedula, TipoIndustria, Rut, TipoCompania, CorreoElectronico, Direccion
from compania.dominio.eventos import CompaniaRegistrada
from compania.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Persona(Entidad):
    ...

@dataclass
class PersonaNatural(Persona):
    nombre_usuario: NombreUsuario = field(default_factory=NombreUsuario)
    cedula: Cedula = field(default_factory=Cedula)

@dataclass
class PersonaJuridica(Persona):
    nombre_compania: NombreCompania = field(default_factory=NombreCompania)
    rut: Rut = field(default_factory=Rut)
    tipo_industria: TipoIndustria = field(default_factory=TipoIndustria)

@dataclass
class InformacionComercial(Entidad):
    ...

@dataclass
class InformacionLegal(Entidad):
    ...

# poner cosas de default 

@dataclass
class Compania(AgregacionRaiz):
    id_compania: uuid.UUID = field(hash=True, default=None)
    correo_electronico: CorreoElectronico = None
    direccion: Direccion = None

    def registrar_compania(self, compania: Compania):
        self.correo_electronico = compania.correo_electronico
        self.direccion = compania.direccion

        self.agregar_evento(CompaniaRegistrada(id_compania=self.id, correo_electronico= self.correo_electronico, direccion=self.direccion))




