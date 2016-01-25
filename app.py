from flask import Flask, jsonify
from get_data import get_data, get_color_data, get_make_data, get_state_data


app = Flask(__name__)
# app.debug = True


@app.route("/")
def data():
    return jsonify(get_data())


@app.route("/state_data")
def state_data():
    return jsonify(get_state_data())


@app.route("/make_data")
def make_data():
    return jsonify(get_make_data())


@app.route("/color_data")
def color_data():
    return jsonify(get_color_data())


if __name__ == '__main__':
    app.run()
