class Korisnik(object):

    def __init__(self, korisnicko_ime=None, lozinka=None, ime=None, prezime=None):
        self._ime = ime
        self._prezime = prezime
        self._korisnicko_ime = korisnicko_ime
        self._lozinka = lozinka

    def __str__(self):
        return "Korisnicko ime: " + self._korisnicko_ime + "\n"

    def get_korisnicko_ime(self):
        return self._korisnicko_ime

    def get_lozinka(self):
        return self._lozinka

    def get_ime(self):
        return self._ime

    def get_prezime(self):
        return self._prezime

    def set_korisnicko_ime(self, korisnicko_ime):
        self._korisnicko_ime = korisnicko_ime

    def set_lozinka(self, lozinka):
        self._lozinka = lozinka

    def set_ime(self, ime):
        self._ime = ime

    def set_prezime(self, prezime):
        self._prezime = prezime
