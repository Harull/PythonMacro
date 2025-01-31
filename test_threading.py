import PySide6.QtWidgets as qt
from PySide6.QtCore import QThread, QTimer

app = qt.QApplication() 


text_edit = qt.QTextEdit()

def Foo(text_edit : qt.QTextEdit):
    print("hello world")
    text_edit.setText("test")

qthread = QThread()
qthread.connect
timer = QTimer()
timer.timeout.connect(lambda : Foo(text_edit))
timer.setInterval(1000)
timer.setSingleShot(True)
timer.start()

window = qt.QMainWindow()
window.show()

app.exec()