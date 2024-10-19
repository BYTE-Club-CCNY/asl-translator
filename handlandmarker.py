import datetime
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os 

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

model_path = '/hand_landmarker.task'
    
if __name__ == "__main__":
    img = mp_image = mp.Image.create_from_file(os.getcwd()+'/test/a.jpg')

    options = HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=os.getcwd()+model_path),
        running_mode=VisionRunningMode.IMAGE,
        num_hands = 2 # i think some asl needs two hands?
    )
    with HandLandmarker.create_from_options(options) as landmarker:
        result = landmarker.detect(mp_image)
        print(result)
        with open(datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S.txt"),"a") as f:
            # prompt: write the results to a text file
            for idx in range(len(result.hand_landmarks)):
                hand_landmarks = result.hand_landmarks[idx]
                handedness = result.handedness[idx]
                f.write(f"Hand {idx}:\n")
                f.write(f"Handedness: {handedness[0].category_name}\n")
                for landmark_idx, landmark in enumerate(hand_landmarks):
                    f.write(f"Landmark {landmark_idx}: x={landmark.x:.4f}, y={landmark.y:.4f}, z={landmark.z:.4f}\n")
                f.write("\n")
            
        