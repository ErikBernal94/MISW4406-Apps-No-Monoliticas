from contrato.config.db import db
from contrato.modulos.contrato.dominio.repositorios import RepositorioContratos
from contrato.modulos.contrato.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from contrato.modulos.contrato.dominio.entidades import Proveedor, Aeropuerto, Contrato
from contrato.modulos.contrato.dominio.fabricas import _FabricaContratos
from .dto import Contrato as ContratoDTO
from .mapeadores import MapeadorContrato
from uuid import UUID

class RepositorioContratosSQLite(RepositorioContratos):

    def __init__(self):
        self._fabrica_contratos: _FabricaContratos = _FabricaContratos()

    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos

    def obtener_por_id(self, id: UUID) -> Contrato:
        contrato_dto = db.session.query(ContratoDTO).filter_by(id=str(id)).one()
        return self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())

    def obtener_todos(self) -> list[Contrato]:
        # TODO
        raise NotImplementedError

    def agregar(self, contrato: Contrato):
        contrato_dto = self.fabrica_contratos.crear_objeto(contrato, MapeadorContrato())
        db.session.add(contrato_dto)

    def actualizar(self, contrato: Contrato):
        # TODO
        raise NotImplementedError

    def eliminar(self, contrato_id: UUID):
        # TODO
        raise NotImplementedError