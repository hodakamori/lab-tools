from dash import Dash, html
import dash_bootstrap_components as dbc
import dash_uploader as du

from .components.input.input import input
from .components.output.output import output
from .callbacks.embed_image_to_excel import enable_download, download_result

def create_app():

    app = Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX, dbc.icons.FONT_AWESOME])
    du.configure_upload(app, "./uploads")
    app.layout = html.Div(
        [
            dbc.Row(
                dbc.Col(input, width=4),
                justify="center",
                align="center",
                style={"margin-top": "100px", "margin-bottom": "100px"},
            ),
            dbc.Row(
                [
                    dbc.Col(output, width=4)
                ],
                justify="center",
                align="center",
                style={"margin-top": "100px", "margin-bottom": "100px"},
            ),
        ]
    )

    enable_download(app)
    download_result(app)
    return app