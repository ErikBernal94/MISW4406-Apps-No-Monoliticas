from dataclasses import dataclass

from propiedad.seedwork.dominio.repositorios import Mapeador, Repositorio
from propiedad.seedwork.dominio.fabricas import Fabrica
from propiedad.seedwork.dominio.entidades import Entidad
from propiedad.dominio.entidades import Propiedad

@dataclass
class _FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad : Propiedad = mapeador.dto_a_entidad(obj)
            return propiedad