from PySide6.QtCore import QThread
from track import Track
import time

class TrackReplayer(QThread):

    track_to_replay : Track = None
    replay_speed : float = 1
    MIN_REPLAY_SPEED = 0.1
    DEFAULT_REPLAY_SPEED = 1

    def __init__(self, track_to_replay : Track, replay_speed : float = DEFAULT_REPLAY_SPEED):
        super().__init__()
        self.track_to_replay = track_to_replay
        self.replay_speed = replay_speed if replay_speed > TrackReplayer.MIN_REPLAY_SPEED else TrackReplayer.MIN_REPLAY_SPEED

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
            has_key_been_executed = self.track_to_replay.key_list[current_key_index].ExecuteToKey(time.time()- start_time, self.replay_speed)
            if has_key_been_executed[0]:
                current_key_index+=1

        print("ReplayTrackAsync Done")
    
