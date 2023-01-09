import spillthebeans_threejs
from dash import Dash, callback, html, Input, Output
from pathlib import Path
import dash_bootstrap_components as dbc
from flask import Flask, make_response
from flask_restful import Resource, Api
import math


def read_wasm(fpath: str) -> bytes:
    resolved = Path(fpath).resolve()
    with open(resolved, "rb") as f:
        fbytes = f.read()
    return fbytes


class Can(Resource):
    def get(self):
        response = make_response(read_wasm("assets/can.glb"))
        response.headers["content-type"] = "application/text"
        return response


class Bean(Resource):
    def get(self):
        response = make_response(read_wasm("assets/bean.glb"))
        response.headers["content-type"] = "application/text"
        return response


server = Flask("my_app")
app = Dash(server=server, external_stylesheets=[dbc.themes.SIMPLEX])
api = Api(server)

api.add_resource(Can, "/assets/can.glb")
api.add_resource(Bean, "/assets/bean.glb")

app.layout = html.Div(
    [
        html.Div(id="input", children=["test"]),
        html.Canvas(id="canvas"),
        spillthebeans_threejs.SpillthebeansThreejs(
            id="test", rotation=0.01, maxAngle=math.pi / 1.5
        ),
    ],
    style={"width": "100%", "height": "100%"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
