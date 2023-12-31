from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QGraphicsRectItem


class PdfAnnotationMouseHandler:
    def __init__(self, pdf_annotation):
        """
        Инициализация обработчика мыши для аннотаций PDF.

        :param pdf_annotation: Экземпляр PdfAnnotation, к которому привязан обработчик мыши.
        """
        self.pdf_annotation = pdf_annotation

    def mousePressEvent(self, event):
        """
        Обработка события нажатия кнопки мыши.

        :param event: Событие мыши
        """
        if event.button() == Qt.LeftButton:
            self.pdf_annotation.start_pos = (
                self.pdf_annotation.ui.graphicsView.mapToScene(event.pos())
            )

    def mouseMoveEvent(self, event):
        """
        Обработка события перемещения мыши.

        :param event: Событие мыши
        """
        if (
            event.buttons() == Qt.LeftButton
            and self.pdf_annotation.start_pos is not None
        ):
            end_pos = self.pdf_annotation.ui.graphicsView.mapToScene(event.pos())
            self.update_rectangle(self.pdf_annotation.start_pos, end_pos)

    def mouseReleaseEvent(self, event):
        """
        Обработка события отпускания кнопки мыши.

        :param event: Событие мыши
        """
        if event.button() == Qt.LeftButton:
            end_pos = self.pdf_annotation.ui.graphicsView.mapToScene(event.pos())
            self.update_rectangle(self.pdf_annotation.start_pos, end_pos)

    def update_rectangle(self, start_pos, end_pos):
        """
        Обновление прямоугольника на сцене.

        :param start_pos: Начальная позиция прямоугольника
        :param end_pos: Конечная позиция прямоугольника
        """
        try:
            # Удаление существующего rect_item, если он существует
            if self.pdf_annotation.rect_item:
                self.pdf_annotation.scene.removeItem(self.pdf_annotation.rect_item)

            # Создание нового прямоугольника
            rect = QGraphicsRectItem(
                start_pos.x(),
                start_pos.y(),
                end_pos.x() - start_pos.x(),
                end_pos.y() - start_pos.y(),
            )
            rect.setPen(QPen(Qt.red))
            self.pdf_annotation.rect_item = rect

            # Показ обновленной страницы с прямоугольником
            self.pdf_annotation.show_page()

        except Exception as e:
            print(f"Error in update_rectangle: {e}")
