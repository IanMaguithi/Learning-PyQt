import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Using LineEdits")
        self.UI()
    
    def UI(self):
        self.nameTextBox=QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Enter your name")
        self.nameTextBox.move(120, 50)
        self.passwordTextBox=QLineEdit(self)
        self.passwordTextBox.setPlaceholderText("Enter your password")
        self.passwordTextBox.move(120, 80)
        # hides the password
        self.passwordTextBox.setEchoMode(QLineEdit.Password)
        
        button = QPushButton("Save", self)
        button.move(160, 110)
        button.clicked.connect(self.getValues)
        self.show()
    
    def getValues(self):
        name = self.nameTextBox.text()
        password = self.passwordTextBox.text()
        self.setWindowTitle("Your name is: " + name + " and your password is: " + password)
        # print(name, password)
        # clear the text boxes
        self.nameTextBox.clear()
        self.passwordTextBox.clear()
        

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
        