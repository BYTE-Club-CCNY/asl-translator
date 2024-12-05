# Sign Tuah
## ASL Translator


Welcome to the BYTE ASL Translator! This project was developed by BYTE's Team 4 during the fall semester to use machine learning for interpreting American Sign Language (ASL) gestures in real-time. Below, you'll find an overview of the project, team members, and instructions on how to use the application.

---

## **Project Overview**

### **MediaPipe Integration**
MediaPipe is employed to identify and extract Regions of Interest (ROIs) within the video feed, specifically focusing on hand detection. This process isolates the hand regions that are essential for gesture recognition.

### **YOLO Model**
The YOLO model (Version 8) is applied to the ROIs identified by MediaPipe. It performs the following tasks:
- Refines bounding boxes around gestures.
- Classifies ASL gestures.
- Detects patterns within the hand regions.

By combining **MediaPipe** and **YOLO**, this application provides accurate recognition of ASL gestures in real-time.

---

## **How to Use**

### **Features**
- **Real-Time Gesture Recognition**: Activate your webcam and display ASL gestures to the camera. The model will recognize and classify them.
- **PDF Documentation**: Access a list of ASL words used for training the model.

### **Steps**
1. **Run the Application**: Press the "Run Model" button to start the webcam feed.
2. **Use ASL Gestures**: Show any of the 50 ASL gestures from the training dataset to the camera.
3. **Stop the Application**: Press the "Stop" button to end the session.
4. **View Documentation**: Use the provided link to access the PDF with the list of recognized gestures.

---

## **Team Members**
- **Aaron James**  
  [LinkedIn Profile](https://www.linkedin.com/in/jamesa329/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

- **Wesley Pilamunga**  
  [LinkedIn Profile](https://www.linkedin.com/in/wesley-pilamunga-911785295/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)

- **Hamim Sean**  
  [LinkedIn Profile](https://www.linkedin.com/in/hamim-seam-07276128a/)

- **Tanzania Sumona**  
  [LinkedIn Profile](https://www.linkedin.com/in/tanzina-sumona-7aa932225/)

- **Mentor/Overseer: Baljinder Hothi**
  [LinkedIn Profile](https://www.linkedin.com/in/baljinder-hothi/)

---

## **Technical Details**

### **Requirements**
- Python
- Streamlit
- OpenCV
- MediaPipe
- YOLO (Ultralytics)

### **File Structure**
- **`cam_tools.py`**: Contains utility functions for handling camera feeds and drawing on images.
- **`Model/best.pt`**: YOLO model trained with 50 ASL words.
- **`ASL_dataset.pdf`**: Documentation listing the gestures in the dataset.

---

## **Usage Instructions**
### Running the Application
1. Clone this repository.
2. Install the required dependencies.
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
4. Follow the on-screen instructions to start the model, use the gestures, and view the documentation.

---

## **Future Improvements**
- Add more ASL gestures to the dataset.
- Optimize model performance for real-time applications.
- Improve the deployment on Streamlit or on a Linux Based Server(BYTE Team 1)

---

Thank you for using the BYTE ASL Translator! If you encounter any issues or have suggestions, feel free to open an issue or submit a pull request.
