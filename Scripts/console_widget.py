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
        
    
    def AddLog(self, log_text : str, log_type : LogType = LogType.ACTION):
        self.setText(self.toPlainText() + f"[{log_type.name}] - (" + time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) + f") -: {log_text}\n")

    
