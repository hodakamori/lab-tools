import dash_bootstrap_components as dbc
from dash import html, dcc

output =  [
    dcc.Store(id="embed-image-to-excel-filename"),
    dbc.Button(
        "ダウンロード",
        color="success",
        disabled=True,
        id="embed-image-to-excel-dlbutton",
        className="d-grid gap-2 col-12 mx-auto",
        n_clicks=0
        ),
    dcc.Download(id="download-file")
    ]
