from model.kalendarski_dogadjaj import KalendarskiDogadjaj
from repozitorijum.kalendar.kalendar_repozitorijum import KalendarRepozitorijum


class KalendarServis:

    @staticmethod
    def vrati_zauzeca_datum_soba(datum, sprat, broj_sobe):
        return KalendarRepozitorijum.vrati_zauzeca_za_datum_i_sobu(datum, sprat, broj_sobe)

    @staticmethod
    def dodaj_dogadjaj_ako_je_slobodna(renoviranjeDTO):
        if KalendarServis.slobodna_prostorija_za_period(renoviranjeDTO):
            dogadjaj = KalendarskiDogadjaj(renoviranjeDTO.datum_pocetka_radova, renoviranjeDTO.vreme,
                                           renoviranjeDTO.sprat_broj_prostorije,
                                           renoviranjeDTO.broj_termina)
            KalendarRepozitorijum.dodaj_dogadjaj(dogadjaj)
            return True
        else:
            return False

    @staticmethod
    def slobodna_prostorija_za_period(renoviranjeDTO):
        if KalendarRepozitorijum.slobodna_prostorija_za_period(renoviranjeDTO):
            return True
        else:
            return False


if __name__ == '__main__':
    lista = KalendarServis.vrati_zauzeca_datum_soba("6/1/2020", "3", "301")
