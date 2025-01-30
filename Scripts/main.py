import PySide6.QtWidgets as qt
import PySide6.QtCore as qtcore
from main_window import MainWindow
from track import Track
import threading
import time
from track_replayer import TrackReplayer
from style_sheet import dark_theme
from font_loader import FontLoader


app = qt.QApplication([])
app.setStyleSheet(dark_theme)
app.setFont(FontLoader.GetQFont("Assets/Lato/Lato-Regular.ttf"))
main_window = MainWindow((1080,720))
main_window.show()



def exec_thread():
    track = Track()
    time.sleep(5)
    print("<RECORD> has started")
    track.StartTracking()
    time.sleep(10)
    track.StopTracking()
    print("<RECORD> stopped, will be played in 10sec")
    time.sleep(10)
    print("<RECORD> start replaying")
    track_replayer = TrackReplayer(track, 0.5)
    track_replayer.run()


# thread = threading.Thread(target = exec_thread, daemon=True)
# thread.start()

app.exec()

# from pynput import keyboard

# def OnKeyboarKeyPressed(key_pressed):
#     print(key_pressed.__str__()+ "\n")
    
# def OnKeyboarKeyReleased(key_released):
#     print(key_released.__str__() + "\n")

# test_listener = keyboard.Listener(OnKeyboarKeyPressed, OnKeyboarKeyReleased)
# test_listener.start()

# while True:
#     pass
