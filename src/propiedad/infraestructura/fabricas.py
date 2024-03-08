from dataclasses import dataclass, field
from propiedad.seedwork.dominio.fabricas import Fabrica
from propiedad.seedwork.dominio.repositorios import Repositorio
from propiedad.dominio.repositorios import RepositorioPropiedades
from .repositorios import RepositorioPropiedadessSQLite

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadessSQLite()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
