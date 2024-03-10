from bff.seedwork.aplicacion.comandos import Comando
from bff.aplicacion.dto import PropiedadDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from bff.seedwork.aplicacion.comandos import ejecutar_commando as comando
from bff.infraestructura.despachadores import Despachador

@dataclass
class CrearPropiedadSagas(Comando):
    tipo: str
    descripcion: str
    id: str


class CrearPropiedadSagasHandler(CrearPropiedadBaseHandler):
    
    def handle(self, comando: CrearPropiedadSagas):
        propiedad_dto = PropiedadDTO(
                descripcion_propiedad= comando.descripcion,
                tipo_propiedad=comando.tipo,
                id_propiedad=comando.id)
        
        despachador = Despachador()
        despachador.publicar_evento_propiedad(propiedad_dto, 'eventos-propiedad')


@comando.register(CrearPropiedadSagas)
def ejecutar_comando_crear_propiedad_sagas(comando: CrearPropiedadSagas):
    handler = CrearPropiedadSagasHandler()
    handler.handle(comando)
