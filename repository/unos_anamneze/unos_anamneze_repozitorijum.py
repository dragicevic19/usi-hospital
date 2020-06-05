import csv
from pathlib import Path
from model.konstante.konstante import *
from model.unosAnamneze import UnosAnamneze

lista_ucitanih_unosa_anamneza = []


class UnosAnamnezeRepository:

    @staticmethod
    def ucitavanje_unosa_anamneze():
        path = Path(PATH_TO_UNOS_ANAMNEZE)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                unos_anamneze = UnosAnamneze(red[0], red[1], red[2], red[3])
                lista_ucitanih_unosa_anamneza.append(unos_anamneze)

    @staticmethod
    def sacuvaj_unos_anamneze():
        path = Path(PATH_TO_UNOS_ANAMNEZE)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')

            for unos in lista_ucitanih_unosa_anamneza:
                writer.writerow([unos.get_id(), unos.get_lekar(), unos.get_opis(), unos.get_datum_i_vreme()])
