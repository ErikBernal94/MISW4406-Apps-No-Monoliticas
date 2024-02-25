from bff.seedwork.aplicacion.comandos import Comando
from bff.aplicacion.dto import ContratoDTO
from .base import CrearContratoBaseHandler
from dataclasses import dataclass, field
from bff.seedwork.aplicacion.comandos import ejecutar_commando as comando
from bff.infraestructura.despachadores import Despachador

@dataclass
class CrearContrato(Comando):
    tipo: str
    estado: str
    id: str


class CrearContratoHandler(CrearContratoBaseHandler):
    
    def handle(self, comando: CrearContrato):
        contrato_dto = ContratoDTO(
                estado_contrato= comando.estado,
                tipo_contrato=comando.tipo,
                id_contrato=comando.id)
        
        despachador = Despachador()
        despachador.publicar_evento_contrato(contrato_dto, 'eventos-contrato')

        


@comando.register(CrearContrato)
def ejecutar_comando_crear_contrato(comando: CrearContrato):
    handler = CrearContratoHandler()
    handler.handle(comando)
    