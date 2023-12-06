import os
import sys

from PyQt5 import QtWidgets

from pdf_app.pdf_viewer import PdfViewer

# Получаем путь к текущей директории
current_dir = os.path.dirname(os.path.realpath(__file__))

# Добавляем корневую директорию проекта в sys.path
sys.path.insert(0, os.path.join(current_dir, '..'))

if __name__ == "__main__":
    # Создание экземпляра приложения Qt
    app = QtWidgets.QApplication(sys.argv)

    # Создание и отображение главного окна PdfViewer
    pdf_viewer = PdfViewer()
    pdf_viewer.show()

    # Запуск цикла обработки событий приложения
    sys.exit(app.exec_())
