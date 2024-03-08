from propiedad.config.db import db
from propiedad.dominio.repositorios import RepositorioPropiedades
from propiedad.dominio.entidades import Proveedor, Aeropuerto, Propiedad
from propiedad.dominio.fabricas import FabricaPropiedades
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedad
from uuid import UUID

class RepositorioPropiedadesSQLite(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        evento_dto = PropiedadDTO()
        evento_dto.tipo_propiedad = propiedad.tipo_propiedad
        evento_dto.descripcion_propiedad = propiedad.descripcion_propiedad
        db.session.add(evento_dto)

    def actualizar(self, propiedad: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        # TODO
        raise NotImplementedError