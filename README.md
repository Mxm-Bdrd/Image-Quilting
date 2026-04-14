# Synthèse et Transfert de Textures (Image Quilting)

Ce projet est une implémentation en Python de l'algorithme d'**Image Quilting** décrit dans l'article de recherche de **Efros et Freeman (SIGGRAPH 2001)**. L'objectif est de synthétiser de grandes textures à partir d'un petit échantillon et d'appliquer ces textures sur des images cibles.

**Auteur :** Maxime Bédard  

---

## Fonctionnalités

Le projet est divisé en quatre étapes clés reflétant l'évolution de la qualité de la synthèse :

1.  **Échantillonnage Aléatoire (`quilt_random.py`)** : La méthode la plus simple qui place des blocs côte à côte sans aucune contrainte.
2.  **Chevauchement de Blocs (`quilt_simple.py`)** : Les blocs sont sélectionnés en minimisant l'erreur (SSD) dans la zone de chevauchement. Optimisé par filtrage (convolution FFT).
3.  **Recherche de Joint Optimal (`quilt_cut.py`)** : Utilisation de la programmation dynamique pour trouver un chemin de coupe minimal (Seam Carving) afin de rendre les transitions invisibles.
4.  **Transfert de Texture (`texture_transfer.py`)** : Synthèse guidée par une image cible pour recréer ses formes avec la texture source.

---

## Technologies Utilisées

* **Langage :** Python 3.14
* **Bibliothèques :**
    * `NumPy` : Manipulation matricielle intensive.
    * `SciPy` : Calcul de corrélation via `fftconvolve`.
    * `Matplotlib` : Affichage et sauvegarde des résultats.

---

## Structure du Projet

```text
.
├── quilt_random.py         # Partie 1 : Random sampling
├── quilt_simple.py         # Partie 2 : Chevauchement simple
├── quilt_cut.py            # Partie 3 : Recherche de joint
├── texture_transfer.py     # Partie 4 : Transfert de texture
├── generer_rapport.py      # Script de génération du rapport HTML
└── index.html              # Rapport final visualisant les résultats
