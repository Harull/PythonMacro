import PySide2.QtWidgets as qt
from main_window import MainWindow
from track import Track
import threading
import time
from track_replayer import TrackReplayer

app = qt.QApplication([])

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


thread = threading.Thread(target = exec_thread, daemon=True)
thread.start()

app.exec_()

# from pynput import keyboard


# def OnKeyboarKeyPressed(key_pressed):
#     print(key_pressed.__str__()+ "\n")
    
# def OnKeyboarKeyReleased(key_released):
#     print(key_released.__str__() + "\n")

# test_listener = keyboard.Listener(OnKeyboarKeyPressed, OnKeyboarKeyReleased)
# test_listener.start()

# while True:
#     pass
