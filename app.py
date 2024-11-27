import streamlit as st
import cv2

import cam_test as ct # cam tools

# import mediapipe as mp # don't know if this is needed yet

if __name__ == "__main__":
    st.write("""
# BYTE ASL TRANSLATOR
""")
    frame_placeholder = st.empty()
    running: bool = true
    while running:
        # frame_placeholder.image(ct.DrawImage(), channels="RGB")
        if st.button("Stop"):
            running = false
            break
        
        
    



