from handvr import mouse_control, config
from unittest.mock import MagicMock

def test_move_mouse_coordinates_conversion():
    landmarks = [(0.1, 0.2, 0.0)] * 21  # Simulate wrist at (0.1, 0.2)
    landmarks[0] = (0.1, 0.2, 0.0)      # Wrist = landmark 0

    mock_mouse = MagicMock()
    mouse_control.move_mouse(mock_mouse, landmarks, screen_width=config.SCREEN_WIDTH, screen_height=config.SCREEN_HEIGHT)

    expected_x = int((1 - 0.1) * 1000)
    expected_y = int(0.2 * 500)

    mock_mouse.position = (expected_x, expected_y)
    assert mock_mouse.position == (expected_x, expected_y)