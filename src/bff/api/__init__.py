import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

def registrar_handlers():
    import bff.aplicacion

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

    registrar_handlers()

    app.run(debug=True, port=5000)

    # Importa Blueprints
    from . import compania
    from . import contrato
    from . import propiedad

    # Registro de Blueprints
    app.register_blueprint(compania.bp)
    app.register_blueprint(contrato.bp)
    app.register_blueprint(propiedad.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
