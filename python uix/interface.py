from PySide6.QtWidgets import QApplication, QPushButton

class Mainwindow(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("click me")
        self.resize(400,400)
        
app= QApplication()
win =Mainwindow()
win.show()
app.exec()