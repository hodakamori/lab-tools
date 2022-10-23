import dash_bootstrap_components as dbc
from dash import html

import dash_uploader as du

input =  [
    html.H5(
        "Excelにまとめたい画像をzipでアップロードしてください",
        style={"margin-bottom":"30px", "text-align":"center", "border-bottom":"3px solid #f6ba33", "font-weight":"bold"},
        ),
    du.Upload(
        id="embed-image-to-excel-upload",
        filetypes=['zip'],
        )
    ]
