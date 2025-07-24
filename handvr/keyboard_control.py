from pynput.keyboard import Key, Controller

def press_key(keyboard, key):
    # Press and release space
    keyboard.press(key)
    keyboard.release(key)