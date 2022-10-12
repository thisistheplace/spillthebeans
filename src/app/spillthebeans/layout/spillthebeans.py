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
                        rotation=0.,
                        maxAngle=math.pi / 0.75,
                        numBeans=2
                    ),
                    style={
                        "zIndex": "5",
                        "position":"absolute",
                        "display":"block",
                        "height": "100%",
                        "width": "100%"
                    }
                ),
                dbc.Button(
                    html.I(className="fa-solid fa-chevron-up"),
                    id=self.ids.sidebar_open(aio_id),
                    className="me-1 blinkingicon",
                    outline=True,
                    size="lg",
                    n_clicks=0,
                    style={
                        "zIndex": "10",
                        "position":"absolute",
                        "display":"block",
                        "bottom": "0px",
                        "margin": "20px",
                        "animation": "blink 2s ease-in infinite"
                        # "background-color":"transparent"
                    }
                ),
                dbc.Offcanvas(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    CardAIO(card=card)
                                )
                                for card in cards
                            ],
                            style={
                                "width":"100%"
                            }
                        )
                    ],
                    id=self.ids.card_row(aio_id),
                    placement="bottom",
                    is_open=False,
                    backdrop=True,
                    style={
                        "background-color":"transparent"
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