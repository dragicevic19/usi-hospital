from fpdf import FPDF
import webbrowser
from model.konstante.konstante import PATH_TO_IZVESTAJ_PROSTORIJE, PATH_TO_IZVESTAJ_LEKARA


class IzvestajRepozitorijum:

    @staticmethod  # tip = False - lekar, True - prostorija
    def generisi_izvestaj(string_za_upis, tip_izvestaja):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10, )
        linija = 1
        for recenica in string_za_upis.split("\n"):
            pdf.cell(200, 10, txt=recenica, ln=linija, align="L", border=1)
            linija += 1
        if tip_izvestaja:
            pdf.output(PATH_TO_IZVESTAJ_PROSTORIJE)
            webbrowser.open_new(r'..\..\data\izvestaj_prostorije.pdf')
        else:
            pdf.output(PATH_TO_IZVESTAJ_LEKARA)
            webbrowser.open_new(r'..\..\data\izvestaj_lekar.pdf')
