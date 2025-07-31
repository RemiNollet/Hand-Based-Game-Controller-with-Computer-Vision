# 🎮 Hand-Based Game Controller with Computer Vision

This project explores how computer vision and hand gesture recognition can be used to **control a game** with only a webcam — no VR headset or physical controller required.

Inspired by gesture-based interaction and virtual reality systems, I wanted to build an **intuitive control interface** where:
- My **right hand controls the mouse**
- My **left hand triggers keyboard actions**
- Simple **gestures replace clicks and keypresses**

---

## Objective

Create a system that allows **hands-only control** of video games using a webcam:
- Map **hand landmarks** to cursor movements and keypresses
- Use **Mediapipe** for real-time hand tracking
- Simulate input events using Python libraries
- Target use-case: playing games like **Minecraft** or **League of Legends**

---

## How it works

| Feature                         | Description                                                 |
|----------------------------------|-------------------------------------------------------------|
| 🖐️ Hand Detection               | Detect hands and 21 landmarks using Mediapipe               |
| 🖱️ Mouse Control               | Move mouse with the right hand                      |
| 👌 Gesture-to-Click Mapping     | Pinch gesture (thumb + index) → right click                |
| ⌨️ Keyboard Trigger via Gestures| Left hand performs static gestures to simulate keypresses  |


---

## 📽️ Demo

*To be added — planned gameplay demo controlled via webcam gestures.*

---
## ✅ Testing

This project includes unit tests to ensure core functionalities like gesture detection and system actions are working correctly.

### What is tested?

- Pinch gesture detection and open-palm logic (`gestures.py`)
- Mouse movement conversion and click simulation (`mouse_control.py`)
- Keyboard press actions (`keyboard_control.py`)
- Gesture-to-action mapping logic (`controller.py`)

### How to run tests locally

Make sure you have `pytest` installed*

```bash
pytest -v
```

---

## What I Learned

- Real-time computer vision pipeline with webcam
- Precision challenges in gesture recognition
- Gesture design for input simulation
- Use cases of Mediapipe for creative interfaces
- Limitations and latency in controlling fast-paced games via vision

---

## Author

Rémi Nollet – Freelance Computer Vision Engineer \
I build custom AI solutions and real-time vision systems. \
[LinkedIn](www.linkedin.com/in/remi-nollet)

## LICENSE
This project is open for review and demonstration purposes only. \
All source code rights are reserved by the author. \
