import PySide2.QtWidgets as qt

class QPBindingButton(qt.QPushButton):
    current_binding : str = ""
    def __init__(self, initial_binding : str, width:int):
        super().__init__(initial_binding)

        self.setFixedWidth(width)
        self.current_binding = initial_binding
    
    def GetBinding(self):
        return self.current_binding 
    
    def SetBinding(self, new_binding:str):
        self.current_binding = new_binding

    def OpenRebindDialog(self):
        """This method allows to change your current binding"""
        #TODO a personal dialog window, where we can "listen" for keyboard inputs, and overwrite the current binding, we want a qline_edit in read only, with 1 button "listen" and one button "apply"
        pass

class QPButton(qt.QPushButton):
    def __init__(self, text : str, callback, width : int = None):
        super().__init__(text)
        self.clicked.connect(callback)
        if width:
            self.setFixedWidth(width)

