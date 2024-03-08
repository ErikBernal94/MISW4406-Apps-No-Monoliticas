from dataclasses import dataclass

from contrato.seedwork.dominio.repositorios import Mapeador, Repositorio
from contrato.seedwork.dominio.fabricas import Fabrica
from contrato.seedwork.dominio.entidades import Entidad
from contrato.modulos.movimiento_inmobiliario.dominio.entidades import MovimientoInmobiliario

@dataclass
class _FabricaMovimientoInmobiliario(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            movimiento : MovimientoInmobiliario = mapeador.dto_a_entidad(obj)
            return movimiento

@dataclass
class FabricaMovimientoInmobiliario(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == MovimientoInmobiliario.__class__:
            fabrica_movimientoInmobiliario = _FabricaMovimientoInmobiliario()
            return fabrica_movimientoInmobiliario.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()
