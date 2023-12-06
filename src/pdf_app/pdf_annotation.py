import fitz
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene

from src.pdf_app.mouse_handler_anotation import PdfAnnotationMouseHandler


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
            self.scene = QGraphicsScene(self.ui.centralwidget)
            self.ui.graphicsView.setScene(self.scene)
            self.rect_item = None
            self.start_pos = None

            # Create an instance of PdfAnnotationMouseHandler
            self.graphics_manager = PdfAnnotationMouseHandler(self)

            # Connect events to graphicsView
            self.ui.graphicsView.mousePressEvent = self.graphics_manager.mousePressEvent
            self.ui.graphicsView.mouseMoveEvent = self.graphics_manager.mouseMoveEvent
            self.ui.graphicsView.mouseReleaseEvent = self.graphics_manager.mouseReleaseEvent

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

                # Add pixmap_item to the scene
                self.scene.addItem(pixmap_item)

                # Add rect_item to the scene if it exists
                if self.rect_item:
                    self.scene.addItem(self.rect_item)

    def previous_page(self):
        try:
            if self.current_page > 0 and self.pdf_document:
                self.current_page -= 1
                self.rect_item = None  # Clear rect_item when changing pages
                self.show_page()
        except Exception as e:
            print(f"Error in previous_page: {e}")

    def next_page(self):
        try:
            if self.current_page < self.pdf_document.page_count - 1 and self.pdf_document:
                self.current_page += 1
                self.rect_item = None  # Clear rect_item when changing pages
                self.show_page()
        except Exception as e:
            print(f"Error in next_page: {e}")
