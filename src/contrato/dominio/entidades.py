from __future__ import annotations
from dataclasses import dataclass, field

from contrato.dominio.objetos_valor import TipoContrato, EstadoContrato
from contrato.dominio.eventos import ContratoRegistrado
from contrato.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Contrato(AgregacionRaiz):
    id_contrato: uuid.UUID = field(hash=True, default=None)
    tipo_contrato: TipoContrato = None
    estado_contrato: EstadoContrato = None

    def registrar_contrato(self, contrato: Contrato):
        self.tipo_contrato = contrato.tipo_contrato
        self.estado_contrato = contrato.estado_contrato

        self.agregar_evento(ContratoRegistrado(id_contrato=self.id_contrato, estado_contrato=self.estado_contrato, tipo_contrato=self.estado_contrato))