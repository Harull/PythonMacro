import PySide6.QtWidgets as qt
import enum
import time
class LogType(enum.Enum):
    ACTION = 0
    WARNING = 1
    ERROR = 2

class ConsoleWidget(qt.QTextEdit):
    def __init__(self, text: str, parent: qt.QWidget | None= ...):
        super().__init__(text, parent)
    
    def AddLog(self, log_text : str, log_type : LogType):
        self.setText(self.toPlainText() + f"[{log_type.name}]-{time.gmtime(time.time())}: {log_text}")

    
