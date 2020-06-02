from repository.kalendar.kalendar_repozitorijum import KalendarRepository


class KalendarServis():

    @staticmethod
    def vrati_zauzeca_datum_soba(datum, sprat, broj_sobe):
        return KalendarRepository.vrati_zauzeca_za_datum_i_sobu(datum, sprat, broj_sobe)


if __name__ == '__main__':
    lista = KalendarServis.vrati_zauzeca_datum_soba("6/1/2020", "3", "301")
