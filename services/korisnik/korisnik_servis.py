from model.enum.uloga import Uloga
from model.pacijent import Pacijent
from repository.korisnik.korisnik_repozitorijum import KorisnikRepository


class KorisnikServis(object):

    @staticmethod
    def dodaj_korisnika(korisnik):
        if KorisnikRepository.nadji_po_korisnickom_imenu(korisnik._korisnicko_ime):
            return False
        KorisnikRepository.dodaj_korisnika(korisnik)
        return True

    @staticmethod
    def registracija_pacijenta(pacijent):
        novi_pacijent = Pacijent(pacijent.korisnicko_ime, pacijent.lozinka, Uloga.PACIJENT.name,
                                 pacijent.ime, pacijent.prezime, "", pacijent.broj_zdravstvene, pacijent.pol)
        KorisnikRepository.dodaj_korisnika(novi_pacijent)
        KorisnikRepository.sacuvaj_korisnike()

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

    @staticmethod
    def azuriraj_lekara(selektovano_k_ime, uneto_radno_vreme, uneti_spisak_specijalizacija):  # dto
        korisnik = KorisnikRepository.nadji_po_korisnickom_imenu(selektovano_k_ime)
        korisnik._radno_vreme = uneto_radno_vreme
        korisnik.set_spisak_specijalizacija_string(uneti_spisak_specijalizacija)

        KorisnikRepository.sacuvaj_korisnike()
