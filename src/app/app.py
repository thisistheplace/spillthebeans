from dash import Dash, html
import dash_bootstrap_components as dbc
from flask import Flask
import os

from spillthebeans.layout.spillthebeans import SpillthebeansAIO
from spillthebeans.server.resources import add_assets
from spillthebeans.constants import ASSETS_DIRECTORY

server = Flask('my_app')
app = Dash(server=server, external_stylesheets=[dbc.themes.SIMPLEX])

add_assets(server, [fname for fname in os.listdir(ASSETS_DIRECTORY) if not fname.startswith(".")])

app.layout = html.Div(
    SpillthebeansAIO(),
    style={
        "width": "100vh",
        "height": "100vw"
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)