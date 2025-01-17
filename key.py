import pyautogui
from enum import Enum
import os 
import win32api

class MouseKeyType(Enum):
    NONE = 0
    CLICKED = 1
    MOVED = 2
    SCROLLED = 3

class Key:

    time = 0.0
    mouse_data = None
    key_type : MouseKeyType = MouseKeyType.NONE

    def __init__(self, time, mouse_data, key_type : MouseKeyType):
        self.time = time
        self.mouse_data = mouse_data
        self.key_type = key_type
        self.mouse_button_clicked = None

    def ExecuteToKey(self, current_replay_time : float):
        """Execute to key is a method in which we'll try to reach the state of the key, meaning matching the mouse position"""
        was_key_executed : bool = current_replay_time >= self.time
        time_of_the_executed_key : float = self.time

        if(was_key_executed):
            if self.key_type == MouseKeyType.CLICKED:
                self.__ExecuteClick()
            elif self.key_type == MouseKeyType.MOVED:
                self.__ExecuteMoved()
            elif self.key_type == MouseKeyType.SCROLLED:
                self.__ExecuteScrolled()
            # else:
            #     was_key_executed = False

        return (was_key_executed, time_of_the_executed_key)

    def __ExecuteClick(self):
        print("click")        
        #data tuple = (x, y, button, isPressed)
        if self.mouse_data[3]:
            pyautogui.mouseDown(self.mouse_data[0], self.mouse_data[1], _pause=False)
        else:
            pyautogui.mouseUp(self.mouse_data[0], self.mouse_data[1], _pause=False)
    
    def __ExecuteMoved(self):
        # VvVvVvV Works for everything but minecraft 
        # win32api.SetCursorPos((self.mouse_data[0], self.mouse_data[1]))
        pyautogui.moveTo(self.mouse_data[0], self.mouse_data[1], _pause=False)
        #pyautogui.move(1,1)

    
    def __ExecuteScrolled(self):
        to_return : bool = False

        #pyautogui.scroll(1,  )
        #data tuple = (x, y, dx, dy)

        return to_return
            
            
