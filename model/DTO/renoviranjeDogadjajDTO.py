import datetime
from model.konstante.konstante import *


class RenoviranjeDTO:

    def __init__(self, datum_pocetka_radova, datum_zavrsetka_radova, prostorija, namena=''):
        self._datum_pocetka_radova = datum_pocetka_radova.strftime("%d/%m/%Y")
        self._vreme = '00:00'
        sprat = prostorija.get_sprat()
        broj_prostorije = prostorija.get_broj_prostorije()
        self._prostorija = '|'.join([sprat, broj_prostorije])
        self._nova_namena = namena
        razlika_datuma = datum_zavrsetka_radova - datum_pocetka_radova
        self._broj_termina = razlika_datuma.days * MINUTA_U_DANU / VREMENSKI_SLOT
        self._objekat_prostorije = prostorija

    @property
    def datum_pocetka_radova(self):
        return self._datum_pocetka_radova

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


if __name__ == '__main__':
    a = datetime.date(2020, 4, 20)
    print(a)
    strDate = a.strftime("%d/%m/%Y")
    print(strDate)
