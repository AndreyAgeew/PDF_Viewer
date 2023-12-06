import sys
from PyQt5 import QtWidgets

from src.pdf_app.pdf_viewer import PdfViewer

if __name__ == '__main__':
    # Создание экземпляра приложения Qt
    app = QtWidgets.QApplication(sys.argv)

    # Создание и отображение главного окна PdfViewer
    pdf_viewer = PdfViewer()
    pdf_viewer.show()

    # Запуск цикла обработки событий приложения
    sys.exit(app.exec_())