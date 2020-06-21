from model.kalendarski_dogadjaj import KalendarskiDogadjaj
from repozitorijum.kalendar.kalendar_repozitorijum import KalendarRepozitorijumImpl


class KalendarServis():
    def __init__(self, repo_kalendar=KalendarRepozitorijumImpl()):
        self._repo_kalendar = repo_kalendar

    def vrati_zauzeca_datum_soba(self, datum, sprat, broj_sobe):
        return self._repo_kalendar.vrati_zauzeca_za_datum_i_sobu(datum, sprat, broj_sobe)

    def dodaj_dogadjaj_ako_je_slobodna(self, renoviranjeDTO):
        if self.slobodna_prostorija_za_period(renoviranjeDTO):
            dogadjaj = KalendarskiDogadjaj(renoviranjeDTO.datum_pocetka_radova, renoviranjeDTO.vreme,
                                           renoviranjeDTO.sprat_broj_prostorije,
                                           renoviranjeDTO.broj_termina)
            self._repo_kalendar.dodaj_dogadjaj(dogadjaj)
            return True
        else:
            return False

    def slobodna_prostorija_za_period(self, renoviranjeDTO):
        if self._repo_kalendar.slobodna_prostorija_za_period(renoviranjeDTO):
            return True
        else:
            return False

    def dobavi_vremenske_slotove(self):
        return self._repo_kalendar.vrati_vremenske_slotove()

    def dobavi_listu_dogadjaja(self):
        return self._repo_kalendar.vrati_listu_dogadjaja()

    def dobavi_listu_proslih_dogadjaja(self):
        return self._repo_kalendar.vrati_listu_proslih_dogadjaja()

# if __name__ == '__main__':
#     lista = KalendarServis().vrati_zauzeca_datum_soba("6/1/2020", "3", "301")
