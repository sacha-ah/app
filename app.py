import os
import random
import time
from PIL import Image
import streamlit as st

# 📁 Dossier contenant les images source
dossier_images = "MonProjet/Insta2"

# 📦 Extensions d'images acceptées
extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

# 📄 Liste des fichiers d'images
fichiers = [f for f in os.listdir(dossier_images) if os.path.splitext(f)[1].lower() in extensions]
if not fichiers:
    raise ValueError("Aucune image trouvée dans le dossier.")

# 📷 Chargement des images
images = [Image.open(os.path.join(dossier_images, f)) for f in fichiers]

# 🏗️ Fonction de réduction de pixel
def pixel_reduction_effect(img):
    facteur = random.uniform(0.0001, 0.05)  # facteur de réduction aléatoire
    new_w = max(1, int(img.width * facteur))
    new_h = max(1, int(img.height * facteur))
    img_small = img.resize((new_w, new_h), Image.LANCZOS)
    img_big = img_small.resize(img.size, Image.NEAREST)
    return img_big

# 🎬 Début de l'affichage Streamlit
st.set_page_config(page_title="Affichage Images", layout="wide", page_icon="🎞️")

st.title("Affichage automatique d'images modifiées")

# 📍 Espace pour afficher l'image
img_spot = st.empty()

while True:
    # Tirer une image au hasard
    img = random.choice(images)

    # 85% de chances d'appliquer un effet
    if random.random() < 0.85:
        img = pixel_reduction_effect(img)

    # Afficher l'image
    img_spot.image(img, use_column_width=True)

    # ⏳ Attendre un peu avant de changer
    time.sleep(0.4)
