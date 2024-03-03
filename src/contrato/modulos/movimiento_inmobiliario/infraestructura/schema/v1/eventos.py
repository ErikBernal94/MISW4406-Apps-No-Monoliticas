from pulsar.schema import *
from contrato.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class MovimientoCreadoPayload(Record):
    id_movimiento = String()

class EventoMovimientoCreado(EventoIntegracion):
    data = MovimientoCreadoPayload()