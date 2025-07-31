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
from handvr import gestures, config, controller
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

    print("[INFO] Starting webcam. Press 'p' to exit.")

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

                for hand_label, landmarks in [("right", landmarks_right), ("left", landmarks_left)]:
                    for finger in range(2, 6):  # Index to pinky
                        if gestures.is_pinch(landmarks, finger=finger, threshold=config.PINCH_THRESHOLD):
                            x = 10 if hand_label == "right" else 800
                            y = 60 + 30 * (finger - 2)
                            cv2.putText(frame, f"Pinch {finger} ({hand_label})", (x, y),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 0, 0), 2)
                            gesture_key = f"{hand_label}_{finger}"
                            controller.execute_gesture(gesture_key, mouse, keyboard, logger)

        cv2.imshow("Hand Tracking", frame)

        key = cv2.waitKey(1)
        if key == ord('l'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()