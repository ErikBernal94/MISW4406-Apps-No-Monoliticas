from __future__ import annotations
from dataclasses import dataclass, field
from propiedad.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoPropiedad(EventoDominio):
    ...


@dataclass
class PropiedadCreada(EventoPropiedad):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    

@dataclass
class RegistroPropiedadFallida(EventoPropiedad):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    

@dataclass
class RegistroPropiedadRevertida(EventoPropiedad):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
