import numpy as np
from PIL import Image
import tensorflow as tf
import os
from src.kidney_disease_classifier.pipeline.prediction_pipeline import predict
import streamlit as st

# CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f0f5;
    }
    h1 {
        color: #2c3e50;
        font-family: 'Arial';
    }
    .stButton>button {
        background-color: #2c3e50;
        color: white;
        font-size: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# logo
st.image(os.path.join("assets/kidney_logo.jpg"), width=100)

# title and subtitle
st.markdown(
    """
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
        font-family: 'Arial';
    }
    .subtitle {
        font-size: 20px;
        color: #34495e;
        font-family: 'Arial';
        margin-top: -10px;
    }
    </style>
    <div>
        <h1 class="main-title">ADOKA</h1>
        <h3 class="subtitle">Automated Diagnosis of Kidney Abnormalities</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Add a sidebar
st.sidebar.title("About")
st.sidebar.info(
    """
    This app classifies kidney CT scan images into four categories:
    - Normal
    - Cyst
    - Stone
    - Tumor
    """
)

# Upload multiple files
uploaded_files = st.file_uploader("Upload kidney CT scan images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.write("### Uploaded Images and Predictions")
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        
        # Display image in the left column
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(image, caption=f'{uploaded_file.name}', use_column_width=True)
        
        # Make prediction and display it in the right column
        with col2:
            with st.spinner('Classifying...'):
                label = predict(image)
            st.success(f"Prediction: **{label}**")


