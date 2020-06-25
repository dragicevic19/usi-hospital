from repozitorijum.izvestaji.izvestaji_repozitorijum import IzvestajRepozitorijumImpl
from repozitorijum.kalendar.kalendar_repozitorijum import KalendarRepozitorijumImpl
from repozitorijum.korisnik.korisnik_repozitorijum import KorisnikRepozitorijumImpl
from repozitorijum.notifikacije.notifikacije_repozitorijum import NotifikacijeRepozitorijumImpl
from repozitorijum.oprema.oprema_repozitorijum_impl import OpremaRepozitorijumImpl
from repozitorijum.prostorije.prostorije_repozitorijum import ProstorijeRepozitorijumImpl
from repozitorijum.unos_anamneze.unos_anamneze_repozitorijum_impl import UnosAnamnezeRepozitorijumImpl
from repozitorijum.zahtevi_za_pregled.zahtevi_za_pregled_repozitorijum import ZahtevZaPregledRepozitorijumImpl

from servis.kalendar.kalendar_servis import KalendarServis
from servis.korisnik.korisnik_servis import KorisnikServis
from servis.oprema.oprema_servis import OpremaServis
from servis.prostorije.prostorije_servis import ProstorijeServis
from servis.unos_anamneze.unos_anamneze_servis import UnosAnamnezeServis

from servis.prostorije.zauzeca_prostorija_servis import ZauzecaProstorijaServis




class Injektor:

    def __init__(self):
        self.__instaciranje_repozitorijuma()
        self.__instanciranje_servisaa()



    def __instanciranje_servisaa(self):
        self._kalendar_servis = KalendarServis(self._kalendar_repo,self._zahtevi_za_pregled_repo,self._notifikacije_repo)
        self._korisnik_servis = KorisnikServis(self._korisnik_repo)
        self._oprema_servis = OpremaServis(self._oprema_repo,self._prostorije_repo)
        self._prostorije_servis = ProstorijeServis(self._prostorije_repo,self._oprema_repo,self._kalendar_servis)
        self._unos_anamneze_servis = UnosAnamnezeServis(self._unos_anamneze_repo,self._korisnik_repo)
        self._zauzece_prostorjie_servis =ZauzecaProstorijaServis(self._kalendar_servis,self._prostorije_servis)




    def __instaciranje_repozitorijuma(self):
        self._korisnik_repo = KorisnikRepozitorijumImpl()
        self._izvestaj_repo = IzvestajRepozitorijumImpl()
        self._kalendar_repo = KalendarRepozitorijumImpl()
        self._notifikacije_repo = NotifikacijeRepozitorijumImpl()
        self._oprema_repo = OpremaRepozitorijumImpl()
        self._prostorije_repo = ProstorijeRepozitorijumImpl()
        self._unos_anamneze_repo = UnosAnamnezeRepozitorijumImpl(self._korisnik_repo)
        self._zahtevi_za_pregled_repo = ZahtevZaPregledRepozitorijumImpl()

    @property
    def zauzece_prostorjie_servis(self):
        return self._zauzece_prostorjie_servis

    @property
    def kalendar_servis(self):
        return self._kalendar_servis

    @property
    def korisnik_servis(self):
        return self._korisnik_servis

    @property
    def oprema_servis(self):
        return self._oprema_servis

    @property
    def prostorije_servis(self):
        return self._prostorije_servis

    @property
    def unos_anamneze_servis(self):
        return self._unos_anamneze_servis