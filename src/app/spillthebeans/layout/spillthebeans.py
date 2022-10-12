from dash import Output, Input, State, html, dcc, callback, MATCH, no_update
import dash_bootstrap_components as dbc
import math
import uuid

from spillthebeans_threejs import SpillthebeansThreejs
from spillthebeans.layout.aio.cardtypes import Card
from spillthebeans.layout.aio.card import CardAIO

from .ids import Ids
from .toast import make_toast

LOADING_STYLE = {
    "position": "absolute",
    "zIndex": "10",
    "height": "100vh",
    "width": "100vw",
    "display": "none",
    "background": "white",
}


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
                SpillthebeansThreejs(
                    id=self.ids.three(aio_id),
                    rotation=0.,
                    maxAngle=math.pi / 0.75,
                    numBeans=2
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
                    placement="bottom",
                    is_open=True,
                    backdrop=True,
                    style={
                        "background-color":"transparent"
                    }
                ),
            ],
            style={"height": "100vh", "width": "100vw"},
        )