from dash import html
import uuid

from forest_threejs import ForestThreejs

from .ids import Ids

from spillthebeans.layout.socials import home


class ForestAIO(html.Div):
    """Holder for full page layout"""

    # Make the ids class a public class
    ids = Ids

    # Define the arguments of the All-in-One component
    def __init__(
        self,
        aio_id: str | None = None,
        totalX: int | None = None,
        totalZ: int | None = None,
        spacing: int | None = None,
        stats: bool = True,
    ):
        """ForestAIO is an All-In-One component which holds a threejs rendering of a Forest"""

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        # Define the component's layout
        super().__init__(
            [  # Equivalent to `html.Div([...])`
                ForestThreejs(
                    id="aio_id",
                    totalX=totalX,
                    totalZ=totalZ,
                    spacing=spacing,
                    stats=stats,
                ),
                home(),
                html.Div(
                    children=[
                        html.H1("forest growth"),
                        html.H4(
                            "tree instancedmeshes positioned on landscape using raycasting"
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
