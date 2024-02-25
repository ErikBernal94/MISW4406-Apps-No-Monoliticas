from dataclasses import dataclass, field
from compania.seedwork.dominio.fabricas import Fabrica
from compania.seedwork.dominio.repositorios import Repositorio
from compania.dominio.repositorios import RepositorioCompania
from .repositorios import RepositorioCompaniasSQLite

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCompania.__class__:
            return RepositorioCompaniasSQLite()