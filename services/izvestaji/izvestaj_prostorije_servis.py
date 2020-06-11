from repository.izvestaji.izvestaji_repozitorijum import IzvestajRepozitorijum
from repository.kalendar.kalendar_repozitorijum import lista_dogadjaja, lista_proslih_dogadjaja
from datetime import datetime

from services.izvestaji.izvestaji import IzvestajServis


class IzvestajProstorijeServis(IzvestajServis):

    def __init__(self, pocetni_datum, krajnji_datum):
        self._string_za_pdf = " "
        super().__init__("prostorije", pocetni_datum, krajnji_datum)

    def pocni(self):
        self.generisanje(self._tip_izvestaja)
        print(self._mapa)
        self._string_za_pdf += self.ukupan_broj_sati_po_prostoriji()
        self._string_za_pdf += self.prosecan_broj_sati_po_prostoriji()
        self._string_za_pdf += self.prosecno_i_ukupno_sati_sve_prostorije()

        IzvestajRepozitorijum.generisi_izvestaj(self._string_za_pdf, False)

    def ukupan_broj_sati_po_prostoriji(self):
        ispis = ""
        for kljuc in self._mapa:
            ispis += "Ukupno zauzece sobe " + kljuc + " je: " + str(
                int(self._mapa[kljuc]) * 30) \
                     + " minuta \n "
        return ispis

    def prosecan_broj_sati_po_prostoriji(self):
        ispis = ""
        for kljuc in self._mapa:
            ispis += "Prosecno zauzece sobe " + kljuc + " po danu je: " \
                     + str(
                int(self._mapa[kljuc]) * 30 / self._broj_dana_za_izvestaj) \
                     + " minuta \n "
        return ispis

    def prosecno_i_ukupno_sati_sve_prostorije(self):
        return ("Ukupan broj sati u svim prostorijama je: "
                + str(
                    self._ukupan_broj_sati_zauzeca_svih) + " sati, a prosecan broj sati zauzeca je: " +
                str(
                    self._ukupan_broj_sati_zauzeca_svih / self._broj_dana_za_izvestaj) +
                " sati po danu.")
