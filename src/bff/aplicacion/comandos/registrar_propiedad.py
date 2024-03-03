from bff.seedwork.aplicacion.comandos import Comando
from bff.aplicacion.dto import PropiedadDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from bff.seedwork.aplicacion.comandos import ejecutar_commando as comando
from bff.infraestructura.despachadores import Despachador

@dataclass
class CrearPropiedad(Comando):
    tipo: str
    descripcion: str
    id: str


class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    
    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
                descripcion_propiedad= comando.descripcion,
                tipo_propiedad=comando.tipo,
                id_propiedad=comando.id)
        
        despachador = Despachador()
        despachador.publicar_evento_propiedad(propiedad_dto, 'eventos-propiedad')


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
