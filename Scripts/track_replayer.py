from PySide6.QtCore import QThread
from track import Track
import time

class TrackReplayer(QThread):

    track_to_replay : Track = None
    replay_speed : float = 1
    MIN_REPLAY_SPEED = 0.1
    DEFAULT_REPLAY_SPEED = 1
    list_of_callback_to_execute_uppon_finish : list = list()

    def __init__(self, track_to_replay : Track, number_of_replay : int, replay_is_looping : bool, replay_speed : float = DEFAULT_REPLAY_SPEED):
        super().__init__()
        self.number_of_replay = number_of_replay
        self.replay_is_looping = replay_is_looping
        self.list_of_callback_to_execute_uppon_finish = list()
        self.track_to_replay = track_to_replay
        self.replay_speed = replay_speed if replay_speed > TrackReplayer.MIN_REPLAY_SPEED else TrackReplayer.MIN_REPLAY_SPEED

    def run(self, delay_before_running : float = 0):
        time.sleep(delay_before_running)
        self.__ReplayTrack()
    
    def __ReplayTrack(self):
        ''' If you wan to replay a track, use run() instead'''
        print("ReplayTrackAsync Called")
        current_replay_count = 0

        # We replayplay all the keys, in loop, or till the number of iteration is complete
        #TODO Implement the failsafe, when you yeet the mouse in the corner to stop the record, so you basically need to catch the exeption to break the loop
        while (self.replay_is_looping or current_replay_count < self.number_of_replay):
            start_time = time.time()
            current_key_index = 0
            key_list_len = len(self.track_to_replay.key_list)

            if (key_list_len <= 0): 
                return
            
            while current_key_index < key_list_len:
                try:
                    has_key_been_executed = self.track_to_replay.key_list[current_key_index].ExecuteToKey(time.time()- start_time, self.replay_speed)
                except:
                    print("Failsafe handled, the replay stopped")
                    self.replay_is_looping = False
                    current_replay_count = self.number_of_replay
                    break
                if has_key_been_executed[0]:
                    current_key_index+=1

            current_replay_count+=1

        for i in self.list_of_callback_to_execute_uppon_finish:
            i()
            
        print("ReplayTrackAsync Done")

    def ConnectToExecuteUpponFinishReplay(self, callback_to_execute):
        self.list_of_callback_to_execute_uppon_finish.append(callback_to_execute)
        
        
    
