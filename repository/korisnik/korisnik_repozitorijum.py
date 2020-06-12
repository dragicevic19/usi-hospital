import csv

from model.enum.recnici import *
from model.enum.uloga import Uloga
from model.konstante.konstante import *
from pathlib import Path

lista_ucitanih_korisnika = []
lista_obrisanih_korisnika = []
INDEX_ULOGE_KORISNIKA = 2


class KorisnikRepository:

    @staticmethod
    def ucitavanje_korisnika():
        path = Path(PATH_TO_KORISNICI)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                korisnik = konstruktor_po_ulozi[red[2]](*red)
                if not korisnik.get_obrisan():
                    lista_ucitanih_korisnika.append(korisnik)
                else:
                    lista_obrisanih_korisnika.append(korisnik)

    @staticmethod
    def nadji_po_korisnickom_imenu(korisniko_ime):
        for korisnik in lista_ucitanih_korisnika:
            if korisnik.get_korisnicko_ime() == korisniko_ime:
                return korisnik
        return False

    @staticmethod
    def obrisi_korisnika(korisnik):
        korisnik._obrisan = True
        lista_ucitanih_korisnika.remove(korisnik)
        lista_obrisanih_korisnika.append(korisnik)
        KorisnikRepository.sacuvaj_korisnike()

    @staticmethod
    def dodaj_korisnika(korisnik):
        lista_ucitanih_korisnika.append(korisnik)
        KorisnikRepository.sacuvaj_korisnike()

    @staticmethod
    def sacuvaj_korisnike():
        path = Path(PATH_TO_KORISNICI)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')

            KorisnikRepository.__upisi_korisnike_csv(writer, lista_ucitanih_korisnika)
            KorisnikRepository.__upisi_korisnike_csv(writer, lista_obrisanih_korisnika)

    @staticmethod
    def vrati_spisak_pacijenata_po_lekaru(ulogovan_lekar):
        for korisnik in lista_ucitanih_korisnika:
            if korisnik.get_korisnicko_ime() == ulogovan_lekar:
                return korisnik.get_spisak_pacijenata()

    @staticmethod
    def __upisi_korisnike_csv(writer, lista):
        for korisnik in lista:
            writer.writerow(korisnik.vrati_za_upis_u_fajl())

    @staticmethod
    def dodaj_id_anamneze_pacijentu(pacijent, id_anamneze):
        pacijent.dodaj_anamnezu(id_anamneze)

# samo za probe pre konacnog
KorisnikRepository.ucitavanje_korisnika()
KorisnikRepository.sacuvaj_korisnike()
# print(KorisnikRepository.vrati_spisak_pacijenata_po_lekaru("sebastijan3412"))
