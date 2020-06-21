from repozitorijum.oprema.interfejs_oprema_repozitorijum import InterfejsOpremaRepo
from model.bolnicka_oprema import BolnickaOprema
from model.konstante.konstante import *
from pathlib import Path
import csv


class OpremaRepozitorijumImpl(InterfejsOpremaRepo):

    def __init__(self):
        self._lista_ucitane_bolnicke_opreme = []
        self.__ucitavanje_bolnicke_opreme()

    def __ucitavanje_bolnicke_opreme(self):
        path = Path(PUTANJA_FAJL_BOLNICKA_OPREMA)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                bolnicka_oprema = BolnickaOprema(*red)
                self._lista_ucitane_bolnicke_opreme.append(bolnicka_oprema)

    def sacuvaj_bolnicku_opremu(self, oprema=None):
        path = Path(PUTANJA_FAJL_BOLNICKA_OPREMA)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for oprema in self._lista_ucitane_bolnicke_opreme:
                writer.writerow(oprema.vrati_za_upis_u_file())

    def nadji_po_nazivu_opreme(self, naziv_opreme):
        for oprema in self._lista_ucitane_bolnicke_opreme:
            if oprema.get_naziv_opreme() == naziv_opreme:
                return oprema
        return False

    def dodaj_opremu(self, oprema):
        self._lista_ucitane_bolnicke_opreme.append(oprema)
        self.sacuvaj_bolnicku_opremu()

    def azuriranje_opreme(self, oprema):
        pass

    def brisanje_opreme(self, oprema):
        oprema._obrisan = True
        self._lista_ucitane_bolnicke_opreme.remove(oprema)
        self.sacuvaj_bolnicku_opremu()

    def smanji_broj_slobodne_opreme(self, prostorija_za_izmenu):
        for oprema in self._lista_ucitane_bolnicke_opreme:
            if oprema._naziv_opreme == prostorija_za_izmenu.naziv_opreme:
                oprema._slobodna_oprema -= prostorija_za_izmenu.broj_opreme
        self.sacuvaj_bolnicku_opremu()

    def povecaj_broj_slobodne_opreme(self, naziv, broj_opreme):
        for oprema in self._lista_ucitane_bolnicke_opreme:
            if oprema._naziv_opreme == naziv:
                oprema._slobodna_oprema += broj_opreme
        self.sacuvaj_bolnicku_opremu()

    def vrati_svu_opremu_u_sistemu(self):
        return self._lista_ucitane_bolnicke_opreme

    def vrati_nazive_bolnicke_opreme_u_sistemu(self):
        lista_imena_opreme = []
        for oprema in self._lista_ucitane_bolnicke_opreme:
            lista_imena_opreme.append(oprema._naziv_opreme)
        return lista_imena_opreme
