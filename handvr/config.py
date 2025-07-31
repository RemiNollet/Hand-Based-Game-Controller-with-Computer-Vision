# handvr/config.py
# -------------------------------------------------
# Central configuration file for screen size, gesture thresholds,
# axis inversion, smoothing, and gesture-action mapping.
# -------------------------------------------------

PINCH_THRESHOLD = 0.04

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

INVERT_X = True
INVERT_Y = False

# Gesture-to-action mapping
GESTURE_ACTIONS = {
    "right_2": "right_click",
    "right_3": "press_d",
    "right_4": "press_f",
    "right_5": "left_click",
    "left_2": "press_q",
    "left_3": "press_w",
    "left_4": "press_e",
    "left_5": "press_r"
}