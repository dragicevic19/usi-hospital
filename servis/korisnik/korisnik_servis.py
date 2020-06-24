from model.enum.tip_lekara import TipLekara
from model.enum.uloga import Uloga
from model.pacijent import Pacijent
from repozitorijum.korisnik.korisnik_repozitorijum import KorisnikRepozitorijumImpl


class KorisnikServis(object):

    def __init__(self, repo_korisnik=KorisnikRepozitorijumImpl()):
        self._repo_korisnik = repo_korisnik

    def dodaj_korisnika(self, korisnik):
        if self._repo_korisnik.nadji_po_korisnickom_imenu(korisnik._korisnicko_ime):
            return False
        self._repo_korisnik.dodaj_korisnika(korisnik)
        return True

    def registracija_pacijenta(self, pacijent):
        novi_pacijent = Pacijent(pacijent.korisnicko_ime, pacijent.lozinka, Uloga.PACIJENT.name,
                                 pacijent.ime, pacijent.prezime, "", pacijent.broj_zdravstvene, pacijent.pol)
        self._repo_korisnik.dodaj_korisnika(novi_pacijent)
        self._repo_korisnik.sacuvaj_korisnike()

    def obrisi_korisnika(self, korisnicko_ime):
        korisnik = self._repo_korisnik.nadji_po_korisnickom_imenu(korisnicko_ime)
        self._repo_korisnik.obrisi_korisnika(korisnik)

    def dobavi_spisak_pacijenata_po_lekaru(self, ulogovani_lekar):
        lista_lekarovih_pacijenata = self._repo_korisnik.vrati_spisak_pacijenata_po_lekaru(ulogovani_lekar)
        lista_objekata_pacijenata = []
        for pacijent in range(len(lista_lekarovih_pacijenata)):
            pac = self._repo_korisnik.nadji_po_korisnickom_imenu(lista_lekarovih_pacijenata[pacijent])
            lista_objekata_pacijenata.append(pac)
        return lista_objekata_pacijenata

    def azuriraj_korisnika(self, selektovano_k_ime, uneto_k_ime, lozinka, ime, prezime):  # dto
        korisnik = self._repo_korisnik.nadji_po_korisnickom_imenu(selektovano_k_ime)
        korisnik._korisnicko_ime = uneto_k_ime
        korisnik._lozinka = lozinka
        korisnik._ime = ime
        korisnik._prezime = prezime
        self._repo_korisnik.sacuvaj_korisnike()

    def azuriraj_lekara(self, selektovano_k_ime, uneto_radno_vreme, uneti_spisak_specijalizacija):  # dto
        korisnik = self._repo_korisnik.nadji_po_korisnickom_imenu(selektovano_k_ime)
        korisnik._radno_vreme = uneto_radno_vreme
        korisnik.set_spisak_specijalizacija_string(uneti_spisak_specijalizacija)

        self._repo_korisnik.sacuvaj_korisnike()

    def vrati_imena_lekara(self, lekari):
        spisak_lekara = lekari.split(",")
        podaci_za_vracanje = ""
        for lekar in spisak_lekara:
            objekat_lekara = self._repo_korisnik.nadji_po_korisnickom_imenu(lekar)
            if objekat_lekara:
                ime_i_prezime_lekara = objekat_lekara.get_ime() + " " + objekat_lekara.get_prezime()
                podaci_za_vracanje += ime_i_prezime_lekara + ", "
        return podaci_za_vracanje[:-2]  # brisemo posledji nalepljen zarez i space

    def pronadji_korisnika_po_korisnickom_imenu(self, korisnicko_ime):
        return self._repo_korisnik.nadji_po_korisnickom_imenu(korisnicko_ime)

    def dobavi_sve_korisnike_u_sistemu(self):
        return self._repo_korisnik.vrati_listu_korisnika()

    def vrati_sve_korisnike_po_ulozi(self, uloga):
        return self._repo_korisnik.vrati_sve_korisnike_po_ulozi(uloga)

    def pronadji_pacijenta(self, korisnicko_ime):
        lista_pronadjenih = []
        lista_svih_pacijenata = self._repo_korisnik.vrati_sve_korisnike_po_ulozi(Uloga.PACIJENT.name)
        for pacijent in lista_svih_pacijenata:
            if pacijent.get_korisnicko_ime() == korisnicko_ime:
                lista_pronadjenih.append(pacijent)
        return lista_pronadjenih

    def vrati_lekare_specijaliste_ili_lop(self, tip_lekara):
        pronadjeni_lekari = []
        svi_lekari = self._repo_korisnik.vrati_sve_korisnike_po_ulozi(Uloga.LEKAR.name)
        for lekar in svi_lekari:
            if tip_lekara == TipLekara.SPECIJALISTA:
                if lekar.get_spisak_specijalizacija()[0] and lekar.get_spisak_specijalizacija()[0] != TipLekara.LOP.value:
                    pronadjeni_lekari.append(lekar)
            elif lekar.get_spisak_specijalizacija()[0] == TipLekara.LOP.value:
                pronadjeni_lekari.append(lekar)

        return pronadjeni_lekari
