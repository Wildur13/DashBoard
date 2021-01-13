from PySide2 import QtWidgets, QtCore, QtWebEngineWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QtWidgets.QGridLayout(self)

        self.spin = QtWidgets.QSpinBox()
        self.spin.setValue(7)
        self.spin.setRange(1, 2000)
        self.spin.setStyleSheet("background-color: white")

        self.line = QtWidgets.QLineEdit()
        self.line.setText('USD')
        self.line.setStyleSheet("background-color: white")
        self.btn_refresh = QtWidgets.QPushButton("Refresh")
        self.btn_refresh.clicked.connect(self.refresh)
        self.btn_refresh.setStyleSheet("QPushButton:hover {color:white;"
                                       "background-color: green}")

        self.setStyleSheet("QWidget{background-color: #343a40}")

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.load(QtCore.QUrl("http://william13.pythonanywhere.com"))

        self.setWindowTitle("Dashboard - Currencies")
        QtWidgets.QShortcut(QtGui.QKeySequence('Enter'), self, self.refresh)
        self.btn_refresh.setFlat(True)

        self.main_layout.addWidget(self.spin, 1, 0, 1, 1)
        self.main_layout.addWidget(self.line, 1, 1, 1, 1)
        self.main_layout.addWidget(self.btn_refresh, 2, 0, 1, 2)
        self.main_layout.addWidget(self.view, 0, 0, 1, 2)

    def refresh(self):
        days = self.spin.value()
        currencies = self.line.text()
        self.view.load(QtCore.QUrl(f"http://william13.pythonanywhere.com/days={days}&currencies={currencies}"))


app = QtWidgets.QApplication([])
win = Window()
win.show()
app.exec_()

