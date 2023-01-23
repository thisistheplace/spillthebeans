from dash import html, callback, Input, Output, MATCH, State, no_update
import dash_bootstrap_components as dbc
import uuid

from dash_wtgviewer import DashWtgviewer

from .ids import Ids
from ..layout.toast import make_toast

from spillthebeans.layout.socials import home


class WtgviewerAIO(html.Div):
    """Holder for full page layout"""

    # Make the ids class a public class
    ids = Ids

    # Define the arguments of the All-in-One component
    def __init__(
        self, model, map, aio_id: str | None = None, tooltip=True, sea=True, show_map=True
    ):
        """WtgviewAIO is an All-In-One component which holds a threejs rendering of a wind turbine"""

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        # Define the component's layout
        super().__init__(
            [  # Equivalent to `html.Div([...])`
                html.Div(
                    DashWtgviewer(
                        id=self.ids.wind(aio_id),
                        tooltip=tooltip,
                        sea=sea,
                        model=model,
                        map=map,
                        show_map=show_map
                    ),
                    style={
                        "width":"100vw",
                        "height":"100vh"
                    }
                ),
                make_toast(
                    "toast",
                    "click on a wind turbine location to view in 3D",
                    "hint",
                    icon="success"
                ),
                home(),
                html.Div(
                    children=[
                        html.H1("wind farm viewer"),
                        html.H4("React component to visualise wind turbine data"),
                    ],
                    style={
                        "zIndex": "30",
                        "left": "0px",
                        "bottom": "0px",
                        "margin": "20px",
                        "position": "absolute",
                        "display": "block",
                    },
                ),
                html.Div(
                    [
                        dbc.Switch(
                            id=self.ids.map_toggle(aio_id),
                            label="map",
                            value=True,
                        ),
                        dbc.Switch(
                            id=self.ids.env_toggle(aio_id),
                            label="environment",
                            value=True,
                        ),
                        dbc.Switch(
                            id=self.ids.tooltip_toggle(aio_id),
                            label="tooltip",
                            value=True,
                        )
                    ],
                    style={
                        "zIndex": "30",
                        "right": "0px",
                        "top": "0px",
                        "margin": "20px",
                        "position": "absolute",
                        "display": "block",
                    },
                )
            ],
            style={"height": "100vh", "width": "100vw"},
        )

    @callback(
        Output(ids.wind(MATCH), "tooltip"),
        Input(ids.tooltip_toggle(MATCH), "value"),
        prevent_initial_call=True,
    )
    def toggle_map(toggle):
        return toggle


    @callback(
        Output(ids.wind(MATCH), "sea"),
        Input(ids.env_toggle(MATCH), "value"),
        prevent_initial_call=True,
    )
    def toggle_map(toggle):
        return toggle

    @callback(
        Output(ids.wind(MATCH), "show_map"),
        Input(ids.map_toggle(MATCH), "value"),
        State(ids.wind(MATCH), "show_map"),
        prevent_initial_call=True,
    )
    def toggle_map(toggle, show_map):
        if show_map != toggle:
            return toggle
        else:
            return no_update

    @callback(
        Output(ids.map_toggle(MATCH), "value"),
        Input(ids.wind(MATCH), "show_map"),
        State(ids.map_toggle(MATCH), "value"),
        prevent_initial_call=True,
    )
    def monitor_map(show_map, toggle):
        if show_map != toggle:
            return show_map
        else:
            return no_update