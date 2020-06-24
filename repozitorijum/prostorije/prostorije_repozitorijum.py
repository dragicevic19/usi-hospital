from repozitorijum.prostorije.interfejs_prostorije_repozitorijum import InterfejsProstorijeRepo
from pathlib import Path
from model.konstante.konstante import *
from model.prostorija import Prostorija
import csv


class ProstorijeRepozitorijumImpl(InterfejsProstorijeRepo):

    def __init__(self):
        self._lista_ucitanih_prostorija = []
        self._lista_obrisanih_prostorija = []
        self.ucitavanje_prostorije()

    def ucitavanje_prostorije(self):
        path = Path(PUTANJA_FAJL_PROSTORIJE)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                obrisana = bool(red[4])
                if not obrisana:
                    self.__ucitaj_prostoriju(red, self._lista_ucitanih_prostorija)
                else:
                    self.__ucitaj_prostoriju(red, self._lista_obrisanih_prostorija)

    def __ucitaj_prostoriju(self, red, lista):
        oprema = {}
        if red[2]:
            pojedinacna_oprema = red[2].split("|")
            for stavka in pojedinacna_oprema:
                naziv, kolicina = stavka.split(";")
                oprema[naziv] = int(kolicina)
        prostorija = Prostorija(red[0], red[1], oprema, red[3], red[4])
        lista.append(prostorija)

    def dodaj_prostoriju(self, prostorija):
        self._lista_ucitanih_prostorija.append(prostorija)
        self.sacuvaj_prostorije()

    def sacuvaj_prostorije(self):
        path = Path(PUTANJA_FAJL_PROSTORIJE)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            self.__upisi_prostorije_csv(writer, self._lista_ucitanih_prostorija)
            self.__upisi_prostorije_csv(writer, self._lista_obrisanih_prostorija)

    def __upisi_prostorije_csv(self, writer, lista_prostorija):
        for prostorija in lista_prostorija:
            spisak_opreme = self.pretvori_opremu_iz_prostorije_u_string(prostorija)

            writer.writerow([prostorija.get_sprat(), prostorija.get_broj_prostorije(), spisak_opreme,
                             prostorija.get_namena_prostorije(), prostorija.get_obrisana()])

    def pretvori_opremu_iz_prostorije_u_string(self, prostorija):
        spisak_opreme = prostorija.get_spisak_opreme()
        spisak_stirng = ''
        for k, v in spisak_opreme.items():
            spisak_stirng += str(k) + ';' + str(v) + '|'
        return spisak_stirng[:-1]

    def vrati_prostoriju_po_broju_i_spratu(self, sprat, broj_sobe):
        for prostorija in self._lista_ucitanih_prostorija:
            if prostorija.get_sprat() == sprat and prostorija.get_broj_prostorije() == broj_sobe:
                return prostorija
        return False

    def obrisi_sobe(self, *prostorije_za_brisanje):
        for prostorija in prostorije_za_brisanje:
            if prostorija in self._lista_ucitanih_prostorija:
                self._lista_ucitanih_prostorija.remove(prostorija)
        self.sacuvaj_prostorije()

    def brisanje_opreme_iz_prostorija(self, naziv_opreme):
        for prostorija in self._lista_ucitanih_prostorija:
            if naziv_opreme in prostorija.get_spisak_opreme():
                prostorija.get_spisak_opreme().pop(naziv_opreme)
        self.sacuvaj_prostorije()

    def vrati_listu_prostorija_za_prikaz(self):
        return self._lista_ucitanih_prostorija

    def pronadji_prostorije_po_nameni(self, namena_prostorije):
        pronadjene_prostorije = []
        for prostorija in self._lista_ucitanih_prostorija:
            if prostorija.get_namena_prostorije() == namena_prostorije:
                sprat = prostorija.get_sprat()
                broj_prostorije = prostorija.get_broj_prostorije()
                pronadjene_prostorije.append(sprat + '|' + broj_prostorije)
        return pronadjene_prostorije





if __name__ == '__main__':
    print(ProstorijeRepozitorijumImpl().vrati_listu_prostorija_za_prikaz())
