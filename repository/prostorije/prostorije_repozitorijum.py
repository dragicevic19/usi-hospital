import csv
from pathlib import Path
from model.konstante.konstante import *
from model.prostorija import Prostorija
from repository.kalendar.kalendar_repozitorijum import KalendarRepository

lista_ucitanih_prostorija = []
lista_obrisanih_prostorija = []


class ProstorijeRepository:

    @staticmethod
    def ucitavanje_prostorije():
        path = Path(PATH_TO_PROSTORIJE)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                obrisana = bool(red[4])
                if not obrisana:
                    ProstorijeRepository.__ucitaj_prostoriju(red, lista_ucitanih_prostorija)
                else:
                    ProstorijeRepository.__ucitaj_prostoriju(red, lista_obrisanih_prostorija)

    @staticmethod
    def __ucitaj_prostoriju(red, lista):
        lista_oprema = []
        if red[2]:
            pojedinacna_oprema = red[2].split("|")
            for stavka in pojedinacna_oprema:
                oprema = {}
                naziv, kolicina = stavka.split(";")
                oprema[naziv] = kolicina
                lista_oprema.append(oprema)
        prostorija = Prostorija(red[0], red[1], lista_oprema, red[3], red[4])
        lista.append(prostorija)

    @staticmethod
    def dodaj_prostoriju(prostorija):
        lista_ucitanih_prostorija.append(prostorija)
        ProstorijeRepository.sacuvaj_prostorije()

    @staticmethod
    def sacuvaj_prostorije():
        path = Path(PATH_TO_PROSTORIJE)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            ProstorijeRepository.__upisi_prostorije_csv(writer, lista_ucitanih_prostorija)
            ProstorijeRepository.__upisi_prostorije_csv(writer, lista_obrisanih_prostorija)

    @staticmethod
    def __upisi_prostorije_csv(writer, lista_prostorija):
        lista_opreme = []
        for prostorija in lista_prostorija:
            for oprema in prostorija.get_spisak_opreme():
                for k, v in oprema.items():
                    lista_opreme.append(k + ";" + v)

            spisak_opreme = '|'.join(lista_opreme)
            lista_opreme.clear()
            writer.writerow([prostorija.get_sprat(), prostorija.get_broj_prostorije(), spisak_opreme,
                             prostorija.get_namena_prostorije(), prostorija.get_obrisana()])

    @staticmethod
    def vrati_prostoriju_po_broju_i_spratu(sprat, broj_sobe):
        for prostorija in lista_ucitanih_prostorija:
            if prostorija.get_sprat() == sprat and prostorija.get_broj_prostorije() == broj_sobe:
                return prostorija
        return False

    @staticmethod
    def dodaj_dogadjaj_za_prostoriju(dogadjaj):
        ProstorijeRepository.sacuvaj_prostorije()
        KalendarRepository.dodaj_dogadjaj(dogadjaj)
