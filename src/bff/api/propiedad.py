import bff.seedwork.presentacion.api as api
import json
from bff.aplicacion.dto import PropiedadDTO

from flask import redirect, render_template, request, session, url_for
from flask import Response
from bff.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from bff.aplicacion.comandos.registrar_propiedad_sagas import CrearPropiedadSagas, RegistrarPropiedadSagas, VerPropiedadSagas
from bff.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('propiedad', '/propiedades')

@bp.route('/registrar', methods=('POST',))
def propiedad_asincrona():
    propiedad_dict = request.json

    map_propiedad = MapeadorPropiedadDTOJson()
    propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

    comando = CrearPropiedad(id=propiedad_dto.id_propiedad, tipo= propiedad_dto.tipo_propiedad, descripcion=propiedad_dto.descripcion_propiedad)

    ejecutar_commando(comando)
    
    return Response('{}', status=202, mimetype='application/json')


bp = api.crear_blueprint('propiedad', '/propiedades')

@bp.route('/registrar-sagas', methods=('POST',))
async def app_startup():
    print('entra por la url')
    propiedad_dict = request.json
    map_propiedad = MapeadorPropiedadDTOJson()
    propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
    print(propiedad_dto)
    comando = CrearPropiedadSagas(id=propiedad_dto.id_propiedad, tipo= propiedad_dto.tipo_propiedad, descripcion=propiedad_dto.descripcion_propiedad)

    ejecutar_commando(comando)
    
    return Response('{}', status=202, mimetype='application/json')


    @app.on_event("shutdown")
    def shutdown_event():
        global tasks
        for task in tasks:
            task.cancel()

@bp.route("/propiedad-registrada-sagas", methods=('GET',))
async def ver_propiedad_registrada():
    print('entra por la url -> propiedad-registrada-sagas')
    #propiedad_dict = request.json
    #map_propiedad = MapeadorPropiedadDTOJson()
    #propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
    #print(propiedad_dto)
    comando = VerPropiedadSagas(id="1", tipo="tipo_propiedad", descripcion="descripcion_propiedad")

    ejecutar_commando(comando)
    
    return Response('{}', status=202, mimetype='application/json')

    @app.on_event("shutdown")
    def shutdown_event():
        global tasks
        for task in tasks:
            task.cancel()

@bp.route("/registrar-propiedad-sagas", methods=('GET','POST'))
async def registrar_propiedad():
    print('entra por la url -> registrar-propiedad-sagas')
    #propiedad_dict = request.json
    #map_propiedad = MapeadorPropiedadDTOJson()
    #propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
    #print(propiedad_dto)
    comando = f(id="1", tipo="tipo_propiedad", descripcion="descripcion_propiedad")

    ejecutar_commando(comando)
    
    return Response('{}', status=202, mimetype='application/json')

    @app.on_event("shutdown")
    def shutdown_event():
        global tasks
        for task in tasks:
            task.cancel()