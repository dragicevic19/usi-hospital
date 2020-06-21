from fpdf import FPDF
import webbrowser
from model.konstante.konstante import PUTANJA_ZA_IZVESTAJ_PROSTORIJE, \
    PUTANJA_ZA_IZVESTAJ_PROSTORIJE_CITANJE, PUTANJA_ZA_IZVESTAJ_LEKARA_CITANJE, PUTANJA_ZA_IZVESTAJ_UPRAVNIK_LEKAR, \
    PUTANJA_ZA_IZVESTAJ_LEKAR_SOPSTVENI, PUTANJA_ZA_IZVESTAJ_LEKAR_SOPSTVENI_CITANJE
from repozitorijum.izvestaji.interfejs_izvestaji_repozitorijum import InterfejsIzvestajRepozitorijum


class IzvestajRepozitorijumImpl(InterfejsIzvestajRepozitorijum):

    def __init__(self):
        pass

    # tip = False - lekar, True - prostorija
    def generisi_izvestaj_upravnik(self, string_za_upis, tip_izvestaja):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10, )
        linija_u_fajlu = 1
        for recenica in string_za_upis.split("\n"):
            pdf.cell(200, 10, txt=recenica, ln=linija_u_fajlu, align="L", border=1)
            linija_u_fajlu += 1
        if tip_izvestaja:
            pdf.output(PUTANJA_ZA_IZVESTAJ_PROSTORIJE)
            webbrowser.open_new(PUTANJA_ZA_IZVESTAJ_PROSTORIJE_CITANJE)
        else:
            pdf.output(PUTANJA_ZA_IZVESTAJ_UPRAVNIK_LEKAR)
            webbrowser.open_new(PUTANJA_ZA_IZVESTAJ_LEKARA_CITANJE)

    def generisi_izvestaj_lekar(self, string_za_upis):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10, )
        linija_u_fajlu = 1
        for recenica in string_za_upis.split("\n"):
            pdf.cell(200, 10, txt=recenica, ln=linija_u_fajlu, align="L", border=1)
            linija_u_fajlu += 1
        pdf.output(PUTANJA_ZA_IZVESTAJ_LEKAR_SOPSTVENI)
        webbrowser.open_new(PUTANJA_ZA_IZVESTAJ_LEKAR_SOPSTVENI_CITANJE)
