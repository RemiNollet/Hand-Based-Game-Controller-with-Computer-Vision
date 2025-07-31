# handvr/controller.py
# -------------------------------------------------
# Maps gesture strings (like "left_3") to system actions.
# Uses mouse_control and keyboard_control modules.
# -------------------------------------------------

from handvr import mouse_control, keyboard_control
from handvr import config

def execute_gesture(gesture_key, mouse, keyboard, logger=None):
    """
    Executes a system action based on the gesture key.
    gesture_key format: "left_2", "right_5", etc.
    """
    action = config.GESTURE_ACTIONS.get(gesture_key)

    if not action:
        return

    if action == "left_click":
        mouse_control.left_click(mouse)
    elif action == "right_click":
        mouse_control.right_click(mouse)
    elif action.startswith("press_"):
        key_char = action[-1]
        keyboard_control.press_key(keyboard, key_char)

    if logger:
        logger.info(f"{gesture_key} → {action}")