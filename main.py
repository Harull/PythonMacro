import PySide2.QtWidgets as qt
from main_window import MainWindow
from track import Track
import threading
import time
from track_replayer import TrackReplayer

app = qt.QApplication([])

main_window = MainWindow((1080,720))
main_window.show()

track = Track()
time.sleep(5)
print("record has started")
track.StartTracking()
time.sleep(5)
print("record will be played in 5sec")
def exec_thread():
    time.sleep(10)
    print("record start replaying")
    track.StopTracking()
    track_replayer = TrackReplayer(track)
    track_replayer.run()


thread = threading.Thread(target = exec_thread, daemon=True)
thread.start()

app.exec_()
