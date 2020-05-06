from model.korisnik import Korisnik


class Lekar(Korisnik):

    def __init__(self, korisnicko_ime=None, lozinka=None, ime=None, prezime=None,
                 radno_vreme=None, spisak_pacijenata=[], spisak_specijalizacija=[], obrisan=''):
        super().__init__(korisnicko_ime, lozinka, ime, prezime, obrisan, "lekar")
        self._spisak_specijalizacija = spisak_specijalizacija
        self._spisak_pacijenata = spisak_pacijenata
        self._radno_vreme = radno_vreme

    def get_spisak_specijalizacija(self):
        return self._spisak_specijalizacija

    def get_radno_vreme(self):
        return self._radno_vreme

    def get_spisak_pacijenata(self):
        return self._spisak_pacijenata

    def add_spisak_specijalizacija(self, specijalizacija):
        self._spisak_specijalizacija.append(specijalizacija)

    def add_spisak_pacijenata(self, pacijent):
        self._spisak_pacijenata.append(pacijent)

    def set_radno_vreme(self, radno_vreme):
        self._radno_vreme = radno_vreme

    def __str__(self):
        return self._ime + " " + self._prezime
