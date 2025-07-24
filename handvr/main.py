# handvr/main.py
# -----------------------------------------------
# Main entry point of the application.
# Captures webcam frames, detects hand landmarks using Mediapipe,
# and identifies gestures like pinch or open palm using gestures.py.
# -----------------------------------------------

import cv2
import logging

from pynput.mouse import  Controller as mouse_Controller
from pynput.keyboard import Controller as kb_Controller

from handvr.landmarks_detector import HandDetector
from handvr import gestures
from handvr import mouse_control, keyboard_control

# ---------- Logger setup ----------
logging.basicConfig(
    filename='hand_gesture_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
# ----------------------------------

def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    mouse = mouse_Controller()
    keyboard = kb_Controller()

    print("[INFO] Starting webcam. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to read from webcam.")
            break

        # Run hand detection and get landmarks
        frame, landmarks_list = detector.detect_hands(frame)

        if landmarks_list:
            landmarks_left = landmarks_list[0]  # Assume first hand = left

            if len(landmarks_list) > 1:
                landmarks_right = landmarks_list[1]  # Second = right hand

                # Mouse position control
                mouse_control.move_mouse(mouse, landmarks_right, screen_width=1440, screen_height=900)

                # --- Right hand gestures ---
                if gestures.is_pinch(landmarks_right, finger=2):
                    cv2.putText(frame, "Pinch Index right hand (Right Click)", (10, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
                    mouse_control.right_click(mouse)
                    logger.info("Right hand: pinch index → right click")

                elif gestures.is_pinch(landmarks_right, finger=3):
                    cv2.putText(frame, "Pinch Middle right hand (Press D)", (10, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    keyboard_control.press_key(keyboard, 'd')
                    logger.info("Right hand: pinch middle → (D)")

                elif gestures.is_pinch(landmarks_right, finger=4):
                    cv2.putText(frame, "Pinch Ring right hand (Press F)", (10, 130),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                    keyboard_control.press_key(keyboard, 'f')
                    logger.info("Right hand: pinch ring → (F)")

                elif gestures.is_pinch(landmarks_right, finger=5):
                    cv2.putText(frame, "Pinch Pinky right hand (Left Click)", (10, 160),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
                    mouse_control.left_click(mouse)
                    logger.info("Right hand: pinch pinky → left click")

                # --- Left hand gestures ---
                if gestures.is_pinch(landmarks_left, finger=2):
                    cv2.putText(frame, "Pinch Index left hand (Press q)", (1000, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
                    keyboard_control.press_key(keyboard, 'q')
                    logger.info("Left hand: pinch index → Q")

                elif gestures.is_pinch(landmarks_left, finger=3):
                    cv2.putText(frame, "Pinch Middle left hand (Press W)", (1000, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    keyboard_control.press_key(keyboard, 'w')
                    logger.info("Left hand: pinch middle → W")

                elif gestures.is_pinch(landmarks_left, finger=4):
                    cv2.putText(frame, "Pinch Ring left hand (Press E)", (1000, 130),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                    keyboard_control.press_key(keyboard, 'e')
                    logger.info("Left hand: pinch ring → E")

                elif gestures.is_pinch(landmarks_left, finger=5):
                    cv2.putText(frame, "Pinch Pinky left hand (Press R)", (1000, 160),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
                    keyboard_control.press_key(keyboard, 'r')
                    logger.info("Left hand: pinch pinky → R")

        cv2.imshow("Hand Tracking", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()