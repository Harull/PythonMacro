import pynput
import key
import time
from console_widget import QPConsoleWidget, LogType
from PySide6.QtCore import QTimer

# A track will ideally be a sequence of input registered, in order to be played back by the script.
# Resulting in a macro
class Track:
    key_list = list()
    is_registering = False
    mouse_listener = None
    time_at_start = None
    timer_of_late_execution : QTimer = None

    def __init__(self):
        self.key_list = list()
        self.is_registering = False
        self.mouse_listener = pynput.mouse.Listener(lambda x,y : self.OnMouseMoved(x,y), lambda x, y, button, pressed: self.OnMouseClicked(x, y, button, pressed), lambda x, y, dx, dy : self.OnScroll(x, y, dx, dy))
        self.keyboard_listener = pynput.keyboard.Listener(lambda x : self.OnKeyboarKeyPressed(x), lambda x : self.OnKeyboarKeyReleased(x))
    
    def StartTracking(self, delay_in_seconds : int, console_widget : QPConsoleWidget):
        if self.timer_of_late_execution and self.timer_of_late_execution.isActive():
            console_widget.AddLog(f"Tracking already ready to start in [{self.timer_of_late_execution.remainingTime() / 1000}] seconds", LogType.WARNING)
            return
        if self.is_registering:
            console_widget.AddLog(f"You are already tracking, you cannot start the tracking, stop first then try again", LogType.WARNING)
            return
        if delay_in_seconds > 0:
            console_widget.AddLog(f"Start tracking in {delay_in_seconds} seconds")

        self.timer_of_late_execution = QTimer()
        self.timer_of_late_execution.timeout.connect(lambda : self.__StartTrackingThread(console_widget))
        self.timer_of_late_execution.setInterval(delay_in_seconds*1000)
        self.timer_of_late_execution.setSingleShot(True)
        self.timer_of_late_execution.start()
    
    def __StartTrackingThread(self, console_widget:QPConsoleWidget):
        self.time_at_start = time.time()
        self.mouse_listener.start()
        self.keyboard_listener.start()
        self.is_registering = True
        console_widget.AddLog("Tracking Started")

    def StopTracking(self, console_widget : QPConsoleWidget):
        if not( self.timer_of_late_execution and self.timer_of_late_execution.isActive()) and not self.is_registering:
            console_widget.AddLog(f"Tracking already stopped, start a tracking first before stopping it", LogType.WARNING)
            return
        
        log_text = "Tracking Stopped"
        if self.timer_of_late_execution and self.timer_of_late_execution.isActive():
            self.timer_of_late_execution.stop()
            log_text = "Tracking Canceled"
        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        self.is_registering = False
        console_widget.AddLog(log_text)

    def OnMouseClicked(self, x, y, button, pressed):
        self.key_list.append(key.Key(time.time()-self.time_at_start, (x, y, button, pressed), key.InputKeyType.MOUSE_CLICKED))

    def OnMouseMoved(self, x, y):
        self.key_list.append(key.Key(time.time()-self.time_at_start, (x, y), key.InputKeyType.MOUSE_MOVED))

    def OnScroll(self, x, y, dx, dy):
        self.key_list.append(key.Key(time.time()-self.time_at_start, (x, y, dx, dy), key.InputKeyType.MOUSE_SCROLLED))

    def OnKeyboarKeyPressed(self, key_pressed):
        self.key_list.append(key.Key(time.time()-self.time_at_start, (key_pressed,), key.InputKeyType.KEYBOARD_KEY_PRESSED))
    
    def OnKeyboarKeyReleased(self, key_released):
        self.key_list.append(key.Key(time.time()-self.time_at_start, (key_released,), key.InputKeyType.KEYBOARD_KEY_REALEASED))
        

