import csv
from pathlib import Path

from model.kalendarski_dogadjaj import KalendarskiDogadjaj
from model.konstante.konstante import PATH_TO_DOGADJAJI

lista_dogadjaja = []
class KalendarRepository:

    @staticmethod
    def ucitaj_dogadjaje():
        path = Path(PATH_TO_DOGADJAJI)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                dogadjaj = KalendarskiDogadjaj(*red)
                lista_dogadjaja.append(dogadjaj)

    @staticmethod
    def sacuvaj_dogadjaj():
        pass

KalendarRepository.ucitaj_dogadjaje()

