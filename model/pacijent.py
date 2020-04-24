from model.korisnik import Korisnik


class Pacijent(Korisnik):

    def __init__(self, korisnicko_ime=None, lozinka=None, ime=None, prezime=None,
                 br_zdravstvene=None, pol=None, anamneza=None):
        super().__init__(korisnicko_ime, lozinka, ime, prezime, "pacijent")
        self._br_zdravstvene = br_zdravstvene
        self._pol = pol
        self._anamneza = anamneza

    def get_br_zdravstvene(self):
        return self._br_zdravstvene

    def get_pol(self):
        return self._pol

    def get_anamneza(self):
        return self._anamneza

    def set_br_zdravstvene(self, br_zdravstvene):
        self._br_zdravstvene = br_zdravstvene

    def set_anamneza(self, anamneza):
        self._anamneza = anamneza
