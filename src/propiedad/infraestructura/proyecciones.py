from propiedad.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from propiedad.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from propiedad.infraestructura.fabricas import FabricaRepositorio
from propiedad.infraestructura.repositorios import RepositorioPropiedades
from propiedad.dominio.entidades import Propiedad

from abc import ABC, abstractmethod
import logging
import traceback
from .dto import Propiedad

class ProyeccionPropiedad(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...

class ProyeccionPropiedadesLista(ProyeccionPropiedad):
    def __init__(self, id_propiedad, tipo_propiedad, descripcion_propiedad, fecha_creacion, fecha_actualizacion):
        self.id_propiedad = id
        self.tipo_propiedad = tipo_propiedad
        self.descripcion_propiedad = descripcion_propiedad
        # self.fecha_creacion = millis_a_datetime(fecha_creacion)
        # self.fecha_actualizacion = millis_a_datetime(fecha_actualizacion)
    
    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioPropiedades)
        
        repositorio.agregar(
            Propiedad(
                id=str(self.id_propiedad), 
                tipo_propiedad=str(self.tipo_propiedad), 
                descripcion_propiedad=str(self.descripcion_propiedad)))

        db.session.commit()

class ProyeccionPropiedadHandler(ProyeccionHandler):
    
    def handle(self, proyeccion: ProyeccionPropiedad):

        from propiedad.config.db import db

        proyeccion.ejecutar(db=db)


@proyeccion.register(ProyeccionPropiedadesLista)
def ejecutar_proyeccion_propiedad(proyeccion, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionPropiedadHandler()
            handler.handle(proyeccion)
            
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')
