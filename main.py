import cv2
import mediapipe as mp
import time
from directkeys import right_pressed, left_pressed
from directkeys import PressKey, ReleaseKey
import pyautogui


break_key_pressed = left_pressed
accelerator_key_pressed = right_pressed

time.sleep(2.0)
current_key_pressed = set()

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)



with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        keyPressed = False
        break_pressed = False
        accelerator_pressed = False
        key_count = 0
        key_pressed = 0
        ret, image = video.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        lmList = []  # Initialize lmList within the loop
        if results.multi_hand_landmarks:
            # Only considering the first detected hand
            hand_landmarks = results.multi_hand_landmarks[0]
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mp_draw.draw_landmarks(image, hand_landmarks,
                                   mp_hand.HAND_CONNECTIONS)

        fingers = []
        if len(lmList) != 0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total = fingers.count(1)

            if total == 0:
                print("Brake")
                pyautogui.keyUp('right')
                pyautogui.keyDown('left')
            elif total == 5:
                print("Gas")
                pyautogui.keyUp('left')
                pyautogui.keyDown('right')

        else:
            print("No hand detected")
            pyautogui.keyUp('left')
            pyautogui.keyUp('right')

        if not keyPressed and len(current_key_pressed) != 0:
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()
        elif key_count == 1 and len(current_key_pressed) == 2:
            key_to_release = current_key_pressed.difference(
                [key_pressed]).pop()
            ReleaseKey(key_to_release)
            current_key_pressed = {key_pressed}

        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
