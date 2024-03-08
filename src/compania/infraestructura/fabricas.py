from dataclasses import dataclass, field
from compania.seedwork.dominio.fabricas import Fabrica
from compania.seedwork.dominio.repositorios import Repositorio
from compania.dominio.repositorios import RepositorioCompanias
from .repositorios import RepositorioCompaniasSQLite

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCompanias:
            return RepositorioCompaniasSQLite()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
