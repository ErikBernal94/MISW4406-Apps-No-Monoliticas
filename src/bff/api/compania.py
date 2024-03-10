import bff.seedwork.presentacion.api as api
import json
from bff.aplicacion.dto import CompaniaDTO

from flask import redirect, render_template, request, session, url_for
from flask import Response
from bff.aplicacion.mapeadores import MapeadorCompaniaDTOJson
from bff.aplicacion.comandos.registrar_compania import CrearCompania
from bff.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('compania', '/companias')

@bp.route('/registrar', methods=('POST',))
def companiar_asincrona():
    compania_dict = request.json

    map_compania = MapeadorCompaniaDTOJson()
    compania_dto = map_compania.externo_a_dto(compania_dict)

    comando = CrearCompania(correo_electronico= compania_dto.correo_electronico, direccion=compania_dto.direccion, id= compania_dto.id_compania)
    
    ejecutar_commando(comando)
    
    return Response('{}', status=202, mimetype='application/json')

@bp.route('/modificar_datos', methods=('PUT',))
def companiar_asincrona():
    compania_dict = request.json

    map_compania = MapeadorCompaniaDTOJson()
    compania_dto = map_compania.externo_a_dto(compania_dict)

    comando = CrearCompania(correo_electronico= compania_dto.correo_electronico, direccion=compania_dto.direccion, id= compania_dto.id_compania)
    
    ejecutar_commando(comando)
    
    return Response('{}', status=202, mimetype='application/json')