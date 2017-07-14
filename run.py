from flask import Flask, jsonify, abort

app = Flask(__name__)

lics = {
    'CYIZ-55IA-TVI8': {
        'name': 'Empresa 1',
        'serial': 'CYIZ-55IA-TVI8',
        'status': 1,
        'support_date': '5/01/2018',
    },
    'W98T-OFKX-QXDF': {
        'name': 'Empresa 2',
        'serial': 'W98T-OFKX-QXDF',
        'status': 1,
        'support_date': '10/01/2017',
    },
    'J36L-58EU-OBDF': {
        'name': 'Empresa XYZ',
        'serial': 'J36L-58EU-OBDF',
        'status': 1,
        'support_date': '15/12/2017',
    },
    'Q9KF-9UBT-6XEO': {
        'name': 'Empresa WWW',
        'serial': 'Q9KF-9UBT-6XEO',
        'status': 1,
        'support_date': '01/08/2018',
    }
}


@app.route("/<string:key_word>")
def get_lic(key_word):
    try:
        lic = lics[key_word]
    except IndexError:
        abort(404)
    return jsonify(lic)


if __name__ == "__main__":
    app.run(debug=True)
