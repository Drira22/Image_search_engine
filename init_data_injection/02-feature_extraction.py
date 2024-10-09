import os
import numpy as np
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model

# Dossier contenant les images pré-traitées
input_dir = "/home/khalil/image_search_engine/data/preprocessed_images/"
# Dossier pour sauvegarder les vecteurs de features
output_dir = "/home/khalil/image_search_engine/data/features/"
os.makedirs(output_dir, exist_ok=True)

# Charger le modèle VGG16 pré-entraîné sur ImageNet, sans la dernière couche de classification
base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)  # 'fc1' donne un vecteur de 4096 dimensions

# Fonction pour extraire les features d'une image
def extract_features(img_array):
    features = model.predict(img_array)
    return features

# Parcourir les fichiers NumPy des images pré-traitées
for img_file in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_file)
    try:
        img_array = np.load(img_path)
        features = extract_features(img_array)
        # Sauvegarder les features
        np.save(os.path.join(output_dir, img_file), features)
        print(f"Features extraites pour {img_file}.")
    except Exception as e:
        print(f"Erreur lors de l'extraction des features pour {img_file}: {str(e)}")
