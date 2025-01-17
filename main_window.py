import PySide2.QtWidgets as qt

class MainWindow(qt.QMainWindow):

    window_size = (100, 100) 

    def __init__(self, window_size):
        super().__init__()
        self.window_size = window_size

        self.setMaximumSize(self.window_size[0], self.window_size[1])
        self.setMinimumSize(self.window_size[0], self.window_size[1])


    