import csv
from pathlib import Path
from model.konstante.konstante import *
from model.unosAnamneze import UnosAnamneze
from repository.korisnik.korisnik_repozitorijum import KorisnikRepository

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

    @staticmethod
    def pronadji_anamnezu_za_pacijenta(ulogovan_pacijent):
        lista_anamneza_po_pacijentu = []
        for unos_anamneze in lista_ucitanih_unosa_anamneza:
            if unos_anamneze.get_id() in ulogovan_pacijent.get_anamneza():
                lista_anamneza_po_pacijentu.append(unos_anamneze)
        return lista_anamneza_po_pacijentu


#samo za testiranje
UnosAnamnezeRepository.ucitavanje_unosa_anamneze()
UnosAnamnezeRepository.sacuvaj_unos_anamneze()
