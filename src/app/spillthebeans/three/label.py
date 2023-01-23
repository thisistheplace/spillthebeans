from dash import html
import uuid

from .ids import Ids

from spillthebeans.layout.socials import home


class LabelAIO(html.Div):
    """Holder for full page layout"""

    # Make the ids class a public class
    ids = Ids

    # Define the arguments of the All-in-One component
    def __init__(self, aio_id: str | None = None):
        """LabelAIO is an All-In-One component which holds a threejs rendering of a BeanCanDesign can label"""

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        # Define the component's layout
        super().__init__(
            [  # Equivalent to `html.Div([...])`
                html.Div(
                    children=[
                        html.Header("bean can"),
                        html.Header("design"),
                    ],
                    style={
                        "fontSize": "150px",
                        "zIndex": "10",
                        "left": "0px",
                        "bottom": "0px",
                        "margin": "200px",
                        "position": "absolute",
                        "display": "block",
                        "transform": "rotate(-90deg)",
                    },
                ),
            ],
            style={"height": "100vh", "width": "100vw"},
        )
