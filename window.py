import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 550, 250)
        self.setWindowTitle("Window Title")
        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
