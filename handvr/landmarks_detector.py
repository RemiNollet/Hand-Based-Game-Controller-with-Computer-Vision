# handvr/detector.py
# -------------------------------------------------
# This module defines the HandDetector class, which
# uses Mediapipe to detect hand landmarks from webcam frames.
# It returns a list of 21 (x, y, z) landmarks per hand.
# Optionally, it can draw the detected hands on the frame.
# -------------------------------------------------

import mediapipe as mp
import cv2

class HandDetector:
    def __init__(self, max_hands=2, detection_conf=0.5, tracking_conf=0.5, static_image_mode=False):
        """
        Initialize the Mediapipe hand detection module.

        Parameters:
            max_hands (int): Maximum number of hands to detect.
            detection_conf (float): Minimum confidence for initial hand detection.
            tracking_conf (float): Minimum confidence for hand tracking after detection.
            static_image_mode (bool): If True, treats input as a static image.
        """
        self.max_hands = max_hands

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=static_image_mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=detection_conf,
            min_tracking_confidence=tracking_conf
        )

        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self, frame, draw=True):
        """
        Process a video frame to detect hand landmarks.

        Parameters:
            frame (np.array): The BGR frame from OpenCV.
            draw (bool): If True, draw landmarks on the frame.

        Returns:
            frame (np.array): The frame with or without drawings (flipped horizontally).
            landmarks_list (list): List of 21 landmarks per detected hand,
                                   each as (x, y, z) normalized coordinates.
        """
        # Convert to RGB for Mediapipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        landmarks_list = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks and connections if required
                if draw:
                    self.mp_draw.draw_landmarks(
                        frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                    )

                # Extract 3D landmark coordinates
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.append((lm.x, lm.y, lm.z))  # Normalized to image size
                landmarks_list.append(landmarks)

        # Optional: flip the frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)

        return frame, landmarks_list