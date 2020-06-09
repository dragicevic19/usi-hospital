from repository.unos_anamneze.unos_anamneze_repozitorijum import lista_ucitanih_unosa_anamneza
from repository.korisnik.korisnik_repozitorijum import KorisnikRepository
from repository.unos_anamneze.unos_anamneze_repozitorijum import UnosAnamnezeRepository


class UnosAnamnezeService(object):

    @staticmethod
    def dobavi_anamnezu_ulogovanog_pacijenta(pacijent):
        return UnosAnamnezeRepository.pronadji_anamnezu_za_pacijenta(pacijent)











