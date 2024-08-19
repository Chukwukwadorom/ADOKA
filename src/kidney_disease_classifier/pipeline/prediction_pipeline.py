import numpy as np
from PIL import Image
import tensorflow as tf
import os

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
