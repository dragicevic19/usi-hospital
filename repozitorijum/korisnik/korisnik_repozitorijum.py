from repozitorijum.korisnik.interfejs_korisnik_repozitorijum import InterfejsKorisnikRepo
from model.enum.recnici import *
from model.konstante.konstante import *
from pathlib import Path
import csv


class KorisnikRepozitorijumImpl(InterfejsKorisnikRepo):

    def __init__(self):
        self._lista_korisnika = []
        self._lista_obrisanih_korisnika = []
        self.ucitavanje_korisnika()

    def ucitavanje_korisnika(self):
        path = Path(PUTANJA_FAJL_KORISNICI)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                korisnik = konstruktor_po_ulozi[red[2]](*red)  # INDEX_ULOGE_KORISNIKA?
                if not korisnik.get_obrisan():
                    self._lista_korisnika.append(korisnik)
                else:
                    self._lista_obrisanih_korisnika.append(korisnik)

    def nadji_po_korisnickom_imenu(self, korisnicko_ime):
        for korisnik in self._lista_korisnika:
            if korisnik.get_korisnicko_ime() == korisnicko_ime:
                return korisnik
        return False

    def obrisi_korisnika(self, korisnik):
        korisnik._obrisan = True
        self._lista_korisnika.remove(korisnik)
        self._lista_obrisanih_korisnika.append(korisnik)
        self.sacuvaj_korisnike()

    def dodaj_korisnika(self, korisnik):
        self._lista_korisnika.append(korisnik)
        self.sacuvaj_korisnike()

    def sacuvaj_korisnike(self):
        path = Path(PUTANJA_FAJL_KORISNICI)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')

            self.__upisi_korisnike_csv(writer, self._lista_korisnika)
            self.__upisi_korisnike_csv(writer, self._lista_obrisanih_korisnika)

    def vrati_spisak_pacijenata_po_lekaru(self, ulogovan_lekar):
        for korisnik in self._lista_korisnika:
            if korisnik.get_korisnicko_ime() == ulogovan_lekar:
                return korisnik.get_spisak_pacijenata()

    @staticmethod
    def __upisi_korisnike_csv(writer, lista):
        for korisnik in lista:
            writer.writerow(korisnik.vrati_za_upis_u_fajl())

    def dodaj_id_anamneze_pacijentu(self, pacijent, id_anamneze):
        self.nadji_po_korisnickom_imenu(pacijent.get_korisnicko_ime()).dodaj_anamnezu(id_anamneze)
        self.sacuvaj_korisnike()

    def vrati_sve_korisnike_po_ulozi(self, uloga):
        pronadjeni_korisnici = []
        for korisnik in self._lista_korisnika:
            if korisnik.get_uloga() == uloga:
                pronadjeni_korisnici.append(korisnik)
        return pronadjeni_korisnici

    def vrati_listu_korisnika(self):
        return self._lista_korisnika

