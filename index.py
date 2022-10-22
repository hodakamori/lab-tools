from src.app.app import create_app

app = create_app()
app.run_server(host="0.0.0.0", port=8050, debug=True)