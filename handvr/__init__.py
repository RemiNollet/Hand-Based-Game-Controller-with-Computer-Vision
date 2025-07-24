# main.py
# Lance le pipeline : webcam → détection → action

# detector.py
# Initialise et gère Mediapipe (retourne les landmarks)

# gestures.py
# Détecte des gestes spécifiques à partir des landmarks

# mouse_control.py
# Utilise pyautogui ou pynput pour bouger la souris

# keyboard_control.py
# Simule des touches via keyboard ou pynput

# controller.py
# Supervise les autres modules pour activer les bonnes actions

# config.py
# Centralise les réglages : seuils, ID landmarks, mapping gestes/touches

# test_*.py
# Vérifie que chaque module se comporte comme attendu
