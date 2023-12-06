import fitz
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene

from pdf_app.mouse_handler_anotation import PdfAnnotationMouseHandler


class PdfAnnotation:
    def __init__(self, ui):
        """
        Инициализация объекта PdfAnnotation.

        :param ui: Объект пользовательского интерфейса
        """
        self.ui = ui
        self.setup_annotation_ui()

    def setup_annotation_ui(self):
        """
        Настройка элементов пользовательского интерфейса для аннотаций PDF.
        """
        try:
            # Подключение кнопок к соответствующим методам
            self.ui.pushButtonLoad.clicked.connect(self.load_pdf)
            self.ui.pushButtonPrev.clicked.connect(self.previous_page)
            self.ui.pushButtonNext.clicked.connect(self.next_page)

            # Инициализация переменных
            self.current_page = 0
            self.pdf_document = None
            self.scene = QGraphicsScene(self.ui.centralwidget)
            self.ui.graphicsView.setScene(self.scene)
            self.rect_item = None
            self.start_pos = None

            # Создание экземпляра PdfAnnotationMouseHandler
            self.graphics_manager = PdfAnnotationMouseHandler(self)

            # Подключение событий мыши к graphicsView
            self.ui.graphicsView.mousePressEvent = self.graphics_manager.mousePressEvent
            self.ui.graphicsView.mouseMoveEvent = self.graphics_manager.mouseMoveEvent
            self.ui.graphicsView.mouseReleaseEvent = (
                self.graphics_manager.mouseReleaseEvent
            )

        except Exception as e:
            print(f"Error in setup_annotation_ui: {e}")

    def load_pdf(self):
        """
        Загрузка PDF-файла и отображение первой страницы.
        """
        try:
            # Выбор файла PDF
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                self.ui.centralwidget, "Open PDF File", "", "PDF Files (*.pdf)"
            )
            self.pdf_document = fitz.open(file_path)
            print(f"PDF loaded: {file_path}")
            self.current_page = 0
            self.show_page()
        except Exception as e:
            print(f"Error loading PDF: {e}")

    def show_page(self):
        """
        Отображение текущей страницы PDF в graphicsView.
        """
        if self.pdf_document is not None:
            if 0 <= self.current_page < len(self.pdf_document):
                page = self.pdf_document[self.current_page]

                # Получение изображения страницы
                image = page.get_pixmap()

                # Преобразование в объект QImage
                qimage = QtGui.QImage(
                    image.samples,
                    image.width,
                    image.height,
                    image.stride,
                    QtGui.QImage.Format_RGB888,
                )

                pixmap = QtGui.QPixmap.fromImage(qimage)

                pixmap_item = QGraphicsPixmapItem(pixmap)
                self.scene.clear()

                # Добавление pixmap_item на сцену
                self.scene.addItem(pixmap_item)

                # Добавление rect_item на сцену, если существует
                if self.rect_item:
                    self.scene.addItem(self.rect_item)

    def previous_page(self):
        """
        Переход на предыдущую страницу PDF и отображение её.
        """
        try:
            if self.current_page > 0 and self.pdf_document:
                self.current_page -= 1
                self.rect_item = None  # Очистка rect_item при смене страницы
                self.show_page()
        except Exception as e:
            print(f"Error in previous_page: {e}")

    def next_page(self):
        """
        Переход на следующую страницу PDF и отображение её.
        """
        try:
            if (
                    self.current_page < self.pdf_document.page_count - 1
                    and self.pdf_document
            ):
                self.current_page += 1
                self.rect_item = None  # Очистка rect_item при смене страницы
                self.show_page()
        except Exception as e:
            print(f"Error in next_page: {e}")
