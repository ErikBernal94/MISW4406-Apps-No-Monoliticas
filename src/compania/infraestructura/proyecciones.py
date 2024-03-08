from compania.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from compania.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from compania.infraestructura.fabricas import FabricaRepositorio
from compania.infraestructura.repositorios import RepositorioCompanias
from compania.dominio.entidades import Compania

from abc import ABC, abstractmethod
import logging
import traceback
from .dto import Compania
# from compania.seedwork.infraestructura.utils import millis_a_datetime

class ProyeccionCompania(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...

class ProyeccionCompaniasTotales(ProyeccionCompania):
    ADD = 1
    DELETE = 2
    UPDATE = 3

    def __init__(self, fecha_creacion, operacion):
        # self.fecha_creacion = millis_a_datetime(fecha_creacion)
        self.operacion = operacion

    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        # NOTE esta no usa repositorios y de una vez aplica los cambios. Es decir, no todo siempre debe ser un repositorio
        record = None
        # record = db.session.query(Compania).one_or_none()
        # record = db.session.query(Compania).filter_by(fecha_creacion=self.fecha_creacion.date()).one_or_none()

        if record and self.operacion == self.ADD:
            record.total += 1
        elif record and self.operacion == self.DELETE:
            record.total -= 1 
            record.total = max(record.total, 0)
        # else:
            # db.session.add(Compania())
            # db.session.add(Compania(fecha_creacion=self.fecha_creacion.date(), total=1))
        
        db.session.commit()

class ProyeccionCompaniasLista(ProyeccionCompania):
    def __init__(self, id_compania, correo_electronico, direccion, fecha_creacion, fecha_actualizacion):
        self.id_compania = id
        self.correo_electronico = correo_electronico
        self.direccion = direccion
        # self.fecha_creacion = millis_a_datetime(fecha_creacion)
        # self.fecha_actualizacion = millis_a_datetime(fecha_actualizacion)
    
    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioCompanias)
        
        repositorio.agregar(
            Compania(
                id=str(self.id_compania), 
                correo_electronico=str(self.correo_electronico), 
                direccion=str(self.direccion)))

        db.session.commit()

class ProyeccionCompaniaHandler(ProyeccionHandler):
    
    def handle(self, proyeccion: ProyeccionCompania):
        from compania.config.db import db

        proyeccion.ejecutar(db=db)


@proyeccion.register(ProyeccionCompaniasLista)
@proyeccion.register(ProyeccionCompaniasTotales)
def ejecutar_proyeccion_compania(proyeccion, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionCompaniaHandler()
            handler.handle(proyeccion)
            
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')
