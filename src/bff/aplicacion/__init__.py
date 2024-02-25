from pydispatch import dispatcher

from .handlers import HandlerCompaniaIntegracion, HandlerContratoIntegracion

from bff.dominio.eventos import CompaniaRegistrada, ContratoRegistrado

dispatcher.connect(HandlerCompaniaIntegracion.handle_compania_creada, signal=f'{CompaniaRegistrada.__name__}Integracion')
dispatcher.connect(HandlerContratoIntegracion.handle_contrato_creada, signal=f'{ContratoRegistrado.__name__}Integracion')
