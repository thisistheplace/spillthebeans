from dash import html, dcc
import uuid

from pagenotfound_threejs import PagenotfoundThreejs

from .ids import Ids

from spillthebeans.layout.socials import home


class PagenotfoundThreejsAIO(html.Div):
    """Holder for full page layout"""

    # Make the ids class a public class
    ids = Ids

    # Define the arguments of the All-in-One component
    def __init__(self, aio_id: str | None = None, radius=500):
        """MoonAIO is an All-In-One component which holds a threejs rendering of a moon"""

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        # Define the component's layout
        super().__init__(
            [  # Equivalent to `html.Div([...])`
                PagenotfoundThreejs(id=aio_id),
                home(),
                html.Div(
                    children=[
                        html.H1("404 - page not found"),
                        html.Div(
                            children=[
                                html.Div("Model by", style={"display": "inline-block"}),
                                dcc.Link(
                                    "Tomas Lauhle",
                                    href="https://www.patreon.com/quaternius",
                                    style={
                                        "display": "inline-block",
                                        "margin-left": "5px",
                                    },
                                ),
                            ]
                        ),
                    ],
                    style={
                        "zIndex": "10",
                        "left": "0px",
                        "bottom": "0px",
                        "margin": "20px",
                        "position": "absolute",
                        "display": "block",
                    },
                ),
            ],
            style={"height": "100vh", "width": "100vw"},
        )
