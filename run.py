from flask import Flask, jsonify, abort

app = Flask(__name__)

lics = [
    {
        'name': 'Empresa 1',
        'serial': 'CYIZ-55IA-TVI8',
        'status': 1,
        'support_date': '5/01/2018',
    },
    {
        'name': 'Empresa 2',
        'serial': 'W98T-OFKX-QXDF',
        'status': 1,
        'support_date': '10/01/2017',
    },
    {
        'name': 'Empresa XYZ',
        'serial': 'J36L-58EU-OBDF',
        'status': 1,
        'support_date': '15/12/2017',
    },
    {
        'name': 'Empresa WWW',
        'serial': 'Q9KF-9UBT-6XEO',
        'status': 1,
        'support_date': '01/08/2018',
    }
]


@app.route("/<int:index>")
def get_lic(index):
    try:
        lic = lics[index]
    except IndexError:
        abort(404)
    return jsonify(lic)


if __name__ == "__main__":
    app.run(debug=True)
