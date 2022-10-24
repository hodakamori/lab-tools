from dash import Dash, html
import dash_bootstrap_components as dbc
import dash
from .components.input.input import input
from .components.output.output import output
from .callbacks.embed_image_to_excel import enable_download, download_result

dash.register_page(__name__, path='/img-on-excel')

layout = html.Div(
    [
        dbc.Row(
            dbc.Col(input, width=6),
            justify="center",
            align="center",
            style={"margin-top": "100px", "margin-bottom": "100px"},
        ),
        dbc.Row(
            [
                dbc.Col(output, width=6)
            ],
            justify="center",
            align="center",
            style={"margin-top": "100px", "margin-bottom": "100px"},
        ),
    ]
)

enable_download()
download_result()
