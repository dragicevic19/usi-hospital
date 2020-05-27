# from model.kreiranje_objekata_entiteta import KreiranjeObjekata, lista_ucitanih_korisnika, lista_obrisanih_korisnika
from repository.korisnik.korisnikRepository import KorisnikRepository


class UserService(object):

    @staticmethod
    def dodaj_korisnika(korisnik):
        KorisnikRepository.dodaj_korisnika(korisnik)

    @staticmethod
    def obrisi_korisnika(korisnicko_ime):
        korisnik = KorisnikRepository.nadji_po_korisnickom_imenu(korisnicko_ime)
        KorisnikRepository.obrisi_korisnika(korisnik)

    @staticmethod
    def azuriraj_korisnika(selektovano_k_ime, uneto_k_ime, lozinka, ime, prezime):  #dto
        korisnik = KorisnikRepository.nadji_po_korisnickom_imenu(selektovano_k_ime)
        korisnik._korisnicko_ime = uneto_k_ime
        korisnik._lozinka = lozinka
        korisnik._ime = ime
        korisnik._prezime = prezime
        KorisnikRepository.sacuvaj_korisnike()
