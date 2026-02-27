import cv2
import numpy as np
import streamlit as st
from PIL import Image

@st.cache_resource
def load_model():
    net = cv2.dnn.readNetFromCaffe(
        "model/deploy.prototxt",
        "model/res10_300x300_ssd_iter_140000.caffemodel"
    )
    return (net)

net = load_model()

st.title("Face Detector")
st.write("ResNet Model + SSD — OpenCV v3.3")
frame = st.camera_input("Camera")

if (frame is not None):
    st.image(frame, "Your Photo!")