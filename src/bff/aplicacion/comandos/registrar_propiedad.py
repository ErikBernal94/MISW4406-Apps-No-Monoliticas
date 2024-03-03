from bff.seedwork.aplicacion.comandos import Comando
from bff.aplicacion.dto import ContratoDTO
from .base import CrearContratoBaseHandler
from dataclasses import dataclass, field
from bff.seedwork.aplicacion.comandos import ejecutar_commando as comando
from bff.infraestructura.despachadores import Despachador

@dataclass
class CrearPropiedad(Comando):
    tipo: str
    descripcion: str
    id: str


class CrearPropiedadHandler(CrearContratoBaseHandler):
    
    def handle(self, comando: CrearContrato):
        propiedad_dto = PropiedadDTO(
                descripcion_propiedad= comando.descripcion,
                tipo_propiedad=comando.tipo,
                id_propiedad=comando.id)
        
        despachador = Despachador()
        despachador.publicar_evento_contrato(contrato_dto, 'eventos-contrato')


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearContratoHandler()
    handler.handle(comando)
