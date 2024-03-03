from contrato.seedwork.dominio.repositorios import Mapeador
from contrato.modulos.contrato.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from contrato.modulos.contrato.dominio.entidades import Contrato
from .dto import Contrato as ContratoDTO

class MapeadorContrato(Mapeador):
    
    def obtener_tipo(self) -> type:
        return Contrato.__class__

    def entidad_a_dto(self, entidad: Contrato) -> ContratoDTO:
        
        contrato_dto = ContratoDTO()
        contrato_dto.estado = entidad.estado_contrato
        contrato_dto.tipo = entidad.tipo_contrato
        contrato_dto.id = str(entidad.id_contrato)

        return contrato_dto

    def dto_a_entidad(self, dto: ContratoDTO) -> Contrato:
        return Contrato(dto.id, id_contrato= dto.id, tipo_contrato=dto.tipo, estado_contrato=dto.estado )