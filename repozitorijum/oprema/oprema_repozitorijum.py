from model.bolnicka_oprema import BolnickaOprema
from pathlib import Path
from model.konstante.konstante import *
from repozitorijum.prostorije.prostorije_repozitorijum import lista_ucitanih_prostorija
import csv

lista_ucitane_bolnicke_opreme = []


class OpremaRepozitorijum:

    @staticmethod
    def ucitavanje_bolnicke_opreme():
        path = Path(PUTANJA_FAJL_BOLNICKA_OPREMA)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                bolnicka_oprema = BolnickaOprema(*red)
                lista_ucitane_bolnicke_opreme.append(bolnicka_oprema)

    @staticmethod
    def sacuvaj_bolnicku_opremu():
        path = Path(PUTANJA_FAJL_BOLNICKA_OPREMA)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for oprema in lista_ucitane_bolnicke_opreme:
                writer.writerow(oprema.vrati_za_upis_u_file())

    @staticmethod
    def nadji_po_nazivu_opreme(naziv_opreme):
        for oprema in lista_ucitane_bolnicke_opreme:
            if oprema.get_naziv_opreme() == naziv_opreme:
                return oprema
        return False

    @staticmethod
    def dodaj_opremu(oprema):
        lista_ucitane_bolnicke_opreme.append(oprema)
        OpremaRepozitorijum.sacuvaj_bolnicku_opremu()

    @staticmethod
    def azuriranje_opreme(oprema):
        pass

    @staticmethod
    def brisanje_opreme(oprema):
        oprema._obrisan = True
        lista_ucitane_bolnicke_opreme.remove(oprema)
        OpremaRepozitorijum.sacuvaj_bolnicku_opremu()

    @staticmethod
    def brisanje_opreme_iz_prostorija(naziv_opreme):
        for prostorija in lista_ucitanih_prostorija:
            if naziv_opreme in prostorija.get_spisak_opreme():
                prostorija.get_spisak_opreme().pop(naziv_opreme)
                OpremaRepozitorijum.sacuvaj_bolnicku_opremu()


#  samo za testiranje
OpremaRepozitorijum.ucitavanje_bolnicke_opreme()
# OpremaRepository.sacuvaj_bolnicku_opremu()
