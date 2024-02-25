from bff.seedwork.aplicacion.comandos import ComandoHandler
from bff.dominio.fabricas import _FabricaCompania, _FabricaContrato

class CrearCompaniaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_companias: _FabricaCompania = _FabricaCompania()
    
    @property
    def fabrica_companias(self):
        return self._fabrica_companias    
    
class CrearContratoBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_contratos: _FabricaContrato = _FabricaContrato()
    
    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos    