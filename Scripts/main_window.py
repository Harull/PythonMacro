import PySide2.QtWidgets as qt
import PySide2.QtGui as qtgui

class MainWindow(qt.QMainWindow):

    window_size = (100, 100) 

    def __init__(self, window_size):
        super().__init__()
        self.window_size = window_size
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

    def InitCreateTrackLayout(self):

        self.create_track_layout = qt.QVBoxLayout()

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
        new_central_widget = self.centralWidget()
        new_central_widget.setLayout(new_layout)
        self.setCentralWidget(new_central_widget)
    