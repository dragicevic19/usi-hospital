import csv

from model.enum.uloga import Uloga
from model.konstante.konstante import *
from model.lekar import Lekar
from model.pacijent import Pacijent
from model.upravnik import Upravnik
from model.administrator import Administrator
from model.sekretar import Sekretar
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
                obrisan = bool(red[5])
                if not obrisan:
                    KorisnikRepository.__kreiraj_po_ulozi(red, lista_ucitanih_korisnika)
                else:
                    KorisnikRepository.__kreiraj_po_ulozi(red, lista_obrisanih_korisnika)

    @staticmethod
    def __kreiraj_po_ulozi(red, lista):
        uloga = red[INDEX_ULOGE_KORISNIKA]
        if uloga == Uloga.UPRAVNIK.name:
            KorisnikRepository.__kreiranje_upravnika_bolnice(red, lista)
        elif uloga == Uloga.ADMINISTRATOR.name:
            KorisnikRepository.__kreiranje_administratora(red, lista)
        elif uloga == Uloga.SEKRETAR.name:
            KorisnikRepository.__kreiranje_sekretara(red, lista)
        elif uloga == Uloga.LEKAR.name:
            KorisnikRepository.__kreiranje_lekara(red, lista)
        elif uloga == Uloga.PACIJENT.name:
            KorisnikRepository.__kreiranje_pacijenta(red, lista)

    @staticmethod
    def __kreiranje_upravnika_bolnice(red, lista):
        upravnik = Upravnik(red[0], red[1], red[3], red[4], red[5])
        lista.append(upravnik)

    @staticmethod
    def __kreiranje_administratora(red, lista):
        administrator = Administrator(red[0], red[1], red[3], red[4], red[5])
        lista.append(administrator)

    @staticmethod
    def __kreiranje_sekretara(red, lista):
        sekretar = Sekretar(red[0], red[1], red[3], red[4], red[5])
        lista.append(sekretar)

    @staticmethod
    def __kreiranje_lekara(red, lista):
        spisak_specijalizacija = red[8].split(';')
        spisak_pacijenata = red[7].split(';')
        lekar = Lekar(red[0], red[1], red[3], red[4], red[6], spisak_pacijenata, spisak_specijalizacija, red[5])
        lista.append(lekar)

    @staticmethod
    def __kreiranje_pacijenta(red, lista):
        pacijent = Pacijent(red[0], red[1], red[3], red[4], red[6], red[7], red[8], red[5])
        lista.append(pacijent)

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
            # if not korisnik.get_obrisan():
            #     obrisan = ''
            # else:
            #     obrisan = True
            KorisnikRepository.sacuvaj_po_ulozi(korisnik, uloga, writer)

    @staticmethod
    def sacuvaj_po_ulozi(korisnik, uloga, writer):

        if uloga == Uloga.UPRAVNIK.name or uloga == Uloga.ADMINISTRATOR.name or uloga == Uloga.SEKRETAR.name:
            writer.writerow([korisnik.get_korisnicko_ime(), korisnik.get_lozinka(), uloga, korisnik.get_ime(),
                             korisnik.get_prezime(), korisnik.get_obrisan()])
        # ako nam bude pravilo problem to sto nemaju svi redovi isto kolona, dodacemo ,,,
        elif uloga == Uloga.LEKAR.name:
            KorisnikRepository.__sacuvaj_lekara(korisnik, uloga, writer)

        elif uloga == Uloga.PACIJENT.name:
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


KorisnikRepository.ucitavanje_korisnika()
print(lista_ucitanih_korisnika[0].get_korisnicko_ime())
