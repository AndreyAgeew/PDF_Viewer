import fitz
from PyQt5 import QtWidgets, QtGui

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene


class PdfAnnotation:
    def __init__(self, ui):
        self.ui = ui
        self.setup_annotation_ui()

    def setup_annotation_ui(self):
        try:
            self.ui.pushButtonLoad.clicked.connect(self.load_pdf)
            self.ui.pushButtonPrev.clicked.connect(self.previous_page)
            self.ui.pushButtonNext.clicked.connect(self.next_page)
            self.current_page = 0
            self.pdf_document = None
            self.webview = QWebEngineView(self.ui.centralwidget)
            self.webview.setGeometry(self.ui.graphicsView.geometry())
            self.webview.setVisible(False)

            self.scene = QGraphicsScene(self.ui.centralwidget)
            self.ui.graphicsView.setScene(self.scene)


        except Exception as e:
            print(f"Error in setup_annotation_ui: {e}")

    def load_pdf(self):
        try:
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self.ui.centralwidget, "Open PDF File", "",
                                                                 "PDF Files (*.pdf)")
            self.pdf_document = fitz.open(file_path)
            print(f"PDF loaded: {file_path}")
            self.current_page = 0
            self.show_page()
        except Exception as e:
            print(f"Error loading PDF: {e}")

    def show_page(self):
        if self.pdf_document is not None:
            if 0 <= self.current_page < len(self.pdf_document):
                page = self.pdf_document[self.current_page]

                image = page.get_pixmap()

                qimage = QtGui.QImage(image.samples, image.width, image.height, image.stride,
                                      QtGui.QImage.Format_RGB888)

                pixmap = QtGui.QPixmap.fromImage(qimage)

                pixmap_item = QGraphicsPixmapItem(pixmap)
                self.scene.clear()
                self.scene.addItem(pixmap_item)

    def previous_page(self):
        try:
            if self.current_page > 0 and self.pdf_document:
                self.current_page -= 1
                self.show_page()
        except Exception as e:
            print(f"Error in previous_page: {e}")

    def next_page(self):
        try:
            if self.current_page < self.pdf_document.page_count - 1 and self.pdf_document:
                self.current_page += 1
                self.show_page()
        except Exception as e:
            print(f"Error in next_page: {e}")
