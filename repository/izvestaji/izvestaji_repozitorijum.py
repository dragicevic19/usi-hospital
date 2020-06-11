from fpdf import FPDF
import webbrowser


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
            pdf.output("../../data/izvestaj_prostorije.pdf")
            webbrowser.open_new(r'..\..\data\izvestaj_prostorije.pdf')
        else:
            pdf.output("../../data/izvestaj_lekar.pdf")
            webbrowser.open_new(r'..\..\data\izvestaj_lekar.pdf')