import datetime
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os 
from dataclasses import asdict
import json
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

model_path = '/hand_landmarker.task'
    
if __name__ == "__main__":
    img = mp_image = mp.Image.create_from_file(os.getcwd()+'/test/twohands.jpg')

    options = HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=os.getcwd()+model_path),
        running_mode=VisionRunningMode.IMAGE,
        num_hands = 2 
    )
    with HandLandmarker.create_from_options(options) as landmarker:
        result = landmarker.detect(mp_image)
        # print(result)
        with open(datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S.json"),"a") as f:
            f.write(json.dumps(asdict(result)))
                

            
        