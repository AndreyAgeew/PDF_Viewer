from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PdfViewer(object):
    def setupUi(self, PdfViewer):
        PdfViewer.setObjectName("PdfViewer")
        PdfViewer.resize(700, 950)
        PdfViewer.setIconSize(QtCore.QSize(16, 16))

        self.centralwidget = QtWidgets.QWidget(PdfViewer)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 121, 650, 850))
        self.graphicsView.setObjectName("graphicsView")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 30, 241, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButtonPrev = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonPrev.setFont(QtGui.QFont())
        self.pushButtonPrev.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonPrev.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout.addWidget(self.pushButtonPrev)

        self.pushButtonNext = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonNext.setFont(QtGui.QFont())
        self.pushButtonNext.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonNext.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonNext.setAutoRepeatInterval(100)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout.addWidget(self.pushButtonNext)

        self.pushButtonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLoad.setGeometry(QtCore.QRect(40, 40, 101, 41))
        self.pushButtonLoad.setFont(QtGui.QFont())
        self.pushButtonLoad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonLoad.setObjectName("pushButtonLoad")

        PdfViewer.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(PdfViewer)
        self.statusbar.setObjectName("statusbar")
        PdfViewer.setStatusBar(self.statusbar)

        self.retranslateUi(PdfViewer)
        QtCore.QMetaObject.connectSlotsByName(PdfViewer)

    def retranslateUi(self, PdfViewer):
        _translate = QtCore.QCoreApplication.translate
        PdfViewer.setWindowTitle(_translate("PdfViewer", "PDF Viewer"))
        self.pushButtonPrev.setText(_translate("PdfViewer", "<"))
        self.pushButtonNext.setText(_translate("PdfViewer", ">"))
        self.pushButtonLoad.setText(_translate("PdfViewer", "Load"))
