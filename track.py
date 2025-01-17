import pynput
import key
import time

# A track will ideally be a sequence of input registered, in order to be played back by the script.
# Resulting in a macro
class Track:
    key_list = list()
    is_registering = False
    mouse_listener = None
    time_at_start = None

    def __init__(self):
        self.key_list = list()
        self.is_registering = False
        self.mouse_listener = pynput.mouse.Listener(lambda x,y : self.OnMouseMoved(x,y), lambda x, y, button, pressed: self.OnMouseClicked(x, y, button, pressed), lambda x, y, dx, dy : self.OnScroll(x, y, dx, dy))

    
    def StartTracking(self,):
        self.time_at_start = time.time()
        self.mouse_listener.start()

    def StopTracking(self):
        self.mouse_listener.stop()

    def OnMouseClicked(self, x, y, button, pressed):
        # print(f"Mouse clicked: {x}, {y}, {button}, {pressed}\n")
        self.key_list.append(key.Key(time.time()-self.time_at_start, (x, y, button, pressed), key.MouseKeyType.CLICKED))

    def OnMouseMoved(self, x, y):
        # print(f"Mouse moved: {x}, {y}\n")
        self.key_list.append(key.Key(time.time()-self.time_at_start, (x, y), key.MouseKeyType.MOVED))

    def OnScroll(self, x, y, dx, dy):
        # print(f"Mouse scrolled: {x}, {y}, dir x {dx}, dir y {dy}\n")
        self.key_list.append(key.Key(time.time()-self.time_at_start, (x, y, dx, dy), key.MouseKeyType.SCROLLED))

   
        

