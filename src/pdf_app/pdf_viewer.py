from PyQt5 import QtWidgets

from src.pdf_app.mouse_handler_anotation import PdfAnnotationMouseHandler
from src.pdf_app.pdf_annotation import PdfAnnotation
from src.pdf_app.pdf_viewer_ui import Ui_PdfViewer


class PdfViewer(QtWidgets.QMainWindow):
    def __init__(self):
        super(PdfViewer, self).__init__()
        self.ui = Ui_PdfViewer()
        self.ui.setupUi(self)

        # экземпляр PdfAnnotationMouseHandler
        self.annotation_handler = PdfAnnotationMouseHandler()
        self.annotation_handler.scene = self.ui.scene
        self.annotation_handler.graphicsView = self.ui.graphicsView
        self.annotation_handler.rect_item = None

        # бработчики событий мыши
        self.ui.graphicsView.mousePressEvent = self.annotation_handler.mousePressEvent
        self.ui.graphicsView.mouseReleaseEvent = self.annotation_handler.mouseReleaseEvent

        self.pdf_annotation = PdfAnnotation(self.ui)
