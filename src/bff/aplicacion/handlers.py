from bff.seedwork.aplicacion.handlers import Handler
from bff.infraestructura.despachadores import Despachador

class HandlerCompaniaIntegracion(Handler):

    @staticmethod
    def handle_compania_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento_compania(evento, 'eventos-compania')

class HandlerContratoIntegracion(Handler):

    @staticmethod
    def handle_contrato_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento_contrato(evento, 'eventos-contrato')


    