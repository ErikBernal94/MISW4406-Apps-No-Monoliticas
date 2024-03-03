from dataclasses import dataclass, field
from contrato.seedwork.dominio.fabricas import Fabrica
from contrato.seedwork.dominio.repositorios import Repositorio
from contrato.modulos.movimiento_inmobiliario.dominio.repositorios import RepositorioMovimiento
from .repositorios import RepositorioMovimientosSQLite

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioMovimiento.__class__:
            return RepositorioMovimientosSQLite()