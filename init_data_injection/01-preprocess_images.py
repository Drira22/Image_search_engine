import os
import cv2
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

# Dossier contenant les images à pré-traiter
input_dir = "/home/khalil/image_search_engine/data/images/"
# Dossier où sauvegarder les images pré-traitées
output_dir = "/home/khalil/image_search_engine/data/preprocessed_images/"
os.makedirs(output_dir, exist_ok=True)

# Fonction pour charger et pré-traiter une image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Redimensionner l'image à 224x224
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)  # Normalisation propre à VGG16
    return img_array

# Parcourir toutes les images du dossier
for img_file in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_file)
    try:
        processed_img = preprocess_image(img_path)
        # Sauvegarder l'image pré-traitée en fichier NumPy
        np.save(os.path.join(output_dir, img_file.split('.')[0] + ".npy"), processed_img)
        print(f"Image {img_file} prétraitée avec succès.")
    except Exception as e:
        print(f"Erreur lors du traitement de {img_file}: {str(e)}")
