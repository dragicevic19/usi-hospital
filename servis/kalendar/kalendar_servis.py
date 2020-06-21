from model.kalendarski_dogadjaj import KalendarskiDogadjaj
from repozitorijum.kalendar.kalendar_repozitorijum import KalendarRepozitorijumImpl
from repozitorijum.notifikacije.notifikacije_repozitorijum import NotifikacijeRepozitorijum
from repozitorijum.zahtevi_za_pregled.zahtevi_za_pregled_repozitorijum import ZahtevZaPregledRepozitorijumImpl


class KalendarServis(object):
    def __init__(self, repo_kalendar=KalendarRepozitorijumImpl(),
                 repo_zahtev_za_pregled=ZahtevZaPregledRepozitorijumImpl(),
                 repo_notifikacije=NotifikacijeRepozitorijum()):

        self._repo_kalendar = repo_kalendar
        self._repo_zahtevi = repo_zahtev_za_pregled
        self._repo_notifikacije = repo_notifikacije

    def vrati_zauzeca_datum_soba(self, datum, sprat, broj_sobe):
        return self._repo_kalendar.vrati_zauzeca_za_datum_i_sobu(datum, sprat, broj_sobe)

    def dodaj_dogadjaj_ako_je_slobodna(self, dogadjajDTO):
        if self._repo_kalendar.slobodna_prostorija_za_period(dogadjajDTO):
            dogadjaj = KalendarskiDogadjaj(dogadjajDTO.datum_pocetka_radova, dogadjajDTO.vreme_pocetka_str,
                                           dogadjajDTO.sprat_broj_prostorije,
                                           dogadjajDTO.broj_termina, dogadjajDTO.lekar, dogadjajDTO.pacijent,
                                           dogadjajDTO.zahvat, dogadjajDTO.hitno)
            self._repo_kalendar.dodaj_dogadjaj(dogadjaj)
            return True
        else:
            return False

    def dobavi_vremenske_slotove(self):
        return self._repo_kalendar.vrati_vremenske_slotove()

    def dobavi_listu_dogadjaja(self):
        return self._repo_kalendar.vrati_listu_dogadjaja()

    def dobavi_listu_proslih_dogadjaja(self):
        return self._repo_kalendar.vrati_listu_proslih_dogadjaja()

    # ovo mozda u notifikacije servis?
    def posalji_notifikaciju_sekretaru(self, dogadjajDTO):
        dogadjaj = KalendarskiDogadjaj(dogadjajDTO.datum_pocetka_radova, dogadjajDTO.vreme_pocetka_str,
                                       dogadjajDTO.sprat_broj_prostorije,
                                       dogadjajDTO.broj_termina, dogadjajDTO.lekar, dogadjajDTO.pacijent,
                                       dogadjajDTO.zahvat, dogadjajDTO.hitno)
        self._repo_notifikacije.posalji_notifikaciju(dogadjaj)

    def posalji_zahtev_za_pregled_kod_specijaliste(self, zahtevDTO):
        self._repo_zahtevi.posalji_zahtev_za_pregled(zahtevDTO)

# if __name__ == '__main__':
#     lista = KalendarServis().vrati_zauzeca_datum_soba("6/1/2020", "3", "301")
