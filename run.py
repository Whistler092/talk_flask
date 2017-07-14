import sys
from flask import Flask, jsonify
from models import db, Lic
from datetime import date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lics.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)


@app.route("/<serial>")
def get_lic(serial):
    # lics = Lic.query.all()        Retorna una list
    # lic = Lic.query.filter(Lic.serial=="CYIZ-55IA-TVI8").first() Primera licencia que encuentre o None
    # lic = Lic.query.filter_by(Lic.serial=="CYIZ-55IA-TVI8").first() filter_by shortcut

    lic = Lic.query.filter(Lic.serial == serial).first_or_404()
    output = {
        "name": lic.name,
        "support_date": lic.support_date,
    }
    return jsonify(output)


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
