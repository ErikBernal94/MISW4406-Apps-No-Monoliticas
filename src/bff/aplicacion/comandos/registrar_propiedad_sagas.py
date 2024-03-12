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

@dataclass
class RegistrarPropiedadSagas(Comando):
    tipo: str
    descripcion: str
    id: str

class RegistrarPropiedadSagaHandler(CrearPropiedadBaseHandler):
    
    def handle(self, comando: RegistrarPropiedadSagas):
        propiedad_dto = PropiedadDTO(
                descripcion_propiedad= comando.descripcion,
                tipo_propiedad=comando.tipo,
                id_propiedad=comando.id)
        print('RegistrarPropiedadSagaHandler: ', comando.id)
        despachador = Despachador()
        despachador.f(propiedad_dto, 'comando-registrar-propiedad')


@comando.register(RegistrarPropiedadSagas)
def ejecutar_comando_registrar_propiedad_saga(comando: RegistrarPropiedadSagas):
    handler = RegistrarPropiedadSagaHandler()
    handler.handle(comando)

# Ver propiedad Saga Registrada
@dataclass
class VerPropiedadSagas(Comando):
    tipo: str
    descripcion: str
    id: str

class VerPropiedadSagasHandler(CrearPropiedadBaseHandler):    
    def handle(self, comando: VerPropiedadSagas):
        propiedad_dto = PropiedadDTO(
                descripcion_propiedad= comando.descripcion,
                tipo_propiedad=comando.tipo,
                id_propiedad=comando.id)
        
        despachador = Despachador()
        despachador.publicar_evento_propiedad(propiedad_dto, 'evento-propiedades')

@comando.register(VerPropiedadSagas)
def ejecutar_comando_ver_propiedad_sagas(comando: VerPropiedadSagas):
    handler = VerPropiedadSagasHandler()
    handler.handle(comando)