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
    recnik = {'1': Upravnik, '2': Administrator, '3': Sekretar, '4': Lekar, '5': Pacijent}

    def citaj(self):
        path = Path(PATH_TO_KORISNICI)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                korisnik = self.recnik[red[2]](*red)
                if not korisnik.get_obrisan():
                    lista_ucitanih_korisnika.append(korisnik)
                else:
                    lista_obrisanih_korisnika.append(korisnik)


if __name__ == '__main__':
    proba = KorisnikRepository()
    proba.citaj()
    print(len(lista_ucitanih_korisnika))
