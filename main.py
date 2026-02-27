import cv2
import numpy as np
import streamlit as st
from PIL import Image

@st.cache_resource
def load_model():
    net = cv2.dnn.readNetFromCaffe(
        "models/deploy.prototxt",
        "models/res10_300x300_ssd_iter_140000.caffemodel"
    )
    return (net)

net = load_model()

st.title("Face Detector")
st.write("ResNet Model + SSD — OpenCV v3.3")
frame = st.camera_input("Camera")

if frame is not None:
    image_pil = Image.open(frame)
    frame = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    st.image(frame)