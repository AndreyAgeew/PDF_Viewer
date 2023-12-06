from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QObject, QEvent
from PyQt5.QtWidgets import QGraphicsPathItem


class PdfAnnotationMouseHandler(QObject):
    def __init__(self):
        super().__init__()
        self.rect_item = None
        self.start_pos = None
        self.scene = None
        self.graphicsView = None

    def eventFilter(self, obj, event):
        try:
            if obj == self.graphicsView and event.type() == QEvent.MouseButtonPress:
                self.mousePressEvent(event)
            elif obj == self.graphicsView and event.type() == QEvent.MouseButtonRelease:
                self.mouseReleaseEvent(event)
            return super().eventFilter(obj, event)
        except Exception as e:
            print(f"Error in eventFilter: {e}")

    def mousePressEvent(self, event):
        try:
            if event.button() == Qt.LeftButton:
                self.start_pos = self.graphicsView.mapFromGlobal(event.globalPos())
        except Exception as e:
            print(f"Error in mousePressEvent: {e}")

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            end_pos = self.graphicsView.mapFromGlobal(event.globalPos())
            print(f"Draw rectangle called\nStart Pos: {self.start_pos}, End Pos: {end_pos}")
            self.draw_rectangle(self.start_pos, end_pos)

    def draw_rectangle(self, start_pos, end_pos):
        try:
            if self.rect_item:
                self.scene.removeItem(self.rect_item)

            # Convert start_pos and end_pos to scene coordinates
            start_pos_scene = self.graphicsView.mapToScene(start_pos)
            end_pos_scene = self.graphicsView.mapToScene(end_pos)

            # Create a rectangle in scene coordinates
            rect = QtCore.QRectF(start_pos_scene, end_pos_scene)

            # Create a rectangle item with the specified rect
            rect_item = QGraphicsPathItem()
            rect_item.setPen(QtGui.QPen(Qt.red))
            rect_item.setBrush(QtGui.QBrush(Qt.red, Qt.SolidPattern))

            # Create a QPainterPath and add a rectangle to it
            path = QtGui.QPainterPath()
            path.addRect(rect)

            rect_item.setPath(path)
            self.rect_item = rect_item
            self.scene.addItem(rect_item)
            self.graphicsView.viewport().update()
            # Print a message to ensure the method is called
            print("Rectangle added to the scene.")

        except Exception as e:
            print(f"Error in draw_rectangle: {e}")
