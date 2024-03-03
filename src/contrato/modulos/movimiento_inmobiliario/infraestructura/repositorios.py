from movimiento.config.db import db
from movimiento.modulos.movimiento_inmobiliario.dominio.repositorios import RepositorioMovimiento
from movimiento.modulos.movimiento_inmobiliario.dominio.entidades import MovimientoInmobiliario
from movimiento.modulos.movimiento_inmobiliario.dominio.fabricas import _FabricaMovimientoInmobiliario
from .dto import MovimientoInmobiliario as MovimientoDTO
from .mapeadores import MapeadorMovimiento
from uuid import UUID

class RepositorioMovimientosSQLite(RepositorioMovimiento):

    def __init__(self):
        self._fabrica_movimientos: _FabricaMovimientoInmobiliario = _FabricaMovimientoInmobiliario()

    @property
    def fabrica_movimientos(self):
        return self._fabrica_movimientos

    def obtener_por_id(self, id: UUID) -> MovimientoInmobiliario:
        movimiento_dto = db.session.query(MovimientoDTO).filter_by(id=str(id)).one()
        return self.fabrica_movimientos.crear_objeto(movimiento_dto, MapeadorMovimiento())

    def obtener_todos(self) -> list[MovimientoInmobiliario]:
        # TODO
        raise NotImplementedError

    def agregar(self, movimiento: MovimientoInmobiliario):
        movimiento_dto = self.fabrica_movimientos.crear_objeto(movimiento, MapeadorMovimiento())
        db.session.add(movimiento_dto)

    def actualizar(self, movimiento: MovimientoInmobiliario):
        # TODO
        raise NotImplementedError

    def eliminar(self, movimiento_id: UUID):
        # TODO
        raise NotImplementedError