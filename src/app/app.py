from dash import Dash, html
import dash_bootstrap_components as dbc
from flask import Flask
import os

from spillthebeans.layout.spillthebeans import SpillthebeansAIO
from spillthebeans.layout.aio.cardtypes import parse_cards
from spillthebeans.server.resources import add_assets
from spillthebeans.system.fileutils import read_yaml
from spillthebeans.constants import ASSETS_DIRECTORY, CARD_CONFIG

server = Flask('my_app')
app = Dash(server=server, external_stylesheets=[dbc.themes.FLATLY])

add_assets(server, [fname for fname in os.listdir(ASSETS_DIRECTORY) if not fname.startswith(".")])

cards = parse_cards(read_yaml(CARD_CONFIG))

app.layout = html.Div(
    SpillthebeansAIO(cards=cards),
    style={
        "width": "100vh",
        "height": "100vw"
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)