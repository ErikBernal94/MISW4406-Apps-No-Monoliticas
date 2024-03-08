from contrato.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from contrato.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from contrato.modulos.contrato.infraestructura.fabricas import FabricaRepositorio
from contrato.modulos.contrato.infraestructura.repositorios import RepositorioContratos
from contrato.modulos.contrato.dominio.entidades import Contrato

from abc import ABC, abstractmethod
import logging
import traceback
from .dto import Contrato

class ProyeccionContrato(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...

class ProyeccionContratosLista(ProyeccionContrato):
    def __init__(self, id_contrato, tipo_contrato, estado_contrato, fecha_creacion, fecha_actualizacion):
        self.id_contrato = id
        self.tipo_contrato = tipo_contrato
        self.estado_contrato = estado_contrato
        # self.fecha_creacion = millis_a_datetime(fecha_creacion)
        # self.fecha_actualizacion = millis_a_datetime(fecha_actualizacion)
    
    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioContratos)
        
        repositorio.agregar(
            Contrato(
                id=str(self.id_contrato), 
                tipo_contrato=str(self.tipo_contrato), 
                estado_contrato=str(self.estado_contrato)))

        db.session.commit()

class ProyeccionContratoHandler(ProyeccionHandler):
    
    def handle(self, proyeccion: ProyeccionContrato):

        from contrato.config.db import db

        proyeccion.ejecutar(db=db)


@proyeccion.register(ProyeccionContratosLista)
def ejecutar_proyeccion_Contrato(proyeccion, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionContratoHandler()
            handler.handle(proyeccion)
            
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')
