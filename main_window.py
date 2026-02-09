# Ici on créé la fenêtre principale de l'application
# Api utilisé : https://customtkinter.tomschimansky.com/

import customtkinter as ctk
from PIL import Image


class PcScan:
    def __init__(self):
        # Création de la fenêtre principale
        self.root = ctk.CTk()

        # Configuration de cette fenêtre principale
        self.root.geometry("750x550")
        self.root.title("PcScan".center(172))
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
        self.row_components_name(main_frame, "CPU", "assets/cpu.png", y=5)
        self.row_components_name(main_frame, "GPU", "assets/gpu.png", y=80)
        self.row_components_name(main_frame, "RAM", "assets/ram.png", y=155)
        self.row_components_name(main_frame, "Stockage", "assets/stockage.png", y=230)
        self.row_components_name(main_frame, "OS", "assets/os.png", y=305)

        # Ici les 5 lignes qui affichent le composant présent dans le système de l'utilisateur
        self.row_user_components(main_frame, "Intel Core i7-9750H", y=5)
        self.row_user_components(main_frame, "NVIDIA GeForce GTX 1650", y=80)
        self.row_user_components(main_frame, "16 GB", y=155)
        self.row_user_components(main_frame, "SSD 512 GB", y=230)
        self.row_user_components(main_frame, "macOS Sonoma 14.4.1.1", y=305)

        # Mettre la petite séparation entre chaque ligne pour le visuel
        y_liste = [78, 152, 227, 302]
        for y in y_liste:
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
            hover_color="#1a7bf2",
        )
        button_pdf.pack(padx=0, pady=0)

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
