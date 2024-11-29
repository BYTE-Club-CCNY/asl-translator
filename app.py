import streamlit as st
import cv2

import cam_test as ct # cam tools

# import mediapipe as mp # don't know if this is needed yet

if __name__ == "__main__":
    st.write("""
# BYTE ASL TRANSLATOR
""")
    frame_placeholder = st.empty()
    stop = st.button("Stop")
    running: bool = True
    while running:
        frame_placeholder.image(ct.DrawImage(), channels="RGB")
        if stop:
            running = False
            # break
        
        
    



