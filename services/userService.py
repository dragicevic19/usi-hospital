from model.kreiranje_objekata_entiteta import KreiranjeObjekata, lista_ucitanih_korisnika, lista_obrisanih_korisnika
from model.korisnik import Korisnik
from model.lekar import Lekar


class UserService(object):

    @staticmethod
    def dodaj_korisnika(korisnicko_ime, lozinka, ime, prezime, uloga):
        if uloga == 'lekar':
            korisnik = Lekar(korisnicko_ime, lozinka, ime, prezime)
        else:
            korisnik = Korisnik(korisnicko_ime, lozinka, ime, prezime, '', uloga)
        lista_ucitanih_korisnika.append(korisnik)
        KreiranjeObjekata.sacuvaj_entitete()

    @staticmethod
    def obrisi_korisnika(korisnicko_ime):
        korisnik = KreiranjeObjekata.postoji_korisnik(korisnicko_ime)
        korisnik._obrisan = True  # ili korisnik.set_obrisan(True)?
        lista_ucitanih_korisnika.remove(korisnik)
        lista_obrisanih_korisnika.append(korisnik)
        KreiranjeObjekata.sacuvaj_entitete()

    @staticmethod
    def azuriraj_korisnika(selektovano_k_ime, uneto_k_ime, lozinka, ime, prezime):
        korisnik = KreiranjeObjekata.postoji_korisnik(selektovano_k_ime)
        korisnik._korisnicko_ime = uneto_k_ime
        korisnik._lozinka = lozinka
        korisnik._ime = ime
        korisnik._prezime = prezime
        KreiranjeObjekata.sacuvaj_entitete()

