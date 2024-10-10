import os
import shutil

# Définir le chemin du dossier principal
main_dir = 'data/animals'

# Extensions d'images courantes
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}

# Parcourir tous les sous-dossiers
for root, dirs, files in os.walk(main_dir):
    # Ne traiter que les sous-dossiers, ignorer le dossier principal lui-même
    if root == main_dir:
        continue
    for file in files:
        # Vérifier l'extension du fichier
        if os.path.splitext(file)[1].lower() in image_extensions:
            source = os.path.join(root, file)
            destination = os.path.join(main_dir, file)
            # Gérer les conflits de noms de fichiers
            if os.path.exists(destination):
                base, ext = os.path.splitext(file)
                counter = 1
                new_filename = f"{base}_{counter}{ext}"
                new_destination = os.path.join(main_dir, new_filename)
                while os.path.exists(new_destination):
                    counter += 1
                    new_filename = f"{base}_{counter}{ext}"
                    new_destination = os.path.join(main_dir, new_filename)
                destination = new_destination
            # Déplacer le fichier
            shutil.move(source, destination)
            print(f"Moved: {source} -> {destination}")

# Supprimer les sous-dossiers vides
for root, dirs, files in os.walk(main_dir, topdown=False):
    if root == main_dir:
        continue
    if not dirs and not files:
        os.rmdir(root)
        print(f"Deleted empty folder: {root}")

print("Tous les fichiers ont été déplacés et les sous-dossiers vides supprimés.")


# import numpy as np

# feature_vector = np.load("data/features/0aabace773.npy")  # Replace with the name of any saved feature file
# print("Feature vector shape:", feature_vector.shape)