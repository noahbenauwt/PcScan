# Création du PDF imprimable de la liste des composants de l'ordi
# Doc utilisé : https://py-pdf.github.io/fpdf2/

from fpdf import FPDF

from system_info import SystemInfo


# Création du PDF
class PcScan_PDF(FPDF):
    def __init__(self):
        # Mise en place de sa forme
        super().__init__(orientation="P", format="A5")
        self.setup()

    # Mise en place du haut de la page
    def header(self):

        # Titre "PcScan" en haut
        self.set_font("Helvetica", "", size=27)
        self.set_y(10)
        self.set_text_color(88, 88, 88)
        self.cell(
            0,
            25,
            "PcScan",
            align="C",
            new_y="NEXT",
            link="https://github.com/noahbenauwt/PcScan",
        )

        # Sous-titre "Rapport Système" juste en dessous
        self.set_font("Helvetica", "", size=17)
        self.set_y(23)
        self.set_text_color(163, 163, 163)
        self.cell(
            0,
            20,
            f"Rapport Système : {SystemInfo().data["name"]}",
            align="C",
            new_y="NEXT",
        )

        # Ligne de séparation
        line_w = 126
        x = (self.w - line_w) / 2
        self.set_line_width(0.1)
        self.set_draw_color(170, 170, 170)
        self.line(x, 42, x + line_w, 42)

    def components_list(self):

        # Texte "configuration détectée"
        self.set_font("Helvetica", "", size=13)
        self.set_y(44)
        self.set_text_color(88, 88, 88)
        self.cell(0, 15, "Configuration détectée", align="L", new_y="NEXT")

        # Mise en place des 5 lignes de composants
        name = ["CPU", "GPU", "RAM", "Stockage", "OS"]
        y_name_list = [58, 78, 98, 118, 138]

        for components, y in zip(name, y_name_list):
            self.set_font("Helvetica", "", size=15)
            self.set_xy(29, y)
            self.set_text_color(88, 88, 88)
            self.write(15, components)

        info = SystemInfo().data
        user_components = [
            info["cpu"],
            info["gpu"],
            info["ram"],
            info["stockage"],
            info["os"],
        ]

        # Mise en place de la liste des composants de l'ordinateur de l'utilisateur
        for components_user, y in zip(user_components, y_name_list):
            self.set_font("Helvetica", "", size=15)
            self.set_xy(50, y)
            self.set_text_color(115, 115, 115)
            self.cell(0, 15, components_user, align="R")

        # Mise en place de la petite ligne de séparation
        y_line_list = [75, 95, 115, 135, 155]
        for line in y_line_list:
            line_w = 126
            x = (self.w - line_w) / 2
            self.set_line_width(0.1)
            self.set_draw_color(170, 170, 170)
            self.line(x, line, x + line_w, line)

        # Ajouter les images
        images_list = ["cpu", "gpu", "ram", "stockage", "os"]

        for y_img, imgs in zip(y_name_list, images_list):
            self.image(f"assets/{imgs}.png", 10, y_img - 2, 19, 19)

    def infos(self):
        # Texte "scan automatique"
        self.set_font("Helvetica", "", size=13)
        self.set_xy(25, 155)
        self.set_text_color(180, 180, 180)
        self.write(14, "Scan automatique")
        self.image("assets/ok.png", 13.5, 157, 15, 9)

        # Texte "Données système réelles"
        self.set_font("Helvetica", "", size=13)
        self.set_xy(80, 155)
        self.set_text_color(180, 180, 180)
        self.write(14, "Données système réelles")
        self.image("assets/ok.png", 68.5, 157, 15, 9)

        # Petite ligne de séparation vers le footer
        line_w = 126
        x = (self.w - line_w) / 2
        self.set_line_width(0.1)
        self.set_draw_color(170, 170, 170)
        self.line(x, 168, x + line_w, 168)

    def footer(self):

        # Texte "Généré par PcScan"
        self.set_font("Helvetica", "", size=21)
        self.set_y(170)
        self.set_text_color(140, 140, 140)
        self.cell(
            0,
            21,
            "Généré par PcScan",
            align="C",
            new_y="NEXT",
            link="https://github.com/noahbenauwt/PcScan",
        )

        # Texte de signature "Par Benauwt Noah"
        self.set_font("Helvetica", "", size=15)
        self.set_y(180)
        self.set_text_color(145, 145, 145)
        self.cell(
            0,
            15,
            "par Benauwt Noah",
            align="C",
            new_y="NEXT",
            link="https://github.com/noahbenauwt",
        )

        # Phrase de fin "Informations collectées automatiquement le depuis le systeme d'exploitation."
        self.set_font("Helvetica", "", size=14)
        self.set_y(194)
        self.set_text_color(175, 175, 175)
        self.multi_cell(
            0,
            6,
            """      Informations collectées automatiquement le depuis 
                           le systeme d'exploitation.""",
            "J",
        )

    def setup(self):
        self.add_page()
        self.components_list()
        self.infos()
