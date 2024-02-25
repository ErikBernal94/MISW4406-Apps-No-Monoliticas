from dataclasses import dataclass

from compania.seedwork.dominio.repositorios import Mapeador, Repositorio
from compania.seedwork.dominio.fabricas import Fabrica
from compania.seedwork.dominio.entidades import Entidad
from compania.dominio.entidades import Compania

@dataclass
class _FabricaCompania(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            compania: Compania = mapeador.dto_a_entidad(obj)
            return compania