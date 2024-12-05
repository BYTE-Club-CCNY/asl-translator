import cv2
import mediapipe as mp
from ultralytics import YOLO
import cvzone

import math
import os
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

def DrawImage(hands, cap,model, show=False ): # This is mostly a copy of the old code (now in name = main) except it returns the frame as an image
        if cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                print("Empty frame.")

            frame.flags.writeable = False
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            

            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
           
            results = model.track(frame, stream=True)
            
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    w, h = x2-x1, y2-y1
                    cvzone.cornerRect(frame, (x1, y1, w, h))

                    conf = math.ceil((box.conf[0]*100))/100

                    cls = box.cls[0]
                    name = r.names[int(cls)]
                    # print('name:', name)

                    cvzone.putTextRect(frame, f'{name} 'f'{conf}', (max(0,x1), max(35,y1)), scale = 0.5)
            results = hands.process(frame)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())
            if show:
                cv2.imshow('MediaPipe Hands', frame)
            return frame       

if __name__ == "__main__":
    model = YOLO(os.getcwd() + "/Model/best.pt", "classify")
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands() as hands:
        while cap.isOpened():
           DrawImage(hands, cap,model, show=True, )

           if cv2.waitKey(1) == ord('q'):
               break

    cap.release()
    cv2.destroyAllWindows()
