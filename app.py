import streamlit as st
import cv2

import cam_tools as ct # cam tools

import mediapipe as mp
mp_hands = mp.solutions.hands

if __name__ == "__main__":
    st.write("""
# BYTE ASL TRANSLATOR
""")
    
    frame_placeholder = st.empty()
    stop = st.button("Stop")
    start = st.button("Run Model")
    
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
            frame_placeholder.image(ct.DrawImage(hands, cap), channels="BGR")
    



