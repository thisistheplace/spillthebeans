import dash_bootstrap_components as dbc


def make_toast(id: str, header: str):
    return dbc.Toast(
        id=id,
        header=header,
        is_open=False,
        dismissable=True,
        icon="danger",
        # duration=6000,
        # top: 66 positions the toast below the navbar
        style={
            "position": "fixed",
            "top": 66,
            "right": 10,
            "width": 350,
            "zIndex": 1000,
        },
    )
