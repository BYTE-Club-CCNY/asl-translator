import cv2
import mediapipe as mp
from ultralytics import YOLO

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

def DrawImage(hands, cap, show=False): # This is mostly a copy of the old code (now in name = main) except it returns the frame as an image
        if cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                print("Empty frame.")

            frame.flags.writeable = False
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame)

            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
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
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands() as hands:
        while cap.isOpened():
           DrawImage(hands, cap, show=True)

           if cv2.waitKey(1) == ord('q'):
               break

    cap.release()
    cv2.destroyAllWindows()
