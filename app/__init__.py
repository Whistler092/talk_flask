import os

from flask import Flask, jsonify
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from .utils import prepare_json_response

login_manager = LoginManager()

# Init Core
app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)
ma = Marshmallow(app)

db.init_app(app)
ma.init_app(app)
login_manager.init_app(app)

# Modelos

from app.models.user import User
from app.models.lic import Lic


if not os.path.exists("./app/db.sqlite"):
    db.create_all()
    print("Base de datos Creada")
    from datetime import date

    usr = User(name='Ramiro Bedoya', api_key='asdf')
    lic1 = Lic(name='Empresa 1', serial='CYIZ-55IA-TVI8',
               status=True, support_date=date(2018, 3, 24)
               )
    lic2 = Lic(name='Empresa 2', serial='W98T-OFKX-QXDF',
               status=1, support_date=date(2017, 1, 10))
    lic3 = Lic(name='Empresa XYZ', serial='J36L-58EU-OBDF',
               status=1, support_date=date(2017, 12, 30))
    db.session.add_all([lic1, lic2, lic3, usr])
    db.session.commit()
    print("Datos cargados")

from app.api_v1 import users
from app.api_v1 import lics

app.register_blueprint(lics.mod)
app.register_blueprint(users.mod)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if not api_key:
        return None
    return User.query.filter_by(api_key=api_key).first()


# -- Error handlers

# Override the default handlers with JSON responses
@app.errorhandler(400)
def forbidden(error):
    """
    Renders 400 response
    :returns: JSON
    :rtype: flask.Response
    """
    return jsonify(
        prepare_json_response(
            message="Error 400: Bad request",
            success=False,
            data=None
        )
    ), 400


@app.errorhandler(401)
def page_not_found(error):
    """
    Source http://flask.pocoo.org/docs/0.12/patterns/errorpages/
    :param error:
    :return:
    """
    resp = jsonify({"error": "No estás autorizado para entrar a la URL Solicitada"})
    resp.status_code = 401
    return resp


@app.errorhandler(403)
def forbidden(error):
    """
    Renders 403 response
    :returns: JSON
    :rtype: flask.Response
    """
    return jsonify(
        prepare_json_response(
            message="Error 403: Forbidden",
            success=False,
            data=None
        )
    ), 403


@app.errorhandler(404)
def page_not_found(error):
    """
    Source http://flask.pocoo.org/docs/0.12/patterns/errorpages/
    :param error:
    :return:
    """
    resp = jsonify({"error": "No encontrado"})
    resp.status_code = 404
    return resp


@app.errorhandler(405)
def not_found(error):
    """
    Renders 405 response
    :returns: JSON
    :rtype: flask.Response
    """
    return jsonify(
        prepare_json_response(
            message="Error 405: Method not allowed",
            success=False,
            data=None
        )
    ), 405


@app.errorhandler(500)
def internal_server_error(error):
    """
    Renders 500 response
    :returns: JSON
    :rtype: flask.Response
    """

    return jsonify(
        prepare_json_response(
            message="Error 500: Error interno del servidor",
            success=False,
            data=None
        )
    ), 405
