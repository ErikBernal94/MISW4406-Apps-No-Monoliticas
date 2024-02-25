from bff.seedwork.aplicacion.comandos import Comando
from bff.aplicacion.dto import CompaniaDTO
from .base import CrearCompaniaBaseHandler
from dataclasses import dataclass, field
from bff.seedwork.aplicacion.comandos import ejecutar_commando as comando
from bff.aplicacion.mapeadores import MapeadorCompania
from bff.dominio.entidades import Compania
from bff.infraestructura.despachadores import Despachador

@dataclass
class CrearCompania(Comando):
    direccion: str
    correo_electronico: str
    id: str


class CrearCompaniaHandler(CrearCompaniaBaseHandler):
    
    def handle(self, comando: CrearCompania):
        compania_dto = CompaniaDTO(
                correo_electronico=comando.correo_electronico
            ,   direccion=comando.direccion    
            ,   id_compania=comando.id)

        compania: Compania = self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())
        
        despachador = Despachador()
        despachador.publicar_evento_compania(compania, 'eventos-compania')

        


@comando.register(CrearCompania)
def ejecutar_comando_crear_compania(comando: CrearCompania):
    handler = CrearCompaniaHandler()
    handler.handle(comando)
    