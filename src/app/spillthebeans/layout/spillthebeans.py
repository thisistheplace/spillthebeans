from dash import Output, Input, html, callback, MATCH
import dash_bootstrap_components as dbc
import math
import uuid

from spillthebeans_threejs import SpillthebeansThreejs
from spillthebeans.layout.aio.cardtypes import Card
from spillthebeans.layout.aio.card import CardAIO

from .ids import Ids

class SpillthebeansAIO(html.Div):
    """Holder for full page layout"""

    # Make the ids class a public class
    ids = Ids

    # Define the arguments of the All-in-One component
    def __init__(
        self,
        aio_id: str | None = None,
        cards: list[Card] | None = None
    ):
        """SpillthebeansAIO is an All-In-One component which holds a threejs rendering and website cards

        Args:
            cards: list of 
            generate_mesh: asyncronous callback to generate mesh from options string
        """

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        # Define the component's layout
        super().__init__(
            [  # Equivalent to `html.Div([...])`
                html.Div(
                    SpillthebeansThreejs(
                        id=self.ids.three(aio_id),
                        canAngle=math.pi * -0.75,
                        scale=0.075
                    ),
                    style={
                        "zIndex": "5",
                        "position":"absolute",
                        "display":"block",
                        "height": "100%",
                        "width": "100%"
                    }
                ),
                html.Div(
                    dbc.Button(
                        html.Div(
                            html.I(
                                className="fa-solid fa-chevron-up"
                            ),
                            className="animate__flash"
                        ),
                        id=self.ids.sidebar_open(aio_id),
                        className="me-1",
                        outline=True,
                        size="lg",
                        n_clicks=0,
                    ),
                    style={
                        "zIndex": "10",
                        "position":"absolute",
                        "display":"block",
                        "bottom": "0px",
                        "margin": "20px",
                    }
                ),
                dbc.Tooltip(
                    "portfolio",
                    id="tooltip",
                    is_open=True,
                    target=self.ids.sidebar_open(aio_id),
                    placement="top",
                    fade=True,
                    delay={"show":5000}
                ),
                html.Div(
                    dbc.Button(
                        html.Img(
                            src="/assets/GitHub-Mark-32px.png",
                            style={
                                "height":"32px",
                                "width":"32px"
                            }
                        ),
                        href="https://github.com/thisistheplace",
                        external_link=True,
                        outline=True,
                        size="lg",
                        n_clicks=0,
                    ),
                    style={
                        "zIndex": "10",
                        "position":"absolute",
                        "display":"block",
                        "top": "0px",
                        "right": "0px",
                        "margin": "20px"
                    }
                ),
                html.Div(
                    dbc.Button(
                        html.I(
                            className="fa-solid fa-envelope"
                        ),
                        href="mailto:bean.can.design@gmail.com",
                        external_link=True,
                        outline=True,
                        size="lg",
                        n_clicks=0,
                    ),
                    style={
                        "zIndex": "10",
                        "position":"absolute",
                        "display":"block",
                        "top": "0px",
                        "left": "0px",
                        "margin": "20px"
                    }
                ),
                dbc.Offcanvas(
                    dbc.Container(
                        dbc.Row(
                            dbc.Col(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            CardAIO(card=card),
                                            width=12,
                                            sm=12,
                                            md=6,
                                            lg=4
                                        )
                                        for card in cards
                                    ],
                                    justify="left",
                                    align="left",
                                    style={
                                        "width":"100%",
                                        "flexFlow": "row",
                                        "overflowX": "scroll"
                                    }
                                ),
                                width=12,
                                sm=12,
                                md=10,
                                lg=12
                            ),
                            justify="center"
                        )
                    ),
                    id=self.ids.card_row(aio_id),
                    placement="bottom",
                    is_open=False,
                    backdrop=True,
                    close_button=False,
                    style={
                        "backgroundColor":"transparent",
                        "borderStyle":"none",
                        "height":"fit-content",
                        "maxHeight": "80vh",
                        "paddingBottom": "20px"
                    }
                ),
            ],
            style={"height": "100vh", "width": "100vw"},
        )

    @callback(
        Output(ids.card_row(MATCH), "is_open"),
        Input(ids.sidebar_open(MATCH), "n_clicks"),
        prevent_initial_call=True,
    )
    def toggle_collapse(n_open):
        return True