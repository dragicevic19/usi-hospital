from model.korisnik import Korisnik


class Upravnik(Korisnik):

    def __init__(self, korisnicko_ime=None, lozinka=None, ime=None, prezime=None, obrisan=''):
        super().__init__(korisnicko_ime, lozinka, ime, prezime, obrisan, "upravnik bolnice")


if __name__ == '__main__':
    upravnik1 = Upravnik("korisnicko12", "123")

    print(upravnik1.get_korisnicko_ime())

    upravnik1.set_ime("marko")
    print(upravnik1.get_ime())
