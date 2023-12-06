import sys
from PyQt5 import QtWidgets

from src.pdf_app.pdf_viewer import PdfViewer

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    pdf_viewer = PdfViewer()
    pdf_viewer.show()
    sys.exit(app.exec_())
