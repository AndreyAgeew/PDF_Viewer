from PyQt5 import QtWidgets

from pdf_app.pdf_annotation import PdfAnnotation
from pdf_app.pdf_viewer_ui import Ui_PdfViewer


class PdfViewer(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Инициализация главного окна приложения для просмотра PDF.

        Вызывает конструктор родительского класса, настраивает пользовательский интерфейс и создает экземпляр
        PdfAnnotation для добавления аннотаций на страницы PDF.

        """
        super(PdfViewer, self).__init__()

        # Инициализация пользовательского интерфейса
        self.ui = Ui_PdfViewer()
        self.ui.setupUi(self)

        # Создание экземпляра PdfAnnotation
        self.pdf_annotation = PdfAnnotation(self.ui)
