from openpyxl import Workbook
from openpyxl.drawing.image import Image
import glob
import numpy as np

class EmbedImageToExcel():

    """
    e = EmbedImageToExcel(outputname="../hello.xlsx")
    e.run()
    """

    def __init__(self, homedir="./", outputname="myworkbook.xlsx"):

        self.zoom = 40
        self.row_offset = 31
        self.column_offset = 11
        self.between_rows = 10
        self.homedir = homedir
        self.outputname = outputname

    def create_anchors(self, dir_index, num_images):

        anchors = []
        num_rows = np.floor(np.sqrt(num_images)).astype('int')
        num_cols = np.ceil(np.sqrt(num_images)).astype('int')
        for row in range(num_rows):
            for col in range(num_cols):
                anchors.append([1+row*self.row_offset+dir_index*(num_rows)*self.row_offset+dir_index*self.between_rows, 1+col*self.column_offset])
        return anchors
    
    def run(self):

        wb = Workbook()
        sheet = wb.active
        sheet.sheet_view.zoomScale = self.zoom
        sheet.sheet_view.zoomScaleNormal = self.zoom

        img_dirs = glob.glob(f"{self.homedir}/*/")
        for dir_index, img_dir in enumerate(img_dirs):
            img_files = glob.glob(f'{img_dir}/*.png')
            anchors = self.create_anchors(dir_index, len(img_files))
            for anc, img_file in zip(anchors, img_files):
                img = Image(img_file)
                sheet.add_image(img, sheet.cell(row=anc[0],column=anc[1]).coordinate)

        wb.save(self.outputname)