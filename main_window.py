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

        self.InitFirstLayout()
        self.InitSecondaryLayout()
        self.InitMenuBar()

        central_widget = qt.QWidget()
        self.setMenuBar()

    def InitFirstLayout(self):

        self.first_layout = qt.QVBoxLayout()

        pass
    
    def InitSecondaryLayout(self):

        self.secondary_layout = qt.QVBoxLayout()
        
        pass
    
    def InitMenuBar(self):
        
        self.menu_bar = qt.QMenuBar()
        self.menu_bar.addAction()
        
        
        pass

    def ChangeMainWidgetsLayout(self, new_layout : qt.QLayout):
        new_central_widget = self.centralWidget()
        new_central_widget.setLayout(new_layout)
        self.setCentralWidget(new_central_widget)



    