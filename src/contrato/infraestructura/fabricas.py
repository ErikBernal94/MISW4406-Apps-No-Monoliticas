from dataclasses import dataclass, field
from contrato.seedwork.dominio.fabricas import Fabrica
from contrato.seedwork.dominio.repositorios import Repositorio
from contrato.dominio.repositorios import RepositorioContrato
from .repositorios import RepositorioContratosSQLite

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioContrato.__class__:
            return RepositorioContratosSQLite()