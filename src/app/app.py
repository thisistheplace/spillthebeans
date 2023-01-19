from dash import Dash, html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc
from flask import Flask
import json
import os

from spillthebeans.layout.spillthebeans import SpillthebeansAIO
from spillthebeans.layout.aio.cardtypes import parse_cards
from spillthebeans.server.resources import add_assets
from spillthebeans.system.fileutils import read_yaml
from spillthebeans.constants import ASSETS_DIRECTORY, CARD_CONFIG
from spillthebeans.three.moon import MoonAIO
from spillthebeans.three.forest import ForestAIO
from spillthebeans.three.label import LabelAIO
from spillthebeans.three.wind import WtgviewerAIO
from spillthebeans.three.pagenotfound import PagenotfoundThreejsAIO


server = Flask("spillthebeans-server")
add_assets(
    server,
    [fname for fname in os.listdir(ASSETS_DIRECTORY) if not fname.startswith(".")],
)

# external CSS stylesheets for Leaflet.js
leaflet_external_stylesheets = [
    {
        'href': 'https://unpkg.com/leaflet@1.9.2/dist/leaflet.css',
        'rel': 'stylesheet',
        'integrity': 'sha256-sA+zWATbFveLLNqWO2gtiw3HL/lh1giY/Inf1BJ0z14=',
        'crossorigin': ''
    },
    {
        'href': 'https://unpkg.com/leaflet@1.9.2/dist/leaflet.js',
        'rel': 'stylesheet',
        'integrity': 'sha256-o9N1jGDZrf5tS+Ft4gbIK7mYMipq9lqpVJ91xHSyKhg=',
        'crossorigin': ''
    }
]

app = Dash(
    server=server,
    external_stylesheets=[
        dbc.themes.FLATLY,
        dbc.icons.FONT_AWESOME,
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    ] + leaflet_external_stylesheets,
    title="spillthebeans",
    use_pages=False,  # there seems to be multiple bugs in Dash which prevent pages from working
)

cards = parse_cards(read_yaml(CARD_CONFIG))

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/":
        return SpillthebeansAIO(cards=cards)
    elif pathname == "/moon":
        return MoonAIO(ntrees=2000, nforests=4)
    elif pathname == "/forest":
        return ForestAIO(totalX=125, totalZ=125, spacing=20, stats=False)
    elif pathname == "/label":
        return LabelAIO()
    elif pathname == "/wind":
        return WtgviewerAIO(
            model=json.load(open("assets/models/windturbine.json", "r")),
            map={
                "center":{"id":"center", "lat":52.29733, "lng":2.35038},
                "turbines":{"positions":json.load(open("assets/models/ea1_turbines.json", "r"))},
                "boundary":{"positions":json.load(open("assets/models/ea1_boundary.json", "r"))}
            }
        )
    else:
        return PagenotfoundThreejsAIO()


if __name__ == "__main__":
    app.run_server(debug=False)
