from dataclasses import dataclass, field
from contrato.seedwork.dominio.fabricas import Fabrica
from contrato.seedwork.dominio.repositorios import Repositorio
from contrato.modulos.movimiento_inmobiliario.dominio.repositorios import RepositorioMovimientos
from .repositorios import RepositorioMovimientosSQLite
from contrato.seedwork.dominio.excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioMovimientos:
            return RepositorioMovimientosSQLite()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')