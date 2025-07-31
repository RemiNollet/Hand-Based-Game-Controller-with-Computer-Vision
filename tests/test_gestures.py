# tests/test_gestures.py

import pytest
from handvr import gestures

def test_is_pinch_true():
    # Simulated landmarks with thumb and index very close
    landmarks = [(0.5, 0.5, 0.0)] * 21
    landmarks[4] = (0.5, 0.5, 0.0)  # Thumb tip
    landmarks[8] = (0.505, 0.5, 0.0)  # Index tip very close
    assert gestures.is_pinch(landmarks, threshold=0.01)

def test_is_pinch_false():
    # Thumb and index far apart
    landmarks = [(0.5, 0.5, 0.0)] * 21
    landmarks[4] = (0.2, 0.5, 0.0)
    landmarks[8] = (0.8, 0.5, 0.0)
    assert not gestures.is_pinch(landmarks, threshold=0.05)