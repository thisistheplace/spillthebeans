from dash import html
import dash_bootstrap_components as dbc


def home():
    return html.Div(
        dbc.Button(
            html.I(className="fa-solid fa-home"),
            href="https://www.beancandesign.com",
            external_link=True,
            outline=True,
            size="lg",
            n_clicks=0,
        ),
        style={
            "zIndex": "10",
            "position": "absolute",
            "display": "block",
            "top": "0px",
            "left": "0px",
            "margin": "20px",
        },
    )


def mail():
    return html.Div(
        dbc.Button(
            html.I(className="fa-solid fa-envelope"),
            href="mailto:bean.can.design@gmail.com",
            external_link=True,
            outline=True,
            size="lg",
            n_clicks=0,
        ),
        style={
            "zIndex": "10",
            "position": "absolute",
            "display": "block",
            "bottom": "0px",
            "right": "0px",
            "margin": "20px",
        },
    )


def github(
    href="https://github.com/thisistheplace",
    style={
        "zIndex": "10",
        "position": "absolute",
        "display": "block",
        "top": "0px",
        "right": "0px",
        "margin": "20px",
    },
):
    return html.Div(
        dbc.Button(
            html.Img(
                src="/assets/GitHub-Mark-32px.png",
                style={"height": "32px", "width": "32px"},
            ),
            href=href,
            external_link=True,
            outline=True,
            size="lg",
            n_clicks=0,
        ),
        style=style,
    )
