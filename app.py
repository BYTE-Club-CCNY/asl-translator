import streamlit as st
import cv2

import cam_test as ct # cam tools

import mediapipe as mp
mp_hands = mp.solutions.hands

if __name__ == "__main__":
    st.write("""
# BYTE ASL TRANSLATOR
""")
    
    frame_placeholder = st.empty()
    stop = st.button("Stop")
    running: bool = True
    with mp_hands.Hands() as hands:
        while running:
            frame_placeholder.image(ct.DrawImage(hands), channels="RGB")
            if stop:
                running = False
                # break
        
hands.close()
    



