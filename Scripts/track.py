import pynput
import key
import time
from console_widget import ConsoleWidget
from stoppable_thread import StoppableThread

# A track will ideally be a sequence of input registered, in order to be played back by the script.
# Resulting in a macro
class Track:
    key_list = list()
    is_registering = False
    mouse_listener = None
    time_at_start = None
    thread_of_late_execution : StoppableThread = None

    def __init__(self):
        self.key_list = list()
        self.is_registering = False
        self.mouse_listener = pynput.mouse.Listener(lambda x,y : self.OnMouseMoved(x,y), lambda x, y, button, pressed: self.OnMouseClicked(x, y, button, pressed), lambda x, y, dx, dy : self.OnScroll(x, y, dx, dy))
        self.keyboard_listener = pynput.keyboard.Listener(lambda x : self.OnKeyboarKeyPressed(x), lambda x : self.OnKeyboarKeyReleased(x))
    
    def StartTracking(self, delay : int, console_widget : ConsoleWidget):
        self.thread_of_late_execution = StoppableThread(target=self.__StartTrackingThread, args=(delay,console_widget), daemon=True)
    
    def __StartTrackingThread(self, tuple):
        #tuple = (delay:int, console_widget:ConsoleWidget)
        delay : int = tuple[0]
        console_widget : ConsoleWidget = tuple[1]

        starting_time = time.time()
        current_time = 0

        while current_time < delay: #since I can't use time.sleep(delay) because the thread is stopppable and I need to use at some occurence stopped(), I did this workaround of a timer
            if self.thread_of_late_execution.stopped():
                return
            current_time = time.time() - starting_time

        self.mouse_listener.start()
        self.keyboard_listener.start()
        console_widget.AddLog("Tracking Started")

    def StopTracking(self, console_widget : ConsoleWidget):
        if self.thread_of_late_execution:
            self.thread_of_late_execution.stop()
            self.thread_of_late_execution.join()
        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        console_widget.AddLog("Tracking Stoped")

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
        

