import datetime
from model.konstante.konstante import *


class RenoviranjeDTO:

    def __init__(self, datum_pocetka, datum_zavrsetka, prostorija, naziv_opreme='', broj_opreme=0, namena=''):

        self._datum_pocetka_radova = datum_pocetka.strftime("%d/%m/%Y")
        self._datum_pocetkaDate = datum_pocetka
        self._datum_zavrsetkaDate = datum_zavrsetka
        razlika_datuma = datum_zavrsetka - datum_pocetka
        self._broj_termina = razlika_datuma.days * MINUTA_U_DANU / VREMENSKI_SLOT
        self._vreme = '00:00'

        sprat, broj_prostorije = prostorija.get_sprat(), prostorija.get_broj_prostorije()
        self._prostorija = '|'.join([sprat, broj_prostorije])
        self._nova_namena = namena

        self._objekat_prostorije = prostorija
        self._naziv_opreme = naziv_opreme
        self._broj_opreme = int(broj_opreme)

    @property
    def datum_pocetka_radova(self):
        return self._datum_pocetka_radova
    
    @property
    def datum_pocetkaDate(self):
        return self._datum_pocetkaDate

    @property
    def datum_zavrsetkaDate(self):
        return self._datum_zavrsetkaDate

    @property
    def vreme(self):
        return self._vreme

    @property
    def prostorija(self):
        return self._prostorija

    @property
    def nova_namena(self):
        return self._nova_namena

    @property
    def broj_termina(self):
        return self._broj_termina

    @property
    def objekat_prostorije(self):
        return self._objekat_prostorije

    @property
    def naziv_opreme(self):
        return self._naziv_opreme

    @property
    def broj_opreme(self):
        return self._broj_opreme


if __name__ == '__main__':
    a = datetime.date(2020, 4, 20)
    print(a)
    strDate = a.strftime("%d/%m/%Y")
    print(strDate)
