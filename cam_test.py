import cv2 as cv
import mediapipe as mp
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

cap = cv.VideoCapture(0)


def DrawImage():
    with mp_hands.Hands() as hands:
        if cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                print("Empty frame.")

            frame.flags.writeable = False
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            results = hands.process(frame)

            

            frame.flags.writeable = True
            frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())

            return frame
        # cv.imshow('MediaPipe Hands', frame)
        


if __name__ == "__main__":
    with mp_hands.Hands() as hands:
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                print("Empty frame.")

            frame.flags.writeable = False
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            results = hands.process(frame)

            

            frame.flags.writeable = True
            frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())

            cv.imshow('MediaPipe Hands', frame)
            if cv.waitKey(1) == ord('q'):
                break
            
    cap.release()
    cv.destroyAllWindows()
