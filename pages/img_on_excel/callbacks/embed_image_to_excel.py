import shutil
import os
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import dcc, callback
from ..api.core import EmbedImageToExcel

def enable_download():
    @callback(
        Output("embed-image-to-excel-dlbutton", "disabled"),
        Output("embed-image-to-excel-filename", "data"),
        Input("embed-image-to-excel-upload", "isCompleted"),
        Input("embed-image-to-excel-upload", "upload_id"),
        Input("embed-image-to-excel-upload", "fileNames"),
    )
    def func(isCompleted, upload_id, file_names):
        if isCompleted and upload_id is not None and file_names is not None:
            tmpdir = os.path.join("./workdir", upload_id)
            shutil.unpack_archive(os.path.join("./uploads/", upload_id, file_names[0]), tmpdir)
            oname = os.path.splitext(file_names[0])[0]+".xlsx"
            e = EmbedImageToExcel(homedir=tmpdir, outputname=os.path.join(tmpdir, oname))
            e.run()
            return False, oname
        else:
            return True, ""

def download_result():
    @callback(
        Output("download-file", "data"),
        Input("embed-image-to-excel-dlbutton", "n_clicks"),
        Input("embed-image-to-excel-upload", "upload_id"),
        State("embed-image-to-excel-filename", "data"),
        prevent_initial_call=True,
    )
    def func(n_clicks, upload_id, oname):
        tmpdir = os.path.join("./workdir", upload_id)
        if n_clicks > 0:
            return dcc.send_file(
                os.path.join(tmpdir, oname)
            )