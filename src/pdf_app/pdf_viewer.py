from PyQt5 import QtWidgets


from src.pdf_app.pdf_annotation import PdfAnnotation
from src.pdf_app.pdf_viewer_ui import Ui_PdfViewer


class PdfViewer(QtWidgets.QMainWindow):
    def __init__(self):
        super(PdfViewer, self).__init__()
        self.ui = Ui_PdfViewer()
        self.ui.setupUi(self)

        # Create an instance of PdfAnnotation
        self.pdf_annotation = PdfAnnotation(self.ui)
