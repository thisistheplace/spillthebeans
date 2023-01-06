from dash import html, callback, MATCH, Input, Output, no_update
import dash_bootstrap_components as dbc
import uuid

from .cardtypes import Card

from ..ids import Ids


class CardAIO(html.Div):
    """Class to hold individual panels"""

    # Make the ids class a public class
    ids = Ids

    # Define the arguments of the All-in-One component
    def __init__(self, aio_id: str | None = None, card: Card | None = None):
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
                self._parse_card(self.ids.card(aio_id), card),
                dbc.Popover(
                    id=self.ids.popover(aio_id),
                    target=self.ids.card(aio_id),
                    body=False,
                    trigger="hover",
                    hide_arrow=True,
                ),
            ]
        )

    @staticmethod
    def _parse_card(id, card: Card):
        return dbc.Card(
            [
                dbc.CardHeader(card.title),
                dbc.CardImg(src=card.image, top=True),
                dbc.CardBody(
                    [
                        html.P(
                            card.description,
                            className="card-text",
                        ),
                        dbc.Button(
                            card.button,
                            href=card.url,
                            external_link=True,
                            color="primary",
                        ),
                    ]
                ),
            ],
            id=id,
        )

    @callback(
        Output(ids.card(MATCH), "style"),
        Input(ids.popover(MATCH), "is_open"),
        prevent_initial_call=True,
    )
    def mouseover_card(is_open):
        if is_open:
            return {"border": "1px solid rgba(0,0,0)"}
        else:
            return {"border": "1px solid rgba(0,0,0,.125)"}
