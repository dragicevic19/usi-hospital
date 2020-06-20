import csv
from datetime import datetime
from pathlib import Path
from model.konstante.konstante import *
from model.unos_anamneze import UnosAnamneze
from repozitorijum.korisnik.korisnik_repozitorijum import KorisnikRepozitorijum, lista_ucitanih_korisnika

mapa_ucitanih_unosa_anamneza = {}
id_sledece_anamneze = 0


class UnosAnamnezeRepozitorijum:

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

    @staticmethod
    def dodaj_anamnezu_u_mapu_anamneza(lekar, opis_anamneze, pacijent):
        UnosAnamnezeRepozitorijum.generisi_id_anamneze()
        global id_sledece_anamneze
        datum = datetime.now().strftime("%d-%m-%Y %H:%M")
        anamneza = UnosAnamneze(id_sledece_anamneze, lekar, opis_anamneze, datum)
        mapa_ucitanih_unosa_anamneza[str(id)] = anamneza
        KorisnikRepozitorijum.dodaj_id_anamneze_pacijentu(pacijent, str(id_sledece_anamneze))


UnosAnamnezeRepozitorijum.ucitavanje_unosa_anamneze()

