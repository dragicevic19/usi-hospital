from repository.unos_anamneze.unos_anamneze_repozitorijum import UnosAnamnezeRepository


class UnosAnamnezeService(object):

    @staticmethod
    def dobavi_anamnezu_ulogovanog_pacijenta(pacijent):
        return UnosAnamnezeRepository.pronadji_anamnezu_za_pacijenta(pacijent)

    @staticmethod
    def dodaj_anamnezu(lekar, opis_anamneze, pacijent):
        UnosAnamnezeRepository.dodaj_anamnezu(lekar, opis_anamneze, pacijent)








