import sys
from flask import Flask, jsonify, request
from flask_login import LoginManager, current_user, login_required
from models import db, Lic, User
from datetime import date
from schemas import ma, lic_schema, lic_schema_light, lic_schemas, user_schema

login_manager = LoginManager()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lics.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Flask-SQLAlchemy debe de ser inicializado antes de Flask-Marshmallow.
db.init_app(app)
ma.init_app(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if not api_key:
        return None
    return User.query.filter_by(api_key=api_key).first()


@app.route("/whoami")
def who_am_i():
    if current_user.is_authenticated:
        name = current_user.name
    else:
        name = "anonymous"
    return jsonify({"name": name})


@app.route("/profile")
@login_required
def user_profile():
    return user_schema.jsonify(current_user)


@app.route("/lics/<int:id>")
def get_lic(id):
    lic = Lic.query.first_or_404(id)
    return lic_schema.jsonify(lic)


@app.route("/lics/", methods=["GET"])
@login_required
def list_lics():
    all_lics = Lic.query.all()
    return lic_schemas.jsonify(all_lics)


@app.route("/lics/", methods=["POST"])
def create_lic():
    lic, errors = lic_schema_light.load(request.json)
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    lic.status = 1
    db.session.add(lic)
    db.session.commit()

    # Return HTTP
    # location = url_for("get_lic", serial=request.json["serial"])
    response = jsonify({"message": "Licencia creada correctamente"})
    response.status_code = 201
    response.headers["Location"] = lic.url
    return response


@app.route("/lics/<int:id>", methods=["PUT"])
def update_lic(id):
    lic = Lic.query.first_or_404(id)
    lic, errors = lic_schema.load(request.json, instance=lic)
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    db.session.add(lic)
    db.session.commit()

    return jsonify({"message": "Licencia actualizada correctamente"})


@app.route("/lics/<int:id>", methods=["DELETE"])
def delete_lic(id):
    lic = Lic.query.first_or_404(id)

    db.session.delete(lic)
    db.session.commit()

    return jsonify({"message": "Licencia eliminada correctamente"})


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


if __name__ == "__main__":
    if "createdb" in sys.argv:
        with app.app_context():
            db.create_all()
            print("Base de datos Creada")
    elif "loaddata" in sys.argv:
        with app.app_context():

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
    else:
        app.run(debug=True)
