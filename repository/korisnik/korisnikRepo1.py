import csv

from model.enum.uloga import Uloga
from model.enum.recnici import *
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
    def __upisi_korisnike_csv(writer, lista):
        for korisnik in lista:
            uloga = korisnik.get_uloga()
            KorisnikRepository.sacuvaj_po_ulozi(korisnik, uloga, writer)

    @staticmethod
    def sacuvaj_po_ulozi(korisnik, uloga, writer):

        if uloga == 'UPRAVNIK' or uloga == 'ADMINISTRATOR' or uloga == 'SEKRETAR':
            writer.writerow([korisnik.get_korisnicko_ime(), korisnik.get_lozinka(), uloga, korisnik.get_ime(),
                             korisnik.get_prezime(), korisnik.get_obrisan()])

        elif uloga == 'LEKAR':
            KorisnikRepository.__sacuvaj_lekara(korisnik, uloga, writer)

        elif uloga == 'PACIJENT':
            KorisnikRepository.__sacuvaj_pacijenta(korisnik, uloga, writer)

    @staticmethod
    def __sacuvaj_lekara(korisnik, uloga, writer):
        spisak_spec = ';'.join(korisnik.get_spisak_specijalizacija())
        spisak_pacijenata = ';'.join(korisnik.get_spisak_pacijenata())

        writer.writerow([korisnik.get_korisnicko_ime(), korisnik.get_lozinka(), uloga,
                         korisnik.get_ime(), korisnik.get_prezime(), korisnik.get_obrisan(), korisnik.get_radno_vreme(),
                         spisak_pacijenata, spisak_spec])

    @staticmethod
    def __sacuvaj_pacijenta(korisnik, uloga, writer):
        writer.writerow([korisnik.get_korisnicko_ime(), korisnik.get_lozinka(), uloga,
                         korisnik.get_ime(), korisnik.get_prezime(), korisnik.get_obrisan(),
                         korisnik.get_br_zdravstvene(), korisnik.get_pol(), korisnik.get_anamneza()])
