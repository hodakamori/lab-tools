from dash import Dash, html
import dash_bootstrap_components as dbc
import dash
from .appcard import appcard

dash.register_page(__name__, path='/')

card = appcard(
    img_path="/static/images/profile.png",
    title="Excelへの画像埋め込み＆自動レイアウト",
    body="zipでまとめた画像をアップロードすると画像を自動でレイアウトしたexcelファイルを生成します。",
    href="/img-on-excel"
)

layout = html.Div(
    [
        dbc.Row([html.H3("Lab Tools")],
            justify="center",
            align="center",
            style={"margin-top": "50px", "margin-bottom": "50px", "margin-left":"100px", "margin-right":"100px"},
        ),
        dbc.Row([html.H6("Useful tools")],
            justify="center",
            align="center",
            className="text-muted",
            style={"margin-top": "50px", "margin-bottom": "50px", "margin-left":"100px", "margin-right":"100px"},
        ),
        dbc.Row(
            [
                dbc.Col(card, width=6),
            ],
            justify="center",
            align="center",
            style={"margin-top": "50px", "margin-bottom": "50px", "margin-left":"100px", "margin-right":"100px"},
        ),
    ]
)
