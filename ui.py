
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(366, 334)
        MainWindow.setStyleSheet("QWidget {\n"
"background-color: rgb(90,90,229);\n"
"}\n"
"\n"
"QPushButton {\n"
"    /*    назва : властивість ;   */\n"
"    background-color: orange; /* колір фону  */\n"
"    color: blue; /* колір тексту  */\n"
"    font-size: 24px; /* розмір тексту  */\n"
"    font-family: \"Courier New\"; /* шрифт тексту  */\n"
"    /* (товщина рамки)(тип лінії)(колір рамки)*/\n"
"    border: 4px solid black; /* створення рамки */\n"
"    border-radius: 30px; /* заокруглення рамки */\n"
"} \n"
"\n"
"QPushButton:hover {\n"
"    background-color: blue; /* колір фону  */\n"
"    color: orange; /* колір тексту  */\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(90, 10, 191, 71))
        self.play_button.setStyleSheet("")
        self.play_button.setObjectName("play_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(90, 90, 191, 71))
        self.stop_button.setStyleSheet("")
        self.stop_button.setObjectName("stop_button")
        self.select_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_button.setGeometry(QtCore.QRect(90, 170, 191, 71))
        self.select_button.setStyleSheet("")
        self.select_button.setObjectName("select_button")
        self.volume_slider = QtWidgets.QSlider(self.centralwidget)
        self.volume_slider.setGeometry(QtCore.QRect(100, 260, 160, 22))
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 366, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.play_button.setText(_translate("MainWindow", "Play/Pause"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.select_button.setText(_translate("MainWindow", "Select"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
