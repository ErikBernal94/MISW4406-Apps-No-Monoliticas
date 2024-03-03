from propiedad.seedwork.dominio.repositorios import Mapeador
from propiedad.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO

class MapeadorPropiedad(Mapeador):
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        
        propiedad_dto = PropiedadDTO()
        propiedad_dto.descripcion = entidad.descripcion_propiedad
        propiedad_dto.tipo = entidad.tipo_propiedad
        propiedad_dto.id = str(entidad.id_propiedad)

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        return Propiedad(dto.id, id_propiedad= dto.id, tipo_propiedad=dto.tipo, descripcion_propiedad=dto.descripcion )