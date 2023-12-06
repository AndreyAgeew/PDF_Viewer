from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PdfViewer(object):
    def setupUi(self, PdfViewer):
        """
        Настройка пользовательского интерфейса для PdfViewer.

        :param PdfViewer: Экземпляр PdfViewer
        """
        PdfViewer.setObjectName("PdfViewer")
        PdfViewer.resize(700, 950)
        PdfViewer.setIconSize(QtCore.QSize(16, 16))

        self.centralwidget = QtWidgets.QWidget(PdfViewer)
        self.centralwidget.setObjectName("centralwidget")

        # Графическое представление PDF-страницы
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 121, 650, 850))
        self.graphicsView.setObjectName("graphicsView")

        # Горизонтальный слой с кнопками
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 30, 241, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Кнопка для перехода на предыдущую страницу
        self.pushButtonPrev = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonPrev.setFont(QtGui.QFont())
        self.pushButtonPrev.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonPrev.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout.addWidget(self.pushButtonPrev)

        # Кнопка для перехода на следующую страницу
        self.pushButtonNext = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonNext.setFont(QtGui.QFont())
        self.pushButtonNext.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonNext.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonNext.setAutoRepeatInterval(100)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout.addWidget(self.pushButtonNext)

        # Кнопка для загрузки PDF-файла
        self.pushButtonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLoad.setGeometry(QtCore.QRect(40, 40, 101, 41))
        self.pushButtonLoad.setFont(QtGui.QFont())
        self.pushButtonLoad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonLoad.setObjectName("pushButtonLoad")

        # Установка центрального виджета в PdfViewer
        PdfViewer.setCentralWidget(self.centralwidget)

        # Статусбар
        self.statusbar = QtWidgets.QStatusBar(PdfViewer)
        self.statusbar.setObjectName("statusbar")
        PdfViewer.setStatusBar(self.statusbar)

        # Перевод текстовых элементов
        self.retranslateUi(PdfViewer)
        QtCore.QMetaObject.connectSlotsByName(PdfViewer)

    def retranslateUi(self, PdfViewer):
        """
        Перевод текстовых элементов интерфейса.

        :param PdfViewer: Экземпляр PdfViewer
        """
        _translate = QtCore.QCoreApplication.translate
        PdfViewer.setWindowTitle(_translate("PdfViewer", "PDF Viewer"))
        self.pushButtonPrev.setText(_translate("PdfViewer", "<"))
        self.pushButtonNext.setText(_translate("PdfViewer", ">"))
        self.pushButtonLoad.setText(_translate("PdfViewer", "Загрузка"))
