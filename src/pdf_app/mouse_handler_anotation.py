from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt



class PdfAnnotationMouseHandler:
    def __init__(self, pdf_annotation):
        self.pdf_annotation = pdf_annotation

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pdf_annotation.start_pos = self.pdf_annotation.ui.graphicsView.mapToScene(event.pos())

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.pdf_annotation.start_pos is not None:
            end_pos = self.pdf_annotation.ui.graphicsView.mapToScene(event.pos())
            self.update_rectangle(self.pdf_annotation.start_pos, end_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            end_pos = self.pdf_annotation.ui.graphicsView.mapToScene(event.pos())
            self.update_rectangle(self.pdf_annotation.start_pos, end_pos)

    def update_rectangle(self, start_pos, end_pos):
        try:
            # Remove existing rect_item if it exists
            if self.pdf_annotation.rect_item:
                self.pdf_annotation.scene.removeItem(self.pdf_annotation.rect_item)

            rect = QGraphicsRectItem(start_pos.x(), start_pos.y(), end_pos.x() - start_pos.x(),
                                     end_pos.y() - start_pos.y())
            rect.setPen(QPen(Qt.red))
            self.pdf_annotation.rect_item = rect

            # Show the updated page with the rectangle
            self.pdf_annotation.show_page()

        except Exception as e:
            print(f"Error in update_rectangle: {e}")