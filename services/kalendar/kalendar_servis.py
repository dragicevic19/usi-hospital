from model.kalendarski_dogadjaj import KalendarskiDogadjaj
from repository.kalendar.kalendar_repozitorijum import KalendarRepository


class KalendarServis:

    @staticmethod
    def vrati_zauzeca_datum_soba(datum, sprat, broj_sobe):
        return KalendarRepository.vrati_zauzeca_za_datum_i_sobu(datum, sprat, broj_sobe)

    @staticmethod
    def dodaj_dogadjaj_ako_je_slobodna(prostorijaDTO):
        if KalendarServis.slobodna_prostorija_za_period(prostorijaDTO.datum_pocetkaDate,
                                                        prostorijaDTO.datum_zavrsetkaDate):

            dogadjaj = KalendarskiDogadjaj(prostorijaDTO.datum_pocetka_radova, prostorijaDTO.vreme,
                                           prostorijaDTO.prostorija,
                                           prostorijaDTO.broj_termina)
            KalendarRepository.dodaj_dogadjaj(dogadjaj)
            return True
        else:
            return False

    @staticmethod
    def slobodna_prostorija_za_period(datum_pocetka, datum_zavrsetka):
        if KalendarRepository.slobodna_prostorija_za_period(datum_pocetka, datum_zavrsetka):
            return True
        else:
            return False


if __name__ == '__main__':
    lista = KalendarServis.vrati_zauzeca_datum_soba("6/1/2020", "3", "301")
