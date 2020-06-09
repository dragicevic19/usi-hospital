import csv
from pathlib import Path
from model.konstante.konstante import *
from model.unosAnamneze import UnosAnamneze
from repository.korisnik.korisnik_repozitorijum import KorisnikRepository, lista_ucitanih_korisnika

mapa_ucitanih_unosa_anamneza = {}
id_sledece_anamneze = 0


class UnosAnamnezeRepository:

    @staticmethod
    def ucitavanje_unosa_anamneze():
        path = Path(PATH_TO_UNOS_ANAMNEZE)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                unos_anamneze = UnosAnamneze(*red)
                mapa_ucitanih_unosa_anamneza[red[0]] = unos_anamneze

    @staticmethod
    def sacuvaj_unos_anamneze():
        path = Path(PATH_TO_UNOS_ANAMNEZE)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for kljuc in mapa_ucitanih_unosa_anamneza:
                unos = mapa_ucitanih_unosa_anamneza[kljuc]
                writer.writerow([unos.get_id(), unos.get_lekar(), unos.get_opis(), unos.get_datum_i_vreme()])

    @staticmethod
    def generisi_id_anamneze():
        global id_sledece_anamneze
        for kljuc in mapa_ucitanih_unosa_anamneza:
            if int(kljuc) > id_sledece_anamneze:
                id_sledece_anamneze = int(kljuc)
        id_sledece_anamneze += 1

    def pronadji_anamnezu_za_pacijenta(ulogovan_pacijent):
        lista_anamneza_po_pacijentu = []
        for kljuc in mapa_ucitanih_unosa_anamneza:
            unos = mapa_ucitanih_unosa_anamneza[kljuc]
            if unos.get_id() in ulogovan_pacijent.get_anamneza():
                lista_anamneza_po_pacijentu.append(unos)
        return lista_anamneza_po_pacijentu


UnosAnamnezeRepository.ucitavanje_unosa_anamneze()
UnosAnamnezeRepository.sacuvaj_unos_anamneze()

