class Korisnik(object):

    def __init__(self, korisnicko_ime, lozinka, ime, prezime, obrisan, uloga):
        self._ime = ime
        self._prezime = prezime
        self._korisnicko_ime = korisnicko_ime
        self._lozinka = lozinka
        self._obrisan = obrisan
        self._uloga = uloga

    def __str__(self):
        return 'Korisnicko ime: ' + self._korisnicko_ime + '\n'

    def get_korisnicko_ime(self):
        return self._korisnicko_ime

    def get_lozinka(self):
        return self._lozinka

    def get_ime(self):
        return self._ime

    def get_prezime(self):
        return self._prezime

    def get_obrisan(self):
        return self._obrisan

    def get_uloga(self):
        return self._uloga

    def set_korisnicko_ime(self, korisnicko_ime):
        self._korisnicko_ime = korisnicko_ime

    def set_lozinka(self, lozinka):
        self._lozinka = lozinka

    def set_ime(self, ime):
        self._ime = ime

    def set_prezime(self, prezime):
        self._prezime = prezime

    def set_obrisan(self, obrisan):
        self._obrisan = obrisan

    def set_uloga(self, uloga):
        self._uloga = uloga

    def vrati_za_upis_u_fajl(self):
        return self._korisnicko_ime, self._lozinka, self._uloga, self._ime, self._prezime, self._obrisan
