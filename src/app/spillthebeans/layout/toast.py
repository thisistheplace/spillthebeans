import dash_bootstrap_components as dbc


def make_toast(
    id: str, children: object, header: str, open=True, icon="primary", duration=4000
):
    return dbc.Toast(
        id=id,
        children=children,
        header=header,
        is_open=open,
        dismissable=True,
        icon=icon,
        duration=duration,
        # top: 66 positions the toast below the navbar
        style={
            "position": "fixed",
            "top": 10,
            "right": 10,
            "width": 350,
            "zIndex": 1000,
        },
    )
