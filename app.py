import streamlit as st
import cv2
import os
import cam_tools as ct # cam tools

from ultralytics import YOLO

import base64 #display pdf


import mediapipe as mp
mp_hands = mp.solutions.hands


def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

if __name__ == "__main__":
    model = YOLO(os.getcwd() + "/Model/best.pt", "classify")

    st.title("""
# BYTE ASL TRANSLATOR
""")
    #intro to the streamlit
    st.write("""
    Welcome to the BYTE ASL Translator! We are BYTE's Team 4: [Add names here]. During the fall semester, 
    we used machine learning to train a YOLO model with 50 ASL words using image classification.

    **MediaPipe**:
    MediaPipe is used to identify and extract regions of interest (ROIs), specifically for hand detection. 
    It pinpoints the areas we need to focus on, and these are then fed to the YOLO model.

    **YOLO**:
    Once MediaPipe identifies the hand ROIs, YOLO is applied to those specific regions. The YOLO model we are using (V8) 
    performs the majority of the heavy lifting, such as refining bounding boxes, classifying gestures, and detecting specific 
    objects or patterns within the identified hand regions.

    This application uses computer vision and machine learning to interpret American Sign Language gestures in real time. 
    Simply start the model, and it will begin analyzing your hand gestures through your webcam. Press 'Stop' to end the session.
    """)

    
    frame_placeholder = st.empty()
    
    st.write(""" To begin using the model, press the "Run Model" button to activate your webcam, and use any of the ASL words that 
             were used to train the model. Using a word outside of the dataset will most likely result in the model not understanding 
             the words you are trying to convey. To access the list of words within the model, please click this PDF.
             """)
    start = st.button("Run Model")
    stop = st.button("Stop")
    
    
    running: bool = None
    cap = cv2.VideoCapture()

    if start and not cap.isOpened():
        cap.open(0)
        running = True

    if stop and cap.isOpened():
        running = False
        cap.release()

    with mp_hands.Hands() as hands:
        
        while running:
            frame_placeholder.image(ct.DrawImage(hands, cap, model), channels="BGR")
            
#adding pdf with the list of words used to train the model
    st.subheader("📄 View Documentation")
    pdf_file_path = os.getcwd() + "/ASL_dataset.pdf"  # Replace with your PDF file path
    show_pdf(pdf_file_path)
    



