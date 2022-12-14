from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import dash_uploader as du
import dash

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
appinfo = dash.page_registry.values()

du.configure_upload(app, "./uploads")

app.layout = html.Div([
	dash.page_container
])

app.run_server(host="0.0.0.0", port=8050, debug=True)
