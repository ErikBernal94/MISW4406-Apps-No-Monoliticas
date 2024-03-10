from dataclasses import dataclass, field
from propiedad.seedwork.dominio.fabricas import Fabrica
from propiedad.seedwork.dominio.repositorios import Repositorio
from propiedad.dominio.repositorios import RepositorioPropiedades
from .repositorios import RepositorioPropiedadesSQLite
from propiedad.seedwork.dominio.excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades:
            return RepositorioPropiedadesSQLite()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
