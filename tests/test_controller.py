from handvr import controller
from unittest.mock import MagicMock

def test_execute_gesture_mouse_action():
    mock_mouse = MagicMock()
    mock_keyboard = MagicMock()
    mock_logger = MagicMock()

    # Test left click gesture
    controller.execute_gesture("right_5", mock_mouse, mock_keyboard, mock_logger)
    mock_mouse.press.assert_called_once()
    mock_mouse.release.assert_called_once()
    mock_logger.info.assert_called_once()

def test_execute_gesture_keyboard_action():
    mock_mouse = MagicMock()
    mock_keyboard = MagicMock()
    mock_logger = MagicMock()

    # Test press 'd'
    controller.execute_gesture("right_3", mock_mouse, mock_keyboard, mock_logger)
    mock_keyboard.press.assert_called_once_with('d')
    mock_keyboard.release.assert_called_once_with('d')
    mock_logger.info.assert_called_once()