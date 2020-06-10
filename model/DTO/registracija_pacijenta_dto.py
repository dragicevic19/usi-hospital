from model.enum.uloga import Uloga


class RegistracijaPacijentaDTO(object):

    def __init__(self, korisnicko_ime, lozinka, ime, prezime, broj_zdravstvene, pol):
        self.ime = ime
        self.prezime = prezime
        self.korisnicko_ime = korisnicko_ime
        self.lozinka = lozinka
        self.broj_zdravstvene = broj_zdravstvene
        self.pol = pol
