from PySide2.QtCore import Qt
from track import Track
import PySide2.QtWidgets as qt
import PySide2.QtGui as qtgui
import buttons as qpb #qpb = Q Personal Button
import enum

class EDelayTime(enum.Enum):
    NO_DELAY = 0
    THREE_SECONDS = 3
    FIVE_SECONDS = 5
    TEN_SECONDS = 10
    MAX = enum.auto()

class MainWindow(qt.QMainWindow):

    window_size = (100, 100) 
    start_record_track_shortcut = "F2"
    stop_record_track_shortcut = "F3"
    last_or_current_recorded_track : Track = None
    is_recording_new_track : bool = False

    def __init__(self, window_size):
        super().__init__()
        self.window_size = window_size

        self.LoadAllFromSaveFiles()
        
        self.setWindowTitle("Macro Maker")
        self.setWindowIcon(qtgui.QIcon("Assets/MacroMakerLogo.png"))
        self.setMaximumSize(self.window_size[0], self.window_size[1])
        self.setMinimumSize(self.window_size[0], self.window_size[1])

        self.InitCreateTrackLayout()
        self.InitManageTracksLayout()
        self.InitReplayTrackLayout()
        self.InitTrackSchedulerLayout()
        self.InitHelpLayout()
        self.InitMenuBar()

        central_widget = qt.QWidget()
        central_widget.setLayout(self.create_track_layout)
        self.setCentralWidget(central_widget)

    def LoadAllFromSaveFiles(self):
        """In this method, we will be loading from file some saved settings or tracks, such as the binding to start the track recorder, or a track saved"""
        #TODO
        #Init self.start_record_track_shortcut = ""
        #Init self.stop_record_track_shortcut = ""
        pass
        

    def InitCreateTrackLayout(self):

        self.create_track_layout = qt.QVBoxLayout()

        name_layout = qt.QVBoxLayout()
        name_layout.addWidget(qt.QLabel("Enter the name of your next track to record"))
        self.new_track_name_line_edit = qt.QLineEdit()
        self.new_track_name_line_edit.setText("Default Track")
        name_layout.addWidget(self.new_track_name_line_edit)
        self.create_track_layout.addLayout(name_layout)

        shortcut_layout = qt.QVBoxLayout()
        shortcut_layout.addWidget(qt.QLabel("Edit main shortcuts"), alignment=Qt.AlignHCenter)
        shortcut_layout.addWidget(qt.QLabel("Start the Record"), aligment= Qt.AlignLeft)
        shortcut_layout.addWidget(qpb.QPBindingButton(self.start_record_track_shortcut, 100))
        shortcut_layout.addWidget(qt.QLabel("Stop the Record"), aligment= Qt.AlignLeft)
        shortcut_layout.addWidget(qpb.QPBindingButton(self.stop_record_track_shortcut, 100))
        self.create_track_layout.addLayout(shortcut_layout)


        validation_layout = qt.QVBoxLayout()
        validation_layout.addWidget(qt.QLabel("Add delay before the record goes on: "))
        self.start_time_offset_dropdown = qt.QComboBox()
        self.PopulateTimeOffsetDropdown()
        self.start_time_offset_dropdown.setFixedWidth(150)
        validation_layout.addWidget(self.start_time_offset_dropdown)
        self.start_stop_track_button = qpb.QPButton("Start/Stop Record", self.StartStopRecordButtonPressed)
        validation_layout.addWidget(self.start_stop_track_button)
        self.create_track_layout.addLayout(validation_layout)
        pass
    
    
    def InitManageTracksLayout(self):

        self.manage_tracks_layout = qt.QVBoxLayout()
        
        pass

    def InitReplayTrackLayout(self):

        self.replay_track_layout = qt.QVBoxLayout()

        pass

    def InitTrackSchedulerLayout(self):

        self.track_scheduler_layout = qt.QVBoxLayout()

        pass

    def InitHelpLayout(self):

        self.help_layout = qt.QVBoxLayout()

        pass

    
    def InitMenuBar(self):
        
        menu_bar = self.menuBar()
        
        #TODO find a way to make tooltips work
        create_track_qAction = qt.QAction("Create Track", self)
        create_track_qAction.triggered.connect(lambda checked: self.ChangeMainWidgetsLayout(self.create_track_layout))
        create_track_qAction.setToolTip("Start creating a new track")
        menu_bar.addAction(create_track_qAction)

        manage_tracks_qAction = qt.QAction("Manage Tracks", self)
        manage_tracks_qAction.triggered.connect(lambda checked: self.ChangeMainWidgetsLayout(self.manage_tracks_layout))
        manage_tracks_qAction.setToolTip("Manage your existing tracks")
        menu_bar.addAction(manage_tracks_qAction)

        replay_tracks_qAction = qt.QAction("Replay Tracks", self)
        replay_tracks_qAction.triggered.connect(lambda checked: self.ChangeMainWidgetsLayout(self.replay_track_layout))
        replay_tracks_qAction.setToolTip("Simply select and replay a track") 
        menu_bar.addAction(replay_tracks_qAction)

        schedule_tracks_qAction = qt.QAction("Schedule Tracks", self)
        schedule_tracks_qAction.triggered.connect(lambda checked: self.ChangeMainWidgetsLayout(self.track_scheduler_layout))
        schedule_tracks_qAction.setToolTip("Schedule a track to be replayed at a given time")
        menu_bar.addAction(schedule_tracks_qAction)

        help_qAction = qt.QAction(qtgui.QIcon("Assets/help-icon-white.png"), "Help", self)
        help_qAction.setToolTip("Learn how to use the Macro Maker")
        help_qAction.triggered.connect(lambda checked: self.ChangeMainWidgetsLayout(self.help_layout))
        menu_bar.addAction(help_qAction)

    def ChangeMainWidgetsLayout(self, new_layout : qt.QLayout):
        new_central_widget = qt.QWidget()
        new_central_widget.setLayout(new_layout)
        self.setCentralWidget(new_central_widget)

    def StartStopRecordButtonPressed(self):
        pass

    def StartRecordingThread(self):
        pass

    def StopRecordingThread(self):
        pass

    def PopulateTimeOffsetDropdown(self):
        for i in range(EDelayTime.MAX.value):
            try:
                enum = EDelayTime(i)
            except:
                continue
            self.start_time_offset_dropdown.addItem(qtgui.QIcon(f"Assets/{enum.name}.png"), f"{i}-second delay" if i > 0 else "No delay", i)
            
    