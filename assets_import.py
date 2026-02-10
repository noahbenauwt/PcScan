# Ce fichier permet à PyInstaller.py d'aller chercher les images de assets/

import os 
import sys 

# Permet de gérer les assets lors de la compilation de PyInstaller
def resource_path(relative_path):
    """ Gestion des chemins pour PyInstaller """
    try:
        base_path = sys._MEIPASS #type: ignore
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

