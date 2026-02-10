# Ici on créé la fenêtre principale de l'application
# DOC utilisé : https://customtkinter.tomschimansky.com/

import platform
import subprocess
from pathlib import Path

import customtkinter as ctk
from PIL import Image

from pdf_generator import PcScan_PDF
from system_info import SystemInfo


class PcScan:
    def __init__(self):
        # Création de la fenêtre principale
        self.root = ctk.CTk()

        # Configuration de cette fenêtre principale
        self.root.geometry("700x500")
        self.root.title(
            f"PcScan | Ordinateur : {SystemInfo().data["name"]}".center(125)
        )
        self.root.resizable(False, False)
        self.root.config(bg="#FAF7F7")

        # Mise en place de l'interface
        self.setup_ui()

    def setup_ui(self):
        # création d'une "frame" principale dans quoi on mettra les informations
        main_frame = ctk.CTkFrame(
            self.root,
            fg_color="white",
            corner_radius=15,
            bg_color="#FAF7F7",
            width=600,
            height=380,
            border_color="#f1f1f4",
            border_width=2,
        )
        main_frame.pack(padx=10, pady=25)

        # On mets en place les 5 lignes qui affichent le nom du composant(ex: CPU, GPU, RAM...)
        name = ["CPU", "GPU", "RAM", "Stockage", "OS"]
        y_place = [5, 80, 155, 230, 305]
        for components_name, coord in zip(name, y_place):
            self.row_components_name(
                main_frame,
                components_name,
                f"assets/{components_name.lower()}.png",
                coord,
            )

        # Ici les 5 lignes qui affichent le composant présent dans le système de l'utilisateur
        info = SystemInfo().data
        user_components = [
            info["cpu"],
            info["gpu"],
            info["ram"],
            info["stockage"],
            info["os"],
        ]
        for components, coord in zip(user_components, y_place):
            self.row_user_components(main_frame, f"{components}", coord)

        # Mettre la petite séparation entre chaque ligne pour le visuel
        y_list = [78, 152, 227, 302]
        for y in y_list:
            self.separation_line(main_frame, y)

        # Créer le bouton "générer le rapport PDF"
        button_pdf = ctk.CTkButton(
            self.root,
            width=350,
            height=50,
            corner_radius=15,
            bg_color="#FAF7F7",
            border_spacing=5,
            fg_color="#5394ee",
            border_color="#d8d8d8",
            border_width=1,
            text_color="white",
            text="Générer le rapport PDF",
            font=("Helvetica Neue", 19, "bold"),
            hover=True,
            hover_color="#1a58a3",
            command=self.generate_pdf,
        )
        button_pdf.pack(padx=0, pady=0)

    # Ici on créer le pdf quand l'utilisateur clique sur le bouton
    def generate_pdf(self):
        pdf = PcScan_PDF()

        # Chemin vers le bureau de l'utilisateur
        desktop = Path.home() / "Desktop"
        pdf_path = desktop / "PcScan_Report.pdf"

        # On génère le PDF sur le bureau
        pdf.output(str(pdf_path))

        # Puis on l'ouvre directement
        def open_pdf(path):
            if platform.system() == "Windows":
                subprocess.run(["cmd", "/c", "start", "", str(path)], shell=True)
            elif platform.system() == "Darwin":
                subprocess.run(["open", path])
            else:  # Linux
                subprocess.run(["xdg-open", path])

        # Puis on ouvre le PDF
        open_pdf(pdf_path)

    def row_components_name(self, parent, name, path_image, y):

        image = ctk.CTkImage(light_image=Image.open(path_image), size=(70, 70))

        # Création de la ligne qui affiche le nom du composant
        name_row = ctk.CTkLabel(
            parent,
            text=(f"{name}"),
            text_color="#6C6C6C",
            font=("Helvetica Neue", 23, "bold"),
            width=275,
            height=70,
            fg_color="white",
            anchor="w",
            compound="left",
            justify="center",
            padx="10",
            image=image,
        )
        name_row.place(x=5, y=y)
        return name_row

    def row_user_components(self, parent, name, y):

        frame_test = ctk.CTkLabel(
            parent,
            text=name,
            text_color="#6C6C6C",
            font=("Helvetica Neue", 23),
            width=310,
            height=70,
            fg_color="white",
            anchor="e",
            justify="center",
        )
        frame_test.place(x=280, y=y)

    def separation_line(self, parent, y):
        line = ctk.CTkFrame(
            parent, height=1, fg_color="#EAE9E9", width=550, corner_radius=15
        )
        line.place(x=30, y=y)

    def run(self):
        # Lancer la fenêtre principale
        self.root.mainloop()


# Lancement de la classe
if __name__ == "__main__":
    app = PcScan()
    app.run()
