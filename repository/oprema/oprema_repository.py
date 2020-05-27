import csv

from model.bolnickaOprema import BolnickaOprema
from pathlib import Path
from model.konstante.konstante import *

lista_ucitane_bolnicke_opreme = []


class OpremaRepository:

    @staticmethod
    def ucitavanje_bolnicke_opreme():
        path = Path(PATH_TO_BOLNICKA_OPREMA)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                bolnicka_oprema = BolnickaOprema(red[0], int(red[1]), int(red[2]), red[3])
                lista_ucitane_bolnicke_opreme.append(bolnicka_oprema)

    @staticmethod
    def sacuvaj_bolnicku_opremu():
        path = Path(PATH_TO_BOLNICKA_OPREMA)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for oprema in lista_ucitane_bolnicke_opreme:
                writer.writerow([oprema.get_naziv_opreme(), oprema.get_ukupan_broj_opreme(),
                                 oprema.get_slobodna_oprema(), oprema.get_opis()])

    @staticmethod
    def postoji_oprema(naziv_opreme):
        for oprema in lista_ucitane_bolnicke_opreme:
            if oprema.get_naziv_opreme() == naziv_opreme:
                return oprema
        return False

