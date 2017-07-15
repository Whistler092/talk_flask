from flask import Blueprint, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from app.schemas.schemas import lic_schema, lic_schema_light, lic_schemas
from app.models.lic import Lic

mod = Blueprint("lic", __name__, url_prefix="/api/lic")


@mod.route("/<int:id>")
def get_lic(id):
    lic , error = Lic.query.filer_by(id=id).first_or_404()
    if not error:
        return lic_schema.jsonify(lic)
    else:
        abort(404)


@mod.route("/", methods=["GET"])
# @login_required
def list_lics():
    all_lics = Lic.query.all()
    return lic_schemas.jsonify(all_lics)


@mod.route("/", methods=["POST"])
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


@mod.route("/<int:id>", methods=["PUT"])
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


@mod.route("/<int:id>", methods=["DELETE"])
def delete_lic(id):
    lic = Lic.query.first_or_404(id)

    db.session.delete(lic)
    db.session.commit()

    return jsonify({"message": "Licencia eliminada correctamente"})
