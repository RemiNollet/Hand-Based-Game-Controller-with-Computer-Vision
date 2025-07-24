# handvr/gestures.py
# -----------------------------------------------
# This module defines hand gesture recognition functions.
# It processes 21 hand landmarks (from Mediapipe) to detect
# specific gestures such as a "pinch" or an "open palm".
# -----------------------------------------------

import math

def distance(p1, p2):
    """
    Compute the Euclidean distance between two 3D points.
    Each point is a tuple (x, y, z) with normalized coordinates.
    """
    return math.sqrt((p1[0] - p2[0])**2 +
                     (p1[1] - p2[1])**2 +
                     (p1[2] - p2[2])**2)

def is_pinch(landmarks, threshold=0.08, finger=2):
    """
    Check if the user is performing a pinch gesture
    (thumb touching a specific finger).

    Parameters:
        landmarks (list): List of 21 (x, y, z) hand landmarks
        threshold (float): Maximum distance to consider a pinch
        finger (int): Finger index to check pinch against:
                      2 = index (default)
                      3 = middle
                      4 = ring
                      5 = pinky

    Returns:
        bool: True if pinch is detected, False otherwise
    """
    if len(landmarks) != 21:
        return False

    thumb_tip = landmarks[4]  # Tip of thumb

    # Map finger number to corresponding landmark index
    finger_tip_map = {
        2: 8,    # Index finger tip
        3: 12,   # Middle finger tip
        4: 16,   # Ring finger tip
        5: 20    # Pinky tip
    }

    # Check if the given finger number is valid
    if finger not in finger_tip_map:
        raise ValueError("finger must be one of: 2 (index), 3 (middle), 4 (ring), 5 (pinky)")

    finger_tip = landmarks[finger_tip_map[finger]]
    d = distance(thumb_tip, finger_tip)

    return d < threshold
