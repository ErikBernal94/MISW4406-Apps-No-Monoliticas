from propiedad.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from propiedad.seedwork.aplicacion.comandos import Comando
from propiedad.seedwork.dominio.eventos import EventoDominio

from propiedad.modulos.sagas.aplicacion.comandos.propiedad import RegistrarPropiedad, RegistrarPropiedadRevertida, RegistrarPropiedadFallida
from propiedad.modulos.sagas.dominio.eventos.propiedad import PropiedadCreada, RegistroPropiedadFallida, RegistroPropiedadRevertida


class CoordinadorPropiedades(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearPropiedad, evento=PropiedadCreada, error=CreacionPropiedadFallida, compensacion=ReversarCrearPropiedad),
            Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorPropiedades()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
