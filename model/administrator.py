from model.korisnik import Korisnik


class Administrator(Korisnik):

    def __init__(self, korisnicko_ime=None, lozinka=None, ime=None, prezime=None):
        super().__init__(korisnicko_ime, lozinka, ime, prezime)
