from __future__ import annotations
from dataclasses import dataclass, field

from propiedad.dominio.objetos_valor import TipoPropiedad
from propiedad.dominio.eventos import PropiedadRegistrada
from propiedad.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Propiedad(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=None)
    tipo_propiedad: TipoPropiedad = None
    descripcion_propiedad: EstadoPropiedad = None

    def registrar_propiedad(self, propiedad: Propiedad):
        self.tipo_propiedad = propiedad.tipo_propiedad
        self.descripcion_propiedad = propiedad.descripcion_propiedad

        self.agregar_evento(PropiedadRegistrada(id_propiedad=self.id_propiedad, descripcion_propiedad=self.descripcion_propiedad, tipo_propiedad=self.tipo_propiedad))