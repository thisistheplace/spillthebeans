from dash import Output, Input, State, html, dcc, callback, MATCH, no_update
import dash_bootstrap_components as dbc

import asyncio
import uuid

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
        children: list | list = list,
        options: list[str] | None = None,
    ):
        """VtkMeshViewerAIO is an All-In-One component which visualizes VTK meshes

        Args:
            options: list of options to add to a dropdown
            generate_mesh: asyncronous callback to generate mesh from options string
        """
        if options is None:
            raise TypeError("options must not be None!")

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        # Define the component's layout
        super().__init__(
            children
            + [  # Equivalent to `html.Div([...])`
                dcc.Interval(
                    id=self.ids.interval(aio_id), interval=1000, max_intervals=0
                ),
                html.Div(
                    id=self.ids.vtkholder(aio_id),
                    children=[
                        dash_vtk.View(
                            id=self.ids.vtk(aio_id),
                            background=[
                                255,
                                255,
                                255,
                            ],  # RGB array of floating point values between 0 and 1.
                            # interactorSettings=[...], # Binding of mouse events to camera action (Rotate, Pan, Zoom...)
                            cameraPosition=[
                                0,
                                5,
                                0,
                            ],  # Where the camera should be initially placed in 3D world
                            cameraViewUp=[
                                0,
                                0,
                                1,
                            ],  # Vector to use as your view up for your initial camera
                            cameraParallelProjection=False,  # Should we see our 3D work with perspective or flat with no depth perception
                            triggerRender=0,  # Timestamp meant to trigger a render when different
                            triggerResetCamera=0,  # Timestamp meant to trigger a reset camera when different
                            # clickInfo,                    # Read-only property to retrieve picked representation id and picking information
                            # hoverInfo                     # Read-only property to retrieve picked representation id and picking information
                        ),
                    ],
                    style={"height": "100vh", "width": "100vw"},
                ),
            ],
            style={"height": "100vh", "width": "100vw"},
        )

    # Define this component's stateless pattern-matching callback
    # that will apply to every instance of this component.
    @callback(
        Output(ids.vtk(MATCH), "children"),
        Input(ids.jobcomplete(MATCH), "data"),
        State(ids.jsonstore(MATCH), "data"),
        prevent_initial_callback=True,
    )
    def _get_mesh(job: dict, json_str: str):
        return no_update