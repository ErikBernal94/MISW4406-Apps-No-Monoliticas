from bff.seedwork.aplicacion.queries import QueryHandler
from bff.dominio.fabricas import _FabricaCompania, _FabricaContrato

class ReservaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_compania: _FabricaCompania = _FabricaCompania()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_compania(self):
        return self._fabrica_compania    