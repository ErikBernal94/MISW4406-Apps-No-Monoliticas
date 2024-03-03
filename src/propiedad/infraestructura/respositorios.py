from propiedad.config.db import db
from propiedad.dominio.repositorios import RepositorioPropiedads
from propiedad.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from propiedad.dominio.entidades import Proveedor, Aeropuerto, Propiedad
from propiedad.dominio.fabricas import FabricaPropiedads
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedad
from uuid import UUID

class RepositorioPropiedadsSQLite(RepositorioPropiedads):

    def __init__(self):
        self._fabrica_propiedads: FabricaPropiedads = FabricaPropiedads()

    @property
    def fabrica_propiedads(self):
        return self._fabrica_propiedads

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedads.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_propiedads.crear_objeto(propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)

    def actualizar(self, propiedad: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        # TODO
        raise NotImplementedError