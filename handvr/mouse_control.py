from pynput.mouse import Controller, Button

def move_mouse(mouse: Controller, landmarks, screen_width=1440, screen_height=900):
    """
    Move the mouse pointer based on the position of the thumb tip.

    Parameters:
        mouse (Controller): Pynput mouse controller object.
        landmarks (list): List of 21 (x, y, z) hand landmarks.
        screen_width (int): Optional, screen width in pixels.
        screen_height (int): Optional, screen height in pixels.
    """

    core_points = [landmarks[i] for i in [0, 5, 9, 13, 17]]
    x_norm = sum(p[0] for p in core_points) / len(core_points)
    y_norm = sum(p[1] for p in core_points) / len(core_points)

    # Convert normalized coordinates to screen position
    x_pixel = int((1 - x_norm) * screen_width)  # flip X horizontally
    y_pixel = int(y_norm * screen_height)

    # Optional: invert y to match screen coordinates if needed
    mouse.position = (x_pixel, y_pixel)
    # print(f"Mouse moved to: {mouse.position}")

def left_click(mouse):
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)

def right_click(mouse):
    # Press and release
    mouse.press(Button.right)
    mouse.release(Button.right)