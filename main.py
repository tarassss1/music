from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.player = QMediaPlayer()
        self.ui.select_button.clicked.connect(self.select_music)
        self.ui.play_button.clicked.connect(self.play_music)
        self.ui.stop_button.clicked.connect(self.stop_music)

    def select_music(self):
        file, n = QFileDialog.getOpenFileName(self, "Select audio", "", 
                                              "Audio Files(*.mp3 *.wav)")
        if file:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))
            self.player.setVolume(50) # встановлення гучності
    
    def play_music(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def stop_music(self):
        self.player.stop()    
    
        


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()


