# feature_image_ex.py
import numpy as np
from PIL import Image
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg16 import preprocess_input

# Load the VGG16 model
base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)

def extract_features(image):
    # Resize and preprocess the image
    img_resized = image.resize((224, 224))  # Resize to 224x224
    img_array = np.array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Extract features
    features = model.predict(img_array)
    return features.flatten()  
