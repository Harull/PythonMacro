from PySide6.QtCore import Qt
from track import Track
import PySide6.QtWidgets as qt
import PySide6.QtGui as qtgui
import qpersonaliezd_widgets as qp #qpb = Q Personal Button
from console_widget import QPConsoleWidget
import enum
from dictionary_utility import DictionaryUtil

class EDelayTime(enum.Enum):
    NO_DELAY = 0
    THREE_SECONDS = 3
    FIVE_SECONDS = 5
    TEN_SECONDS = 10
    MAX = enum.auto()

class MainWindow(qt.QMainWindow):

    DEFAULT_TRACK_NAME = "Default Track"
    window_size = (100, 100) 
    start_record_track_shortcut = "F2"
    stop_record_track_shortcut = "F3"
    drop_edit_flag_shortcut = "F4"
    last_or_current_track : Track = None
    is_recording_new_track : bool = False
    all_recorded_tracks_dictionary = dict() # key : str, value : Track)

    def __init__(self, window_size):
        super().__init__()
        self.window_size = window_size
        self.setToolTipDuration(1)

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

        self.central_stacked_widget = qt.QStackedWidget()
        self.central_stacked_widget.addWidget(self.create_track_widget)
        self.central_stacked_widget.addWidget(self.manage_tracks_widget)
        self.central_stacked_widget.addWidget(self.replay_track_widget)
        self.central_stacked_widget.addWidget(self.track_scheduler_widget)
        self.central_stacked_widget.addWidget(self.help_widget)
        self.central_stacked_widget.setCurrentWidget(self.create_track_widget)
        self.setCentralWidget(self.central_stacked_widget)

    def LoadAllFromSaveFiles(self):
        """In this method, we will be loading from file some saved settings or tracks, such as the binding to start the track recorder, or a track saved"""
        #TODO
        #Init self.start_record_track_shortcut = ""
        #Init self.stop_record_track_shortcut = ""
        #Init self.drop_edit_flag_shortcut = ""
        #Init self.all_recorded_tracks
        pass
        

    def InitCreateTrackLayout(self):

        create_track_layout = qt.QVBoxLayout()
        create_track_layout.setAlignment(Qt.AlignTop)
        self.create_track_widget = qt.QWidget()
        self.create_track_widget.setLayout(create_track_layout)
        create_track_layout.addItem(qt.QSpacerItem(0,15))

        name_layout = qt.QVBoxLayout()
        name_layout.addWidget(qt.QLabel("Enter the name of your next track to record"))
        self.new_track_name_line_edit = qt.QLineEdit()
        self.new_track_name_line_edit.setText(self.DEFAULT_TRACK_NAME)
        name_layout.addWidget(self.new_track_name_line_edit)
        create_track_layout.addLayout(name_layout)
        create_track_layout.addItem(qt.QSpacerItem(0,25))

        shortcut_layout = qt.QVBoxLayout()
        shortcut_layout.addWidget(qt.QLabel("Edit main shortcuts"), alignment=Qt.AlignmentFlag.AlignHCenter)
        shortcut_layout.addWidget(qt.QLabel("Start the Record"),alignment= Qt.AlignmentFlag.AlignLeft)
        shortcut_layout.addWidget(qp.QPBindingButton(self.start_record_track_shortcut, 100))
        shortcut_layout.addWidget(qt.QLabel("Stop the Record"),alignment= Qt.AlignmentFlag.AlignLeft)
        shortcut_layout.addWidget(qp.QPBindingButton(self.stop_record_track_shortcut, 100))
        shortcut_layout.addWidget(qt.QLabel("Advanced Shortcuts"),alignment= Qt.AlignmentFlag.AlignHCenter)
        shortcut_layout.addWidget(qt.QLabel("Drop edit flag"),alignment= Qt.AlignmentFlag.AlignLeft)
        shortcut_layout.addWidget(qp.QPBindingButton(self.drop_edit_flag_shortcut, 100))

        create_track_layout.addLayout(shortcut_layout)
        create_track_layout.addItem(qt.QSpacerItem(0,25))

        validation_layout = qt.QVBoxLayout()
        validation_layout.addWidget(qt.QLabel("Add delay before the record goes on: "))
        self.start_time_offset_dropdown = qt.QComboBox()
        self.PopulateTimeOffsetDropdown(self.start_time_offset_dropdown)
        self.start_time_offset_dropdown.setFixedWidth(150)
        validation_layout.addWidget(self.start_time_offset_dropdown)
        self.start_stop_track_button = qp.QPButton("Start/Stop Record", self.StartStopRecordButtonPressed)
        validation_layout.addWidget(self.start_stop_track_button)
        create_track_layout.addLayout(validation_layout)
        create_track_layout.addItem(qt.QSpacerItem(0,25))

        create_track_layout.addWidget(qt.QLabel("Feedback console: "),alignment= Qt.AlignmentFlag.AlignHCenter)
        self.console_log = QPConsoleWidget()
        create_track_layout.addWidget(self.console_log)
    
    
    def InitManageTracksLayout(self):

        manage_tracks_layout = qt.QVBoxLayout()
        self.manage_tracks_widget = qt.QWidget()
        self.manage_tracks_widget.setLayout(manage_tracks_layout)

        manage_tracks_layout.addWidget(qt.QLabel("Here are all your recorded tracks:", alignment=Qt.AlignmentFlag.AlignHCenter))

        self.recorded_track_replay_section_list = qt.QListWidget()
        self.recorded_track_replay_section_list.setSelectionMode(qt.QAbstractItemView.SelectionMode.MultiSelection)
        manage_tracks_layout.addWidget(self.recorded_track_replay_section_list)

        delete_selected_tracks_button = qp.QPButton("Delete Selected Tracks", self.DeleteSelectedTracks)
        manage_tracks_layout.addWidget(delete_selected_tracks_button)

        delete_selected_tracks_button = qp.QPButton("Edit Selected Track", self.EditSelectedTrack)
        manage_tracks_layout.addWidget(delete_selected_tracks_button)

        pass

    def InitReplayTrackLayout(self):

        replay_track_layout = qt.QVBoxLayout()
        self.replay_track_widget = qt.QWidget()
        self.replay_track_widget.setLayout(replay_track_layout)

        first_h_layout = qt.QHBoxLayout()

        first_v_layout = qt.QVBoxLayout()
        first_v_layout.addWidget(qt.QLabel("Select A Track"), alignment=Qt.AlignmentFlag.AlignHCenter)
        self.recorded_track_replay_section_list = qt.QListWidget()
        first_v_layout.addWidget(self.recorded_track_replay_section_list)

        second_v_layout = qt.QVBoxLayout()
        second_v_layout.addWidget(qt.QLabel("Replay Options"), alignment=Qt.AlignmentFlag.AlignHCenter)
        second_v_layout.addWidget(qt.QLabel("Add delay before the track replays: "))
        self.replay_time_offset_dropdown = qt.QComboBox()
        self.PopulateTimeOffsetDropdown(self.replay_time_offset_dropdown)
        second_v_layout.addWidget(self.replay_time_offset_dropdown)
        self.replay_speed_multiplier_slider = qp.QPSliderInfoWidget("Replay Speed Multiplier", 400, 1, 10)
        second_v_layout.addWidget(self.replay_speed_multiplier_slider)
        self.play_w_edited_parts_checkbox = qt.QCheckBox("Play with edited parts")
        second_v_layout.addWidget(self.play_w_edited_parts_checkbox)
        self.play_in_loop = qt.QCheckBox("Play in loop")
        self.play_in_loop.stateChanged.connect(lambda new_state: self.play_count_slider.setDisabled(new_state))
        second_v_layout.addWidget(self.play_in_loop)

        self.play_count_slider = qp.QPSliderInfoWidget("Play a number of times",400,1,100)
        second_v_layout.addWidget(self.play_count_slider)
        
        first_h_layout.addLayout(first_v_layout)
        first_h_layout.addLayout(second_v_layout)

        replay_track_layout.addLayout(first_h_layout)
       



        pass

    def InitTrackSchedulerLayout(self):

        track_scheduler_layout = qt.QVBoxLayout()
        self.track_scheduler_widget = qt.QWidget()
        self.track_scheduler_widget.setLayout(track_scheduler_layout)

        pass

    def InitHelpLayout(self):

        help_layout = qt.QVBoxLayout()
        self.help_widget = qt.QWidget()
        self.help_widget.setLayout(help_layout)

        pass

    
    def InitMenuBar(self):
        
        menu_bar = self.menuBar()
        
        #TODO find a way to make tooltips work
        create_track_qAction = qtgui.QAction("Create Track", self)
        create_track_qAction.triggered.connect(lambda checked: self.ChangeCurrentWidgetInStackedWidget(self.create_track_widget))
        create_track_qAction.setToolTip("Start creating a new track")
        menu_bar.addAction(create_track_qAction)

        manage_tracks_qAction = qtgui.QAction("Manage Tracks", self)
        manage_tracks_qAction.triggered.connect(lambda checked: self.ChangeCurrentWidgetInStackedWidget(self.manage_tracks_widget))
        manage_tracks_qAction.setToolTip("Manage your existing tracks")
        menu_bar.addAction(manage_tracks_qAction)

        replay_tracks_qAction = qtgui.QAction("Replay Tracks", self)
        replay_tracks_qAction.triggered.connect(lambda checked: self.ChangeCurrentWidgetInStackedWidget(self.replay_track_widget))
        replay_tracks_qAction.setToolTip("Simply select and replay a track") 
        menu_bar.addAction(replay_tracks_qAction)

        schedule_tracks_qAction = qtgui.QAction("Schedule Tracks", self)
        schedule_tracks_qAction.triggered.connect(lambda checked: self.ChangeCurrentWidgetInStackedWidget(self.track_scheduler_widget))
        schedule_tracks_qAction.setToolTip("Schedule a track to be replayed at a given time")
        menu_bar.addAction(schedule_tracks_qAction)

        help_qAction = qtgui.QAction(qtgui.QIcon("Assets/help-icon-white.png"), "Help", self)
        help_qAction.setToolTip("Learn how to use the Macro Maker")
        help_qAction.triggered.connect(lambda checked: self.ChangeCurrentWidgetInStackedWidget(self.help_widget))
        menu_bar.addAction(help_qAction)

    def ChangeCurrentWidgetInStackedWidget(self, new_widget : qt.QWidget):
        self.central_stacked_widget.setCurrentWidget(new_widget)

    def StartStopRecordButtonPressed(self):
        if self.is_recording_new_track and self.last_or_current_track:
            self.StopRecording()
        else:
            self.StartRecording()

    def StartRecording(self):
        if self.is_recording_new_track:
            return
        self.last_or_current_track = Track()
        self.last_or_current_track.StartTracking(self.start_time_offset_dropdown.currentData(), self.console_log)
        self.is_recording_new_track = True

    def StopRecording(self):
        if not self.is_recording_new_track:
            return
        self.last_or_current_track.StopTracking(self.console_log)
        valid_name_of_track = self.GetUniqueTrackName()
        self.all_recorded_tracks_dictionary.update({valid_name_of_track : self.last_or_current_track})
        self.recorded_track_replay_section_list.addItem(valid_name_of_track)
        self.console_log.AddLog(f"The track was saved as '{valid_name_of_track}'")
        self.is_recording_new_track = False

    def PopulateTimeOffsetDropdown(self, dropdown : qt.QComboBox):
        for i in range(EDelayTime.MAX.value):
            try:
                enum = EDelayTime(i)
            except:
                continue
            dropdown.addItem(qtgui.QIcon(f"Assets/{enum.name}.png"), f"{i}-second delay" if i > 0 else "No delay", i)

    def GetUniqueTrackName(self):
        """This method is used to have a unique track name, the name will try to be the one in 'self.new_track_name_line_edit.text()'"""
        wanted_name = self.new_track_name_line_edit.text()
        wanted_name = wanted_name if len(wanted_name) > 0 else self.DEFAULT_TRACK_NAME
        return DictionaryUtil.GetUniqueStringKey(self.all_recorded_tracks_dictionary, wanted_name)
    
    def DeleteSelectedTracks(self):
        list_of_index_selected = self.recorded_track_replay_section_list.selectedIndexes()
        count_of_items_selected = len(list_of_index_selected)

        # If you have no items selected return
        if count_of_items_selected <= 0:
            return

        # Put all the items selected string in a single string, with indentation as a list
        list_as_text = ""
        for index in list_of_index_selected:
            list_as_text += "- " + self.recorded_track_replay_section_list.item(index.row()).text() + "\n"

        # Open dialog box to ask if the user is sure and wants to delete
        return_value = qt.QMessageBox.question(self, "Are you sure you want to proceed? ", f"{count_of_items_selected} items to delete:\n{list_as_text}", qt.QMessageBox.Yes | qt.QMessageBox.No, qt.QMessageBox.No)

        if return_value == qt.QMessageBox.Yes:
            # If the user wants to delete those tracks, we delete them.
            offset = 0
            for index in list_of_index_selected:
                item_text = self.recorded_track_replay_section_list.item(index.row()-offset).text()
                self.all_recorded_tracks_dictionary.pop(item_text)
                self.recorded_track_replay_section_list.takeItem(index.row()-offset)
                self.console_log.AddLog(f"Deleted the track '{item_text}'")
                offset+=1

    def EditSelectedTrack(self):
        # qt.QDialogButtonBox.open()

        #The idea of this button is to open a window where you can "modify" your track, what I hear by modifying the recorded track is:
        # - Add the possibility to write text + press enter, at a given moment
        # - Add the possibility to write a random text among a list of text that the user gives
        # - Add the possibility to play a track to play at a given moment
        # - Add the possibility to press a chosen key at a given moment, just like "enter" for example

        # There is only a condition to where you can Edit your tracks:
        # You can only modify tracks where they have a "modify track flag" on them. It means that during the recording you need to drop a flag by pressing your corresponding shortcut key. 
        pass #TODO

    def CheckSingleSelection(self, list : qt.QListWidget):
        return len(list.selectedIndexes()) == 1
