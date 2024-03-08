from propiedad.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from propiedad.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from propiedad.infraestructura.fabricas import FabricaRepositorio
from propiedad.infraestructura.repositorios import RepositorioPropiedades
from propiedad.dominio.entidades import Propiedad

from abc import ABC, abstractmethod
import logging
import traceback
from .dto import Propiedad

class ProyeccionReserva(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...

class ProyeccionReservasTotales(ProyeccionReserva):
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
        # record = db.session.query(Propiedad).one_or_none()
        # record = db.session.query(Propiedad).filter_by(fecha_creacion=self.fecha_creacion.date()).one_or_none()

        if record and self.operacion == self.ADD:
            record.total += 1
        elif record and self.operacion == self.DELETE:
            record.total -= 1 
            record.total = max(record.total, 0)
        # else:
            # db.session.add(Propiedad())
            # db.session.add(Propiedad(fecha_creacion=self.fecha_creacion.date(), total=1))
        
        db.session.commit()

class ProyeccionReservasLista(ProyeccionReserva):
    def __init__(self, id_propiedad, correo_electronico, direccion, fecha_creacion, fecha_actualizacion):
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

class ProyeccionReservaHandler(ProyeccionHandler):
    
    def handle(self, proyeccion: ProyeccionReserva):

        from propiedad.config.db import db

        proyeccion.ejecutar(db=db)


@proyeccion.register(ProyeccionReservasLista)
@proyeccion.register(ProyeccionReservasTotales)
def ejecutar_proyeccion_reserva(proyeccion, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionReservaHandler()
            handler.handle(proyeccion)
            
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')
