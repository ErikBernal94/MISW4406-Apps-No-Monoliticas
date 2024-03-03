from __future__ import annotations
from dataclasses import dataclass, field

from contrato.modulos.movimiento_inmobiliario.dominio.eventos import MovimientoRegistrado
from contrato.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class MovimientoInmobiliario(AgregacionRaiz):
    id_movimiento: uuid.UUID = field(hash=True, default=None)

    def registrar_movimiento(self, movimiento: MovimientoInmobiliario):
        self.id_movimiento = movimiento.id_movimiento
        self.agregar_evento(MovimientoRegistrado(id_movimiento=self.id_movimiento))