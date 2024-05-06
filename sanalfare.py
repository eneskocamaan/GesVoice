import cv2
import mediapipe as mp
import pyautogui
import time

start_time = time.time()

cap = cv2.VideoCapture(0)

screen_width, screen_height = pyautogui.size()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

difference = 0.05

hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5,max_num_hands=1)

while True:
    status, frame = cap.read()

    frame = cv2.flip(frame, 1)

    if not status:
        print("Kare Okunamadı!")

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    result = hands.process(rgb_frame)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if result.multi_hand_landmarks:
        for idx,hand_landmarks in enumerate(result.multi_hand_landmarks):
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            handedness = result.multi_handedness[idx].classification[0].label

            index4 = hand_landmarks.landmark[4]
            index5 = hand_landmarks.landmark[5]
            index8 = hand_landmarks.landmark[8]
            index9 = hand_landmarks.landmark[9]
            index11 = hand_landmarks.landmark[11]
            index12 = hand_landmarks.landmark[12]
            index16 = hand_landmarks.landmark[16]

            distance = ((index8.x - index12.x) ** 2 + (index8.y - index12.y) ** 2) ** 0.5
            distance2 = ((index12.x - index16.x) ** 2 + (index12.y - index16.y) ** 2) ** 0.5

            x = int(index8.x * screen_width)
            y = int(index8.y * screen_height)

            if handedness == 'Right':
                if index8.y < index5.y:
                    if index9.y < index12.y: 
                        pyautogui.moveTo(x+(x/30), y+(y/30))

                if index8.y < index5.y:
                    if distance < difference:
                        pyautogui.leftClick()

                if index8.y < index5.y and index12.y < index9.y:
                    if distance < difference and distance2 < difference:
                        pyautogui.rightClick()

            
            elif handedness == 'Left':
                if index8.y < index5.y:
                    if index9.y < index12.y:
                        pyautogui.scroll(40)  

                if index12.y < index11.y :
                    pyautogui.scroll(-40)


    fps = 1 / (time.time() - start_time)
    start_time = time.time()
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
