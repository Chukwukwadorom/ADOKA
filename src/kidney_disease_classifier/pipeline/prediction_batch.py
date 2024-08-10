import os
import numpy as np
import streamlit as st
from PIL import Image
import tensorflow as tf

# Loading the model
model = tf.keras.models.load_model(os.path.join("artifacts", "training", "model.h5"))

# Define the classes
classes = ['Cyst', 'Normal', 'Stone', 'Tumor']

def predict(image):
    # Convert PIL image to TensorFlow Tensor
    image = tf.convert_to_tensor(np.array(image))
    
    # Preprocess the image
    image = tf.image.resize(image, [224, 224])
    image = image / 255.0
    image = tf.expand_dims(image, axis=0)
    
    # Predict the class
    predictions = model.predict(image)
    return classes[np.argmax(predictions)]

# Add custom CSS
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

# Add a logo or title
st.image(os.path.join(os.path.dirname(__file__), "../../../assets/kidney_logo.jpg"), width=100)

# Custom title with subtitle
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
