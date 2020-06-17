from fpdf import FPDF
import webbrowser
from model.konstante.konstante import PATH_TO_IZVESTAJ_PROSTORIJE, \
    PATH_TO_IZVESTAJ_PROSTORIJE_CITANJE_WEB, PATH_TO_IZVESTAJ_LEKARA_CITANJE_WEB, PATH_TO_IZVESTAJ_UPRAVNIK_ZA_LEKARA, \
    PATH_TO_IZVESTAJ_LEKAR_ZA_SEBE, PATH_TO_IZVESTAJ_LEKAR_ZA_SEBE_CITANJE_WEB


class IzvestajRepozitorijum:

    @staticmethod  # tip = False - lekar, True - prostorija
    def generisi_izvestaj_upravnik(string_za_upis, tip_izvestaja):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10, )
        linija_u_fajlu = 1
        for recenica in string_za_upis.split("\n"):
            pdf.cell(200, 10, txt=recenica, ln=linija_u_fajlu, align="L", border=1)
            linija_u_fajlu += 1
        if tip_izvestaja:
            pdf.output(PATH_TO_IZVESTAJ_PROSTORIJE)
            webbrowser.open_new(PATH_TO_IZVESTAJ_PROSTORIJE_CITANJE_WEB)
        else:
            pdf.output(PATH_TO_IZVESTAJ_UPRAVNIK_ZA_LEKARA)
            webbrowser.open_new(PATH_TO_IZVESTAJ_LEKARA_CITANJE_WEB)

    @staticmethod
    def generisi_izvestaj_lekar(string_za_upis):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10, )
        linija_u_fajlu = 1
        for recenica in string_za_upis.split("\n"):
            pdf.cell(200, 10, txt=recenica, ln=linija_u_fajlu, align="L", border=1)
            linija_u_fajlu += 1
        pdf.output(PATH_TO_IZVESTAJ_LEKAR_ZA_SEBE)
        webbrowser.open_new(PATH_TO_IZVESTAJ_LEKAR_ZA_SEBE_CITANJE_WEB)
