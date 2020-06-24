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


    def vrati_zauzeca_datum_lekar(self, datum, lekar):
        return self._repo_kalendar.vrati_zauzeca_za_datum_i_lekara(datum, lekar)

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

    def vrati_slobodne_termine_lekara_za_datum(self,datum,lekar):
        print(type(lekar))
        return self._repo_kalendar.vrati_slobodne_termine_lekara_za_datum(datum,lekar)

    def vrati_slotove_od_do(self,od,do):
        return  self._repo_kalendar.vrati_vremenske_slotovo_od_do(od,do)

    def da_li_lekar_radi_u_trazenim_slotovima(self, zeljeni_slotovi, lekar):
        return self._repo_kalendar.da_li_lekar_radi_u_zeljenim_slotovima(zeljeni_slotovi,lekar)