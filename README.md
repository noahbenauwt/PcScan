<div align="center">

# 🖥️ PcScan

### Scannez et documentez votre configuration système en un clic

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-lightgrey?style=for-the-badge)]()

<img src="assets/cpu.png" width="100" alt="PcScan Logo">

**Un outil simple et élégant pour scanner automatiquement votre configuration matérielle et générer un rapport PDF professionnel.**

[Fonctionnalités](#-fonctionnalités) •
[Installation](#-installation) •
[Utilisation](#-utilisation) •
[Structure](#-structure-du-projet) •
[Contributeur](#-contributeur)

</div>

---

## 📸 Aperçu

<div align="center">
  <img src="screenshots/interface.png" width="590" alt="Interface principale">
  <img src="screenshots/rapport-pdf.png" width="320" alt="Rapport PDF">
  <br>
  <p><i>Interface principale • Rapport PDF généré</i></p>
</div>

---

## ✨ Fonctionnalités

🔍 **Scan automatique** des composants système
- 🧠 **CPU** - Processeur et modèle
- 🎮 **GPU** - Carte graphique
- 💾 **RAM** - Mémoire vive installée
- 💿 **Stockage** - Type (SSD/HDD) et capacité totale
- 🖥️ **OS** - Système d'exploitation et version

📄 **Génération de rapport PDF**
- Design professionnel et épuré
- Informations détaillées et formatées
- Export direct sur le bureau
- Ouverture automatique du PDF

🎨 **Interface moderne**
- Design minimaliste avec CustomTkinter
- Icônes personnalisées pour chaque composant
- Affichage clair et organisé
- Compatibilité multi-plateforme

---

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation des dépendances

```bash
# Cloner le repository
git clone https://github.com/noahbenauwt/PcScan.git
cd PcScan

# Installer les dépendances
pip install -r requirements.txt
```

### Dépendances principales

- `customtkinter` - Interface graphique moderne
- `fpdf2` - Génération de PDF
- `Pillow` - Gestion des images
- `reportlab` - Support PDF avancé

---

## 🎯 Utilisation

### Lancer l'application

```bash
python main_window.py
```

### Utilisation de l'interface

1. **Lancement** - L'application scanne automatiquement votre système
2. **Visualisation** - Consultez vos composants dans l'interface
3. **Génération PDF** - Cliquez sur "Générer le rapport PDF"
4. **Consultation** - Le PDF s'ouvre automatiquement sur votre bureau

---

## 📁 Structure du projet

```
PcScan/
│
├── main_window.py          # Interface graphique principale
├── pdf_generator.py        # Générateur de rapport PDF
├── system_info.py          # Collecte des informations système
├── assets_import.py        # Gestion des ressources pour PyInstaller
├── requirements.txt        # Dépendances Python
│
├── assets/                 # Ressources visuelles
│   ├── cpu.png
│   ├── gpu.png
│   ├── ram.png
│   ├── stockage.png
│   ├── os.png
│   └── ok.png
│
└── PcScan-Installer.dmg   # Installateur macOS
```

---

## 🛠️ Technologies utilisées

<div align="center">

| Technologie | Utilisation |
|------------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Langage principal |
| ![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5394ee?style=flat) | Interface graphique |
| ![FPDF2](https://img.shields.io/badge/FPDF2-FF6B6B?style=flat) | Génération PDF |
| ![Pillow](https://img.shields.io/badge/Pillow-3776AB?style=flat) | Traitement d'images |

</div>

---

## 🎓 Objectifs pédagogiques

Ce projet a été développé dans un cadre d'apprentissage pour maîtriser :

- ✅ La création d'interfaces graphiques avec CustomTkinter
- ✅ La manipulation de fichiers PDF avec FPDF2
- ✅ L'utilisation de commandes système avec subprocess
- ✅ La gestion des ressources pour la compilation avec PyInstaller
- ✅ Le développement multi-plateforme (Windows, macOS, Linux)
- ✅ L'organisation et la structure d'un projet Python

---

## 💡 Fonctionnalités spécifiques par OS

### 🪟 Windows
- Utilisation de `wmic` pour récupérer les informations matérielles
- Détection automatique du type de disque (SSD/HDD)

### 🍎 macOS
- Commandes `sysctl` et `system_profiler`
- Support complet des puces Apple Silicon (M1, M2, M3, M4)

### 🐧 Linux
- Lecture de `/proc/cpuinfo` et utilisation de `lspci`
- Compatibilité avec la plupart des distributions

---

## 👨‍💻 Contributeur

<div align="center">

**Benauwt Noah**

[![GitHub](https://img.shields.io/badge/GitHub-noahbenauwt-181717?style=for-the-badge&logo=github)](https://github.com/noahbenauwt)

*Projet développé dans le cadre de l'apprentissage de Python*

</div>

---

## 📝 License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---
