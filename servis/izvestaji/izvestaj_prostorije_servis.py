from repozitorijum.izvestaji.izvestaji_repozitorijum import IzvestajRepozitorijumImpl
from servis.izvestaji.izvestaji_servis import IzvestajServis


class IzvestajProstorijeServis(IzvestajServis):

    def __init__(self, pocetni_datum, krajnji_datum, repo_izvestaj=IzvestajRepozitorijumImpl()):
        super().__init__("prostorije", pocetni_datum, krajnji_datum)
        self._repo_izvestaj = repo_izvestaj

    def pripremi_i_izgenerisi_izvestaj(self):
        self._string_za_pdf = self.generisanje(self._tip_izvestaja)
        self._string_za_pdf += self.ukupan_broj_sati_po_prostoriji()
        self._string_za_pdf += self.prosecan_broj_sati_po_prostoriji()
        self._string_za_pdf += self.prosecno_i_ukupno_sati_sve_prostorije()

        self._repo_izvestaj.generisi_izvestaj_upravnik(self._string_za_pdf, True)

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


