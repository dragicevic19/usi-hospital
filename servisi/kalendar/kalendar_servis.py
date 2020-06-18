from model.kalendarski_dogadjaj import KalendarskiDogadjaj
from repozitorijum.kalendar.kalendar_repozitorijum import KalendarRepozitorijum
from repozitorijum.notifikacije.notifikacije_repozitorijum import NotifikacijeRepozitorijum


class KalendarServis:

    @staticmethod
    def vrati_zauzeca_datum_soba(datum, sprat, broj_sobe):
        return KalendarRepozitorijum.vrati_zauzeca_za_datum_i_sobu(datum, sprat, broj_sobe)

    @staticmethod
    def dodaj_dogadjaj_ako_je_slobodna(dogadjajDTO):
        if KalendarRepozitorijum.slobodna_prostorija_za_period(dogadjajDTO):
            dogadjaj = KalendarskiDogadjaj(dogadjajDTO.datum_pocetka_radova, dogadjajDTO.vreme_pocetka_str,
                                           dogadjajDTO.sprat_broj_prostorije,
                                           dogadjajDTO.broj_termina, dogadjajDTO.lekar, dogadjajDTO.pacijent,
                                           dogadjajDTO.zahvat, dogadjajDTO.hitno)
            KalendarRepozitorijum.dodaj_dogadjaj(dogadjaj)
            return True
        else:
            return False

    # @staticmethod
    # def slobodna_prostorija_za_period(dogadjajDTO):
    #     if KalendarRepozitorijum.slobodna_prostorija_za_period(dogadjajDTO):
    #         return True
    #     else:
    #         return False

    @staticmethod
    def posalji_notifikaciju_sekretaru(dogadjajDTO):
        dogadjaj = KalendarskiDogadjaj(dogadjajDTO.datum_pocetka_radova, dogadjajDTO.vreme_pocetka_str,
                                       dogadjajDTO.sprat_broj_prostorije,
                                       dogadjajDTO.broj_termina, dogadjajDTO.lekar, dogadjajDTO.pacijent,
                                       dogadjajDTO.zahvat, dogadjajDTO.hitno)
        NotifikacijeRepozitorijum.posalji_notifikaciju(dogadjaj)


if __name__ == '__main__':
    lista = KalendarServis.vrati_zauzeca_datum_soba("6/1/2020", "3", "301")
