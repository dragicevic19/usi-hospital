from model.enum.tip_lekara import TipLekara
from model.enum.uloga import Uloga
from model.pacijent import Pacijent
from repozitorijum.korisnik.korisnik_repozitorijum import KorisnikRepozitorijum


class KorisnikServis(object):

    @staticmethod
    def dodaj_korisnika(korisnik):
        if KorisnikRepozitorijum.nadji_po_korisnickom_imenu(korisnik._korisnicko_ime):
            return False
        KorisnikRepozitorijum.dodaj_korisnika(korisnik)
        return True

    @staticmethod
    def registracija_pacijenta(pacijent):
        novi_pacijent = Pacijent(pacijent.korisnicko_ime, pacijent.lozinka, Uloga.PACIJENT.name,
                                 pacijent.ime, pacijent.prezime, "", pacijent.broj_zdravstvene, pacijent.pol)
        KorisnikRepozitorijum.dodaj_korisnika(novi_pacijent)
        KorisnikRepozitorijum.sacuvaj_korisnike()

    @staticmethod
    def obrisi_korisnika(korisnicko_ime):
        korisnik = KorisnikRepozitorijum.nadji_po_korisnickom_imenu(korisnicko_ime)
        KorisnikRepozitorijum.obrisi_korisnika(korisnik)

    @staticmethod
    def dobavi_spisak_pacijenata_po_lekaru(ulogovani_lekar):
        lista_lekarovih_pacijenata = KorisnikRepozitorijum.vrati_spisak_pacijenata_po_lekaru(ulogovani_lekar)
        lista_objekata_pacijenata = []
        for korisnicko_ime in lista_lekarovih_pacijenata:
            pacijent = KorisnikRepozitorijum.nadji_po_korisnickom_imenu(korisnicko_ime)
            lista_objekata_pacijenata.append(pacijent)
        return lista_objekata_pacijenata

    @staticmethod
    def azuriraj_korisnika(selektovano_k_ime, uneto_k_ime, lozinka, ime, prezime):  # dto
        korisnik = KorisnikRepozitorijum.nadji_po_korisnickom_imenu(selektovano_k_ime)
        korisnik._korisnicko_ime = uneto_k_ime
        korisnik._lozinka = lozinka
        korisnik._ime = ime
        korisnik._prezime = prezime
        KorisnikRepozitorijum.sacuvaj_korisnike()

    @staticmethod
    def azuriraj_lekara(selektovano_k_ime, uneto_radno_vreme, uneti_spisak_specijalizacija):  # dto
        korisnik = KorisnikRepozitorijum.nadji_po_korisnickom_imenu(selektovano_k_ime)
        korisnik._radno_vreme = uneto_radno_vreme
        korisnik.set_spisak_specijalizacija_string(uneti_spisak_specijalizacija)

        KorisnikRepozitorijum.sacuvaj_korisnike()

    @staticmethod
    def vrati_imena_lekara(lekari):
        spisak_lekara = lekari.split(",")
        podaci_za_vracanje = ""
        for lekar in spisak_lekara:
            objekat_lekara = KorisnikRepozitorijum.nadji_po_korisnickom_imenu(lekar)
            if objekat_lekara:
                ime_i_prezime_lekara = objekat_lekara.get_ime() + " " + objekat_lekara.get_prezime()
                podaci_za_vracanje += ime_i_prezime_lekara + ", "
        return podaci_za_vracanje[:-2]  # brisemo posledji nalepljen zarez i space

    @staticmethod
    def vrati_sve_korisnike_po_ulozi(uloga):
        return KorisnikRepozitorijum.vrati_sve_korisnike_po_ulozi(uloga)

    @staticmethod
    def vrati_korisnika_po_korisnickom_imenu(korisnicko_ime):
        return KorisnikRepozitorijum.nadji_po_korisnickom_imenu(korisnicko_ime)

    @staticmethod
    def pronadji_pacijenta(korisnicko_ime):
        lista_pronadjenih = []
        lista_svih_pacijenata = KorisnikRepozitorijum.vrati_sve_korisnike_po_ulozi(Uloga.PACIJENT.name)
        for pacijent in lista_svih_pacijenata:
            if pacijent.get_korisnicko_ime() == korisnicko_ime:
                lista_pronadjenih.append(pacijent)
        return lista_pronadjenih

    @staticmethod
    def vrati_lekare_specijaliste_ili_lop(tip_lekara):
        pronadjeni_lekari = []
        svi_lekari = KorisnikRepozitorijum.vrati_sve_korisnike_po_ulozi(Uloga.LEKAR.name)
        for lekar in svi_lekari:
            if tip_lekara == TipLekara.SPECIJALISTA:
                if lekar.get_uloga() != TipLekara.LOP.value:
                    pronadjeni_lekari.append(lekar)
            elif lekar.get_uloga() == TipLekara.LOP.value:
                pronadjeni_lekari.append(lekar)

        return pronadjeni_lekari
