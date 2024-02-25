from dataclasses import dataclass

from bff.seedwork.dominio.repositorios import Mapeador, Repositorio
from bff.seedwork.dominio.fabricas import Fabrica
from bff.seedwork.dominio.entidades import Entidad
from bff.dominio.entidades import Compania, Contrato

@dataclass
class _FabricaCompania(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            compania: Compania = mapeador.dto_a_entidad(obj)
            return compania
        
@dataclass
class _FabricaContrato(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            contrato: Contrato = mapeador.dto_a_entidad(obj)
            return contrato