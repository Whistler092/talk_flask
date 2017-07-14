from flask import Flask

app = Flask(__name__)


@app.route("/")
def init():
    return "<h1>Hola Python Cali!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
