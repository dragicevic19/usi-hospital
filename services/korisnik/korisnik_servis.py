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
    def dobavi_spisak_pacijenata_po_lekaru(ulogovani_lekar):
        lista_lekarovih_pacijenata = KorisnikRepository.vrati_spisak_pacijenata_po_lekaru(ulogovani_lekar)
        lista_objekata_pacijenata = []
        for pacijent in range(len(lista_lekarovih_pacijenata)):
            pac = KorisnikRepository.nadji_po_korisnickom_imenu(lista_lekarovih_pacijenata[pacijent])
            lista_objekata_pacijenata.append(pac)
        return lista_objekata_pacijenata

    @staticmethod
    def azuriraj_korisnika(selektovano_k_ime, uneto_k_ime, lozinka, ime, prezime):  # dto
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

    @staticmethod
    def vrati_imena_lekara(lekari):
        spisak_lekara = lekari.split(",")
        podaci_za_vracanje = ""
        for lekar in spisak_lekara:
            objekat_lekara = KorisnikRepository.nadji_po_korisnickom_imenu(lekar)
            if objekat_lekara:
                ime_i_prezime_lekara = objekat_lekara.get_ime() + " " + objekat_lekara.get_prezime()
                podaci_za_vracanje += ime_i_prezime_lekara + ", "
        return podaci_za_vracanje[:-2]  # brisemo posledji nalepljen zarez i space
