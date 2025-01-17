from PySide2.QtCore import QThread
from track import Track
import time

class TrackReplayer(QThread):

    track_to_replay : Track = None

    def __init__(self, track_to_replay : Track):
        super().__init__()
        self.track_to_replay = track_to_replay

    def run(self):
        self.ReplayTrack()
    
    def ReplayTrack(self):
        print("ReplayTrackAsync Called")
        start_time = time.time()
        current_key_index = 0
        key_list_len = len(self.track_to_replay.key_list)

        if (key_list_len <= 0): 
            return
        
        while current_key_index < key_list_len:
            has_key_been_executed = self.track_to_replay.key_list[current_key_index].ExecuteToKey(time.time()- start_time)
            if has_key_been_executed[0]:
                current_key_index+=1

        print("ReplayTrackAsync Done")
    
