from time import sleep
from pynput import keyboard

def on_press(key : keyboard.KeyCode):
    try:
        key_code = key.vk
    except AttributeError:
        key_code = key.value.vk
    print("Suceeded" if keyboard.Key.f2 == key else "Failed")
    print(str(keyboard.Key.f2.name) + " vs " + str(key_code))

listener = keyboard.Listener(on_press=on_press)
listener.start()
try:
    while listener.is_alive():
        sleep
except KeyboardInterrupt:
    listener.stop()