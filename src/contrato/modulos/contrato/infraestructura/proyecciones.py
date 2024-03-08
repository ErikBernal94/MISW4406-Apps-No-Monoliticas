from contrato.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from contrato.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from contrato.modulos.contrato.infraestructura.fabricas import FabricaRepositorio
from contrato.modulos.contrato.infraestructura.respositorios import RepositorioContratos
from contrato.modulos.contrato.dominio.entidades import Contrato

from abc import ABC, abstractmethod
import logging
import traceback
from .dto import Contrato

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
        # record = db.session.query(Contrato).one_or_none()
        # record = db.session.query(Contrato).filter_by(fecha_creacion=self.fecha_creacion.date()).one_or_none()

        if record and self.operacion == self.ADD:
            record.total += 1
        elif record and self.operacion == self.DELETE:
            record.total -= 1 
            record.total = max(record.total, 0)
        # else:
            # db.session.add(Contrato())
            # db.session.add(Contrato(fecha_creacion=self.fecha_creacion.date(), total=1))
        
        db.session.commit()

class ProyeccionReservasLista(ProyeccionReserva):
    def __init__(self, id_contrato, correo_electronico, direccion, fecha_creacion, fecha_actualizacion):
        self.id_contrato = id
        self.correo_electronico = correo_electronico
        self.direccion = direccion
        # self.fecha_creacion = millis_a_datetime(fecha_creacion)
        # self.fecha_actualizacion = millis_a_datetime(fecha_actualizacion)
    
    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioContratos)
        
        # TODO Haga los cambios necesarios para que se consideren los itinerarios, demás entidades y asociaciones
        repositorio.agregar(
            Contrato(
                id=str(self.id_contrato), 
                correo_electronico=str(self.correo_electronico), 
                direccion=str(self.direccion)))
        
        # TODO ¿Y si la reserva ya existe y debemos actualizarla? Complete el método para hacer merge

        # TODO ¿Tal vez podríamos reutilizar la Unidad de Trabajo?
        db.session.commit()

class ProyeccionReservaHandler(ProyeccionHandler):
    
    def handle(self, proyeccion: ProyeccionReserva):

        # TODO El evento de creación no viene con todos los datos de itinerarios, esto tal vez pueda ser una extensión
        # Asi mismo estamos dejando la funcionalidad de persistencia en el mismo método de recepción. Piense que componente
        # podriamos diseñar para alojar esta funcionalidad
        from contrato.config.db import db

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
