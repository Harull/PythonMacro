import PySide6.QtWidgets as qt
from PySide6.QtCore import Qt
import PySide6.QtGui as qtgui

class QPSliderInfoWidget(qt.QWidget):
    def __init__(self, label_text :str, width_of_widget:int, min_slider_value:int, max_slider_value:int):
        super().__init__()

        self.width_of_widget = width_of_widget
        self.label_text = label_text
        self.min_slider_value = min_slider_value
        self.max_slider_value = max_slider_value

        self.main_horizontal_layout = qt.QHBoxLayout()
        self.setLayout(self.main_horizontal_layout)
        self.setFixedWidth(self.width_of_widget)

        self.InitWidgetContent()

    def InitWidgetContent(self):
        percent_size_of_left_right_items = 4

        label_text = qt.QLabel(self.label_text)
        self.main_horizontal_layout.addWidget(label_text)

        self.slider = qt.QSlider(Qt.Horizontal)
        self.slider.setMinimum(self.min_slider_value)
        self.slider.setMaximum(self.max_slider_value)
        self.slider.valueChanged.connect(lambda : self.line_edit.setText(self.slider.value().__str__()))
        self.main_horizontal_layout.addWidget(self.slider)

        self.line_edit = qt.QLineEdit()
        int_validator = qtgui.QIntValidator(self.min_slider_value,self.max_slider_value, self.line_edit)
        self.line_edit.setValidator(int_validator)
        self.line_edit.setFixedWidth(50)
        self.line_edit.textEdited.connect(lambda: self.slider.setValue(int(self.line_edit.text()) if self.line_edit.text() else 0))
        self.main_horizontal_layout.addWidget(self.line_edit)

        self.SetValue(self.min_slider_value)

    def GetValue(self):
        return self.slider.value()

    def SetValue(self, new_value : int):
        self.slider.setValue(new_value)
        self.line_edit.setText(new_value.__str__())

    def ConnectCallbackToValueChangedSignal(self, callback):
        self.slider.valueChanged.connect(callback)
        self.line_edit.textEdited.connect(callback)

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

