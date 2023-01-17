from dash import html
import uuid

from dash_wtgviewer import DashWtgviewer

from .ids import Ids

from spillthebeans.layout.socials import home


class WtgviewerAIO(html.Div):
    """Holder for full page layout"""

    # Make the ids class a public class
    ids = Ids

    # Define the arguments of the All-in-One component
    def __init__(
        self, model, aio_id: str | None = None, tooltip=False,sea=True
    ):
        """WtgviewAIO is an All-In-One component which holds a threejs rendering of a wind turbine"""

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        # Define the component's layout
        super().__init__(
            [  # Equivalent to `html.Div([...])`
                html.Div(
                    DashWtgviewer(
                        id=aio_id,
                        tooltip=tooltip,
                        sea=sea,
                        model=model
                    ),
                    style={
                        "width":"100vw",
                        "height":"100vh"
                    }
                ),
                home(),
                html.Div(
                    children=[
                        html.H1("wind farm viewer"),
                        html.H4("React component to visualise wind turbine data"),
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
