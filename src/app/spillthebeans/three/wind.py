from dash import html, callback, Input, Output, MATCH, State, no_update
import dash_bootstrap_components as dbc
import uuid
import json

from dash_wtgviewer import DashWtgviewer

from .ids import Ids
from ..layout.toast import make_toast

from spillthebeans.layout.socials import home, github

STYLE_VISIBLE = {'display': 'block'}
STYLE_HIDDEN = {'display': 'none'}
STYLE_MARGIN = {'margin': '10px'}

class WtgviewerAIO(html.Div):
    """Holder for full page layout"""

    # Make the ids class a public class
    ids = Ids

    # Define the arguments of the All-in-One component
    def __init__(
        self,
        model,
        map,
        aio_id: str | None = None,
        tooltip=True,
        environment=True,
        show_map=True,
        stats=False,
        results=False
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
                        environment=environment,
                        model=model,
                        map=map,
                        show_map=show_map,
                        stats=stats
                    ),
                    style={"width": "100vw", "height": "100vh"},
                ),
                make_toast(
                    self.ids.toast_wind(aio_id),
                    "click on a wind turbine location to view in 3D",
                    "hint",
                    icon="success",
                ),
                home(),
                html.Div(
                    children=[
                        html.H1("wind farm viewer"),
                        html.H4("Dash/React component to visualise wind turbine data"),
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
                dbc.Offcanvas(
                    [
                        dbc.InputGroup(
                            [
                                dbc.Input(id=self.ids.minimum(aio_id), placeholder="minimum", type="number", style=STYLE_MARGIN),
                                dbc.Input(id=self.ids.maximum(aio_id), placeholder="maximum", type="number", style=STYLE_MARGIN)
                            ]
                        ),
                        dbc.Button("set", id=self.ids.set_limits(aio_id), style=STYLE_MARGIN)
                    ],
                    id=self.ids.show_limits_input(aio_id),
                    class_name="colorscale-input",
                    is_open=False,
                    close_button=True,
                    backdrop=False,
                    title="Change colorscale limits:"
                ),
                html.Div(
                    [
                        github(
                            "https://github.com/thisistheplace/dash-wtgviewer",
                            style={
                                "margin":"10px",
                                "top": "0px",
                                "left": "0px"
                            }
                        ),
                        dbc.Switch(
                            id=self.ids.map_toggle(aio_id),
                            label="map",
                            value=show_map,
                        ),
                        dbc.Switch(
                            id=self.ids.env_toggle(aio_id),
                            label="environment",
                            value=environment,
                            style=STYLE_HIDDEN if show_map else STYLE_VISIBLE
                        ),
                        dbc.Switch(
                            id=self.ids.tooltip_toggle(aio_id),
                            label="tooltip",
                            value=tooltip,
                            style=STYLE_HIDDEN if show_map else STYLE_VISIBLE
                        ),
                        dbc.Switch(
                            id=self.ids.stats_toggle(aio_id),
                            label="stats",
                            value=stats,
                            style=STYLE_HIDDEN if show_map else STYLE_VISIBLE
                        ),
                        dbc.Switch(
                            id=self.ids.results_toggle(aio_id),
                            label="results",
                            value=results,
                            style=STYLE_HIDDEN if show_map else STYLE_VISIBLE
                        ),
                    ],
                    style={
                        "zIndex": "30",
                        "right": "0px",
                        "top": "0px",
                        "margin": "20px",
                        "position": "absolute",
                        "display": "block",
                    },
                ),
            ],
            style={"height": "100vh", "width": "100vw"},
        )

    @callback(
        Output(ids.wind(MATCH), "colorscale"),
        Output(ids.toast_wind(MATCH), "is_open"),
        Output(ids.toast_wind(MATCH), "children"),
        Output(ids.toast_wind(MATCH), "icon"),
        Input(ids.set_limits(MATCH), "n_clicks"),
        State(ids.minimum(MATCH), "value"),
        State(ids.maximum(MATCH), "value"),
        State(ids.wind(MATCH), "colorscale"),
        prevent_initial_call=True,
    )
    def set_min_max(n, min, max, current):
        if min is None or max is None:
            return no_update, True, "Please set both minimum and maximum values!", "danger"
        return {
            "visible": True,
            "limits": {
                "min": min,
                "max": max
            }
        }, no_update, no_update, no_update

    @callback(
        Output(ids.show_limits_input(MATCH), "is_open"),
        Input(ids.wind(MATCH), "colorscale_clicked"),
        prevent_initial_call=True,
    )
    def show_min_max(show_viewer):
        if show_viewer:
            return True
        return False

    @callback(
        Output(ids.wind(MATCH), "stats"),
        Input(ids.stats_toggle(MATCH), "value"),
        prevent_initial_call=True,
    )
    def toggle_stats(toggle):
        return toggle

    @callback(
        Output(ids.wind(MATCH), "results"),
        Input(ids.results_toggle(MATCH), "value"),
        prevent_initial_call=True,
    )
    def toggle_results(toggle):
        if toggle:
            return json.load(open("assets/models/ea1_results.json", "r"))
        else:
            return {}

    @callback(
        Output(ids.wind(MATCH), "tooltip"),
        Input(ids.tooltip_toggle(MATCH), "value"),
        prevent_initial_call=True,
    )
    def toggle_tooltip(toggle):
        return toggle

    @callback(
        Output(ids.wind(MATCH), "environment"),
        Input(ids.env_toggle(MATCH), "value"),
        prevent_initial_call=True,
    )
    def toggle_environment(toggle):
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
        Output(ids.env_toggle(MATCH), "style"),
        Output(ids.tooltip_toggle(MATCH), "style"),
        Output(ids.stats_toggle(MATCH), "style"),
        Output(ids.results_toggle(MATCH), "style"),
        Input(ids.wind(MATCH), "show_map"),
        State(ids.map_toggle(MATCH), "value"),
        prevent_initial_call=True,
    )
    def monitor_map(show_map, toggle):
        if show_map:
            show_toggles = [STYLE_HIDDEN] * 4
        else:
            show_toggles = [STYLE_VISIBLE] * 4

        if show_map != toggle:
            return [show_map] + show_toggles
        else:
            return [no_update] + show_toggles
