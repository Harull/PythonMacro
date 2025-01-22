import pyautogui
import pydirectinput
import pynput
from enum import Enum
import os 
import win32api

class InputKeyType(Enum):
    NONE = 0
    MOUSE_CLICKED = 1
    MOUSE_MOVED = 2
    MOUSE_SCROLLED = 3
    KEYBOARD_KEY_PRESSED = 4
    KEYBOARD_KEY_REALEASED = 5

class Key:

    time = 0.0
    key_data = None
    key_type : InputKeyType = InputKeyType.NONE

    def __init__(self, time, key_data, key_type : InputKeyType):
        self.time = time
        self.key_data = key_data
        self.key_type = key_type
        self.mouse_button_clicked = None

    def ExecuteToKey(self, current_replay_time : float, replay_speed : float):
        """Execute to key is a method in which we'll try to reach the state of the key, meaning matching the mouse position"""
        was_key_executed : bool = current_replay_time >= self.time/replay_speed
        time_of_the_executed_key : float = self.time /replay_speed

        #Note to self, i would love to use a "match" statement, but it's not available for the python version I'm currently using
        if(was_key_executed):
            if self.key_type == InputKeyType.MOUSE_CLICKED:
                self.__ExecuteClick()
            elif self.key_type == InputKeyType.MOUSE_MOVED:
                self.__ExecuteMoved()
            elif self.key_type == InputKeyType.MOUSE_SCROLLED:
                self.__ExecuteScrolled()
            elif self.key_type == InputKeyType.KEYBOARD_KEY_PRESSED:
                self.__ExecuteKeyboardKeyPressed()
            elif self.key_type == InputKeyType.KEYBOARD_KEY_REALEASED:
                self.__ExecuteKeyboardKeyReleased()
            # else:
            #     was_key_executed = False

        return (was_key_executed, time_of_the_executed_key)

    def __ExecuteClick(self):
        #data tuple = (x, y, button, isPressed)

        if self.key_data[3]:
            pydirectinput.mouseDown(self.key_data[0], self.key_data[1], _pause=False)
        else:
            pydirectinput.mouseUp(self.key_data[0], self.key_data[1], _pause=False)
    
    def __ExecuteMoved(self):
        #data tuple = (x, y)

        # VvVvVvV try to make relative movement so it can work in minecraft aswell
        pydirectinput.moveTo(self.key_data[0], self.key_data[1], _pause = False)

    def __ExecuteScrolled(self):
        #data tuple = (x, y, dx, dy)

        print(self.key_data)
        pynput.mouse.Controller().scroll(self.key_data[2],self.key_data[3])

    def __ExecuteKeyboardKeyPressed(self):
        #data tuple = (concerned key)

        pynput.keyboard.Controller().press(self.key_data[0])
        pass            


    def __ExecuteKeyboardKeyReleased(self):
        #data tuple = (concerned key)

        pynput.keyboard.Controller().release(self.key_data[0])
        # print(f"Trying to reproduce 'RELEASED' on the keycode: {self.key_data[0]}")
        # pydirectinput.keyUp(self.key_data[0])
        # pynput.keyboard.Controller().release(self.key_data[0])

        pass

            
