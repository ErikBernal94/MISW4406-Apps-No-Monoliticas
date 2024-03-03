from bff.seedwork.aplicacion.queries import Query
from bff.aplicacion.dto import CompaniaDTO
from .base import BuscarCompaniaBaseHandler
from dataclasses import dataclass, field
from bff.seedwork.aplicacion.queries import ejecutar_query as query
from bff.aplicacion.mapeadores import MapeadorCompania
from bff.dominio.entidades import Compania
from bff.infraestructura.despachadores import Despachador

@dataclass
class BuscarCompania(Query):
    id: str


class BuscarCompaniaHandler(BuscarCompaniaBaseHandler):
    
    def handle(self, comando: BuscarCompania):
        compania_dto = CompaniaDTO(id_compania=comando.id)

        compania: Compania = self.fabrica_compania.crear_objeto(compania_dto, MapeadorCompania())
        
        despachador = Despachador()
        despachador.publicar_evento_compania(compania, 'eventos-compania')

        


@query.register(BuscarCompania)
def ejecutar_comando_crear_compania(query: BuscarCompania):
    handler = BuscarCompaniaHandler()
    handler.handle(query)
    