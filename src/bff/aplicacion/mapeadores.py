from bff.seedwork.aplicacion.dto import Mapeador as AppMap
from bff.seedwork.dominio.repositorios import Mapeador as RepMap
from bff.dominio.entidades import Compania, Contrato, Propiedad
from .dto import CompaniaDTO, ContratoDTO, PropiedadDTO

from datetime import datetime

class MapeadorCompaniaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> CompaniaDTO:
        compania_dto = CompaniaDTO(correo_electronico=externo['correo_electronico'],direccion=externo['direccion'], id_compania=externo['id'])
        return compania_dto

    def dto_a_externo(self, dto: CompaniaDTO) -> dict:
        return dto.__dict__

class MapeadorCompania(RepMap):

    def obtener_tipo(self) -> type:
        return Compania.__class__

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        
        correo_electronico = entidad.correo_electronico
        direccion = entidad.direccion
        _id = str(entidad.id)
        
        return CompaniaDTO(direccion= direccion, correo_electronico=correo_electronico, id_compania= _id)

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania(correo_electronico=dto.correo_electronico,direccion=dto.direccion, id_compania=dto.id_compania)
        return compania
    

class MapeadorContratoDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> ContratoDTO:
        contrato_dto = ContratoDTO(tipo_contrato=externo['tipo_contrato'], estado_contrato=externo['estado_contrato'], id_contrato=externo['id'])
        return contrato_dto

    def dto_a_externo(self, dto: ContratoDTO) -> dict:
        return dto.__dict__

class MapeadorContrato(RepMap):

    def obtener_tipo(self) -> type:
        return Contrato.__class__

    def entidad_a_dto(self, entidad: Contrato) -> ContratoDTO:
        
        tipo = entidad.tipo_contrato
        estato = entidad.estado_contrato
        _id = str(entidad.id)
        
        return ContratoDTO(tipo_contrato=tipo, estado_contrato=estato, id_contrato= _id)

    def dto_a_entidad(self, dto: ContratoDTO) -> Contrato:
        contrato = Contrato(tipo_contrato=dto.tipo_contrato, estado_contrato=dto.estado_contrato, id_contrato=dto.id_contrato)
        return contrato


class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO(tipo_propiedad=externo['tipo_propiedad'], descripcion_propiedad=externo['descripcion_propiedad'], id_propiedad=externo['id_propiedad'])
        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__

class MapeadorPropiedad(RepMap):

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:

        tipo = entidad.tipo_propiedad
        descripcion = entidad.descripcion_propiedad
        _id = str(entidad.id)

        return PropiedadDTO(tipo_propiedad=tipo, descripcion_propiedad=descripcion, id_propiedad= _id)

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(tipo_propiedad=dto.tipo_propiedad, descripcion_propiedad=dto.descripcion_propiedad, id_propiedad=dto.id_propiedad)
        return contrato
