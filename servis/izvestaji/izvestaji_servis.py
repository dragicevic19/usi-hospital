from servis.kalendar.kalendar_servis import KalendarServis
from datetime import datetime


class IzvestajServis:
    def __init__(self, tip_izvestaja, pocetni_datum, krajnji_datum):
        self._pocetni_datum_string = pocetni_datum
        self._krajnji_datum_string = krajnji_datum
        self._prosli_i_buduci_dogadjaji = KalendarServis().dobavi_listu_proslih_dogadjaja() + \
                                          KalendarServis().dobavi_listu_dogadjaja()
        self._mapa = {}  # IZMENITI
        self._string_za_pdf = " "
        self._broj_dana_za_izvestaj = 0
        self._ukupan_broj_sati_zauzeca_svih = 0
        self._tip_izvestaja = tip_izvestaja
        dan, mes, god = pocetni_datum.split("/")
        d, m, g = krajnji_datum.split("/")
        self._datum_od = datetime(int(god), int(mes), int(dan))
        self._datum_do = datetime(int(g), int(m), int(d))
        self.ukupno_termina_po_objektu(self._datum_od, self._datum_do)

    def generisanje(self, vrsta_izvestaja):  # vrsta izvestaja -> prostorija, lekar
        string_za_pdf = "IZVESTAJ ZA SVE " + vrsta_izvestaja.upper() + " OD " + self._pocetni_datum_string + " DO " \
                        + self._krajnji_datum_string + "\n\n"

        self._broj_dana_za_izvestaj = (self._datum_do - self._datum_od).days

        return string_za_pdf

    def ukupno_termina_po_objektu(self, datum_od, datum_do):
        for dogadjaj in self._prosli_i_buduci_dogadjaji:
            if datum_od <= dogadjaj.datum_vreme <= datum_do:
                self.__razvrstaj_izvestaj_po_tipu(dogadjaj)
        self._ukupan_broj_sati_zauzeca_svih /= 2

    def __razvrstaj_izvestaj_po_tipu(self, dogadjaj):
        if self._tip_izvestaja == "prostorije":
            kljuc = str(dogadjaj.sprat) + "|" + str(dogadjaj.broj_prostorije)
            self.__odredi(kljuc, dogadjaj.trajanje)
            self._ukupan_broj_sati_zauzeca_svih += dogadjaj.trajanje
        elif self._tip_izvestaja == "lekare":
            for lekar in dogadjaj.spisak_doktora:
                if len(dogadjaj.spisak_doktora) > 0:
                    self.__odredi(lekar, dogadjaj.broj_termina)
                    self._ukupan_broj_sati_zauzeca_svih += dogadjaj.broj_termina


    def __odredi(self, kljuc, broj_termina):  # PROMENITI NAZIV!
        if kljuc in self._mapa:
            self._mapa[kljuc] += broj_termina
        else:
            self._mapa[kljuc] = broj_termina
