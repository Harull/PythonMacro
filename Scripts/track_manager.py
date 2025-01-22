from track import Track

class TrackManager:

    track_list = list()

    def __init__(self):
        self.LoadListFromFile()

    def LoadListFromFile(self):
        #TODO Load from file
        self.track_list = list()

    def SaveInFile(self):
        #TODO Save in file
        pass

    def CreateNewTrack(self):
        new_track : Track = Track()
        self.track_list.append(new_track)
        return new_track 
    
    def DeleteTrackAtIndex(self, index : int):
        if index < 0 or index >= len(self.track_list):
            return
        self.track_list.pop(index)

    