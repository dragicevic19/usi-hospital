from repozitorijum.korisnik.korisnik_repozitorijum import KorisnikRepozitorijumImpl
from repozitorijum.unos_anamneze.unos_anamneze_repozitorijum_impl import UnosAnamnezeRepozitorijumImpl


class UnosAnamnezeServis(object):

    def __init__(self, repo_anamneza=UnosAnamnezeRepozitorijumImpl(), repo_korisnik=KorisnikRepozitorijumImpl()):
        self._repo_anamneza = repo_anamneza
        self._repo_korisnik = repo_korisnik

    def dobavi_anamnezu_ulogovanog_pacijenta(self, pacijent):
        return self._repo_anamneza.pronadji_anamnezu_za_pacijenta(pacijent)

    def dodaj_anamnezu_svuda(self, unos_anamneze_dto):
        self._repo_anamneza.sacuvaj_anamnezu(unos_anamneze_dto)
