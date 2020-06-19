from pathlib import Path
from model.konstante.konstante import *
from model.prostorija import Prostorija
import csv


lista_ucitanih_prostorija = []
lista_obrisanih_prostorija = []


class ProstorijeRepozitorijum:

    @staticmethod
    def ucitavanje_prostorije():
        path = Path(PUTANJA_FAJL_PROSTORIJE)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                obrisana = bool(red[4])
                if not obrisana:
                    ProstorijeRepozitorijum.__ucitaj_prostoriju(red, lista_ucitanih_prostorija)
                else:
                    ProstorijeRepozitorijum.__ucitaj_prostoriju(red, lista_obrisanih_prostorija)

    @staticmethod
    def __ucitaj_prostoriju(red, lista):
        oprema = {}
        if red[2]:
            pojedinacna_oprema = red[2].split("|")
            for stavka in pojedinacna_oprema:
                naziv, kolicina = stavka.split(";")
                oprema[naziv] = int(kolicina)
        prostorija = Prostorija(red[0], red[1], oprema, red[3], red[4])
        lista.append(prostorija)

    @staticmethod
    def dodaj_prostoriju(prostorija):
        lista_ucitanih_prostorija.append(prostorija)
        ProstorijeRepozitorijum.sacuvaj_prostorije()

    @staticmethod
    def sacuvaj_prostorije():
        path = Path(PUTANJA_FAJL_PROSTORIJE)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            ProstorijeRepozitorijum.__upisi_prostorije_csv(writer, lista_ucitanih_prostorija)
            ProstorijeRepozitorijum.__upisi_prostorije_csv(writer, lista_obrisanih_prostorija)

    @staticmethod
    def __upisi_prostorije_csv(writer, lista_prostorija):
        # lista_opreme = []
        for prostorija in lista_prostorija:
            spisak_opreme = ProstorijeRepozitorijum.recnik_u_string(prostorija.get_spisak_opreme())

            writer.writerow([prostorija.get_sprat(), prostorija.get_broj_prostorije(), spisak_opreme,
                             prostorija.get_namena_prostorije(), prostorija.get_obrisana()])

    @staticmethod
    def recnik_u_string(spisak_opreme):
        spisak_stirng = ''
        for k, v in spisak_opreme.items():
            spisak_stirng += k + ';' + str(v) + '|'

        return spisak_stirng[:-1]

    @staticmethod
    def vrati_prostoriju_po_broju_i_spratu(sprat, broj_sobe):
        for prostorija in lista_ucitanih_prostorija:
            if prostorija.get_sprat() == sprat and prostorija.get_broj_prostorije() == broj_sobe:
                return prostorija
        return False

    @staticmethod
    def obrisi_sobe(*prostorije_za_brisanje):
        for prostorija in prostorije_za_brisanje:
            if prostorija in lista_ucitanih_prostorija:
                lista_ucitanih_prostorija.remove(prostorija)


ProstorijeRepozitorijum.ucitavanje_prostorije()
