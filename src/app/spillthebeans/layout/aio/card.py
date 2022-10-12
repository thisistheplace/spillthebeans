from dash import Output, Input, State, html, dcc, callback, MATCH, no_update
import dash_bootstrap_components as dbc
import uuid

from .cardtypes import Card

from ..ids import Ids
from ..toast import make_toast

LOADING_STYLE = {
    "position": "absolute",
    "zIndex": "10",
    "height": "100vh",
    "width": "100vw",
    "display": "none",
    "background": "white",
}

class CardAIO(html.Div):
    """Class to hold individual panels """

    # Make the ids class a public class
    ids = Ids

    # Define the arguments of the All-in-One component
    def __init__(
        self,
        aio_id: str | None = None,
        card: Card | None = None
    ):
        """CardAIO is an All-In-One component which lays out a Card type

        Args:
            card: Card type object
        """
        if aio_id is None:
            aio_id = str(uuid.uuid4())
        
        if card is None:
            raise ValueError("Attribute 'card' must not be None")

        # Define the component's layout
        super().__init__(
            [  # Equivalent to `html.Div([...])`
                self._parse_card(card)
            ],
        )

    @staticmethod
    def _parse_card(card: Card):
        return dbc.Card(
            [
                dbc.CardImg(src=card.image, top=True),
                dbc.CardBody(
                    [
                        html.H4(card.title, className="card-title"),
                        html.P(
                            card.description,
                            className="card-text",
                        ),
                        dbc.Button(     
                            "Take me there...",       
                            href=card.url,
                            external_link=True,
                            color="primary"
                        )
                    ]
                ),
            ],
            style={"width": "18rem"},
        )