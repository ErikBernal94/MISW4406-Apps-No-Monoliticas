from compania.seedwork.dominio.repositorios import Mapeador
from compania.dominio.entidades import Compania
from .dto import Compania as CompaniaDTO

class MapeadorCompania(Mapeador):
    
    def obtener_tipo(self) -> type:
        return Compania.__class__

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        
        compania_dto = CompaniaDTO()
        compania_dto.correo_electronico = entidad.correo_electronico
        compania_dto.direccion = entidad.direccion
        compania_dto.id = str(entidad.id)

        return compania_dto

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:

        return Compania(correo_electronico= dto.correo_electronico, direccion=dto.direccion )