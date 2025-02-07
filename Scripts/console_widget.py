import PySide6.QtWidgets as qt
import PySide6.QtGui as qtgui 
import enum
import time

class LogType(enum.Enum):
    ACTION = 0
    WARNING = 1
    ERROR = 2

class QPConsoleWidget(qt.QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setMinimumHeight(100)
        
    
    def AddLog(self, log_text : str, log_type : LogType = LogType.ACTION):
        self.setText(self.toPlainText() + f"[{log_type.name}] - (" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + f") -: {log_text}\n")
        cursor = self.textCursor()
        cursor.movePosition(qtgui.QTextCursor.MoveOperation.End)
        self.setTextCursor(cursor)