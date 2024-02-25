import bff.seedwork.presentacion.api as api
import json
from bff.aplicacion.dto import ContratoDTO

from flask import redirect, render_template, request, session, url_for
from flask import Response
from bff.aplicacion.mapeadores import MapeadorContratoDTOJson
from bff.aplicacion.comandos.registrar_contrato import CrearContrato
from bff.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('contrato', '/contratos')

@bp.route('/registrar', methods=('POST',))
def contrator_asincrona():
    contrato_dict = request.json

    map_contrato = MapeadorContratoDTOJson()
    contrato_dto = map_contrato.externo_a_dto(contrato_dict)

    comando = CrearContrato(id=contrato_dto.id_contrato, tipo= contrato_dto.tipo_contrato, estado=contrato_dto.estado_contrato)
    
    ejecutar_commando(comando)
    
    return Response('{}', status=202, mimetype='application/json')