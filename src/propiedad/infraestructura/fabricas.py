from dataclasses import dataclass, field
from propiedad.seedwork.dominio.fabricas import Fabrica
from propiedad.seedwork.dominio.repositorios import Repositorio
from propiedad.dominio.repositorios import RepositorioPropiedad
from .repositorios import RepositorioPropiedadsSQLite

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedad.__class__:
            return RepositorioPropiedadsSQLite()