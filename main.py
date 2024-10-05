from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow # віджети
from ui import Ui_MainWindow # імпорт інтерфейсу
from PyQt6.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt6.QtCore import QUrl

class Widget(Ui_MainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.player = QMediaPlayer() # об'єкт для роботи з музикою

    def select_music(self):
        file, file1 = QFileDialog.getOpenFileName(self,
                                                  "Select audio",
                                                  "",
                                                  "Audio Files(*.mp3 *.wav)")
        if file:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))
            self.player.setVolume(50)
    def play_music(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
           self.player.play() 

app = QApplication([])
window = Widget()
window.show()
app.exec_()

 

      
