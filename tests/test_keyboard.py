from handvr import keyboard_control
from unittest.mock import MagicMock

def test_press_key_calls_press_and_release():
    mock_keyboard = MagicMock()
    keyboard_control.press_key(mock_keyboard, 'd')
    
    mock_keyboard.press.assert_called_once_with('d')
    mock_keyboard.release.assert_called_once_with('d')