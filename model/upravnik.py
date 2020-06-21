from model.korisnik import Korisnik


class Upravnik(Korisnik):

    def __init__(self, korisnicko_ime=None, lozinka=None, uloga=None, ime=None, prezime=None, obrisan=''):
        super().__init__(korisnicko_ime, lozinka, ime, prezime, obrisan, uloga)

