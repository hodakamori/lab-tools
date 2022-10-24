import dash_bootstrap_components as dbc
from dash import Dash, html

def appcard(img_path, title, body, href):
    card = dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src=img_path,
                            className="img-fluid rounded-start",
                            style={"max-height":"100%","width":"auto"}
                        ),
                        className="col-md-3",
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [
                                html.H5(title, className="card-title"),
                                html.P(
                                    body,
                                    className="card-text",
                                ),
                                dbc.Button("Use", color="primary", href=href),
                            ]
                        ),
                        className="col-md-9",
                    ),
                ],
                className="g-0 d-flex align-items-center",
            )
        ],
        # style={"maxWidth":"200px"}
    )
    return card
