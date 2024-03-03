from movimiento.seedwork.dominio.repositorios import Mapeador
from movimiento.modulos.movimiento_inmobiliario.dominio.entidades import MovimientoInmobiliario
from .dto import MovimientoInmobiliario as MovimientoDTO

class MapeadorMovimiento(Mapeador):
    
    def obtener_tipo(self) -> type:
        return MovimientoInmobiliario.__class__

    def entidad_a_dto(self, entidad: MovimientoInmobiliario) -> MovimientoDTO:
        
        movimiento_dto = MovimientoDTO()
        movimiento_dto.id = str(entidad.id_movimiento)

        return movimiento_dto

    def dto_a_entidad(self, dto: MovimientoDTO) -> MovimientoInmobiliario:
        return MovimientoInmobiliario(dto.id, id_movimiento= dto.id)