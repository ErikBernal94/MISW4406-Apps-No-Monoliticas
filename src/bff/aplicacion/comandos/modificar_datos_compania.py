from bff.seedwork.aplicacion.comandos import Comando
from bff.aplicacion.dto import CompaniaDTO
from .base import CrearCompaniaBaseHandler
from dataclasses import dataclass, field
from bff.seedwork.aplicacion.comandos import ejecutar_commando as comando
from bff.aplicacion.mapeadores import MapeadorCompania
from bff.dominio.entidades import Compania
from bff.infraestructura.despachadores import Despachador

@dataclass
class ModificarDatosCompania(Comando):
    direccion: str
    correo_electronico: str
    id: str


class ModificarDatosHandler(CrearCompaniaBaseHandler):
    
    def handle(self, comando: ModificarDatosCompania):
        compania_dto = CompaniaDTO(
                correo_electronico=comando.correo_electronico
            ,   direccion=comando.direccion    
            ,   id_compania=comando.id)

        compania: Compania = self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())
        
        despachador = Despachador()
        despachador.publicar_evento_compania(compania, 'eventos-compania')

        


@comando.register(ModificarDatosCompania)
def ejecutar_comando_crear_compania(comando: ModificarDatosCompania):
    handler = ModificarDatosHandler()
    handler.handle(comando)
    