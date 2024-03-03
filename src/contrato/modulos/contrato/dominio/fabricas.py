from dataclasses import dataclass

from contrato.seedwork.dominio.repositorios import Mapeador, Repositorio
from contrato.seedwork.dominio.fabricas import Fabrica
from contrato.seedwork.dominio.entidades import Entidad
from contrato.modulos.contrato.dominio.entidades import Contrato

@dataclass
class _FabricaContrato(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            contrato : Contrato = mapeador.dto_a_entidad(obj)
            return contrato