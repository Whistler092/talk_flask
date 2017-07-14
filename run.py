import sys
from flask import Flask, jsonify, request, url_for
from models import db, Lic
from datetime import date
from schemas import ma, lic_schema, lic_schema_light, lic_schemas

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lics.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
ma.init_app(app)


@app.route("/lics/<serial>", methods=["GET"])
def get_lic(serial):
    lic = Lic.query.filter(Lic.serial == serial).first_or_404()
    # Si hubiera sido un ID
    # lic = Lic.query.first_or_404(id)
    return lic_schema_light.jsonify(lic)


@app.route("/lics/", methods=["GET"])
def list_lics():
    all_lics = Lic.query.all()
    return lic_schemas.jsonify(all_lics)


@app.route("/lics/", methods=["POST"])
def create_lic():
    # validamos los campos importantes

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


@app.route("/lics/<serial>", methods=["PUT"])
def update_lic(serial):
    lic = Lic.query.filter(Lic.serial == serial).first_or_404()
    lic, errors = lic_schema.load(request.json, instance=lic)
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    db.session.add(lic)
    db.session.commit()

    # Return HTTP
    # location = url_for("get_lic", serial=lic.serial)
    response = jsonify({"message": "Licencia actualizada correctamente"})
    response.status_code = 201
    response.headers["Location"] = lic.url

    return response


@app.route("/lics/<serial>", methods=["DELETE"])
def delete_lic(serial):
    lic = Lic.query.filter(Lic.serial == serial).first_or_404()

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
    resp = jsonify({"error": "not found"})
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    if "createdb" in sys.argv:
        with app.app_context():
            db.create_all()
            print("Base de datos Creada")
    elif "loaddata" in sys.argv:
        with app.app_context():
            lic1 = Lic(name='Empresa 1', serial='CYIZ-55IA-TVI8',
                       status=True, support_date=date(2018, 3, 24)
                       )
            db.session.add(lic1)

            lic2 = Lic(name='Empresa 2', serial='W98T-OFKX-QXDF',
                       status=1, support_date=date(2017, 1, 10))
            db.session.add(lic2)
            lic3 = Lic(name='Empresa XYZ', serial='J36L-58EU-OBDF',
                       status=1, support_date=date(2017, 12, 30))
            db.session.add(lic3)
            db.session.commit()
            print("Datos cargados")
    else:
        app.run(debug=True)
