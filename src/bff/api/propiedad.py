import bff.seedwork.presentacion.api as api
import json
from bff.aplicacion.dto import ContratoDTO

from flask import redirect, render_template, request, session, url_for
from flask import Response
from bff.aplicacion.mapeadores import MapeadorContratoDTOJson
from bff.aplicacion.comandos.registrar_propiedad import CrearPropiedad
from bff.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('propiedad', '/propiedades')

@bp.route('/registrar', methods=('POST',))
def propiedad_asincrona():
    propiedad_dict = request.json

    map_propiedad = MapeadorPropiedadDTOJson()
    propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

    comando = CrearPropiedad(id=propiedad_dto.id_propiedad, tipo= propiedad_dto.tipo_propiedad, descripcion=propiedad_dto.descripcion_contrato)

    ejecutar_commando(comando)
    
    return Response('{}', status=202, mimetype='application/json')
