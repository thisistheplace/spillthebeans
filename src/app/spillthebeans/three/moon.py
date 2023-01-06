from dash import html
import uuid

from moon_threejs import MoonThreejs

from .ids import Ids


class MoonAIO(html.Div):
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
                MoonThreejs(id=str(uuid.uuid4()), radius=radius),
                html.Div(
                    children=[
                        html.H1("lonely moon"),
                        html.H4("gpu rendered fractal trees using threejs"),
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
