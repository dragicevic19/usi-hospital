from model.konstante.konstante import MINUTA_U_DANU, VREMENSKI_SLOT


class DeljenjeProstorijeDTO:

    def __init__(self, datum_pocetka, datum_zavrsetka, prostorija, naziv_opreme, broj_opreme1, broj_opreme2,
                 visak_opreme, namena1, namena2, broj_prostorije1, broj_prostorije2):

        self._datum_pocetka_radova = datum_pocetka.strftime('%d/%m/%Y')
        self._datum_pocetkaDate = datum_pocetka
        self._datum_zavrsetkaDate = datum_zavrsetka
        self._vreme = '00:00'
        self._broj_termina = (datum_zavrsetka - datum_pocetka).days * MINUTA_U_DANU / VREMENSKI_SLOT
        self._stara_prostorija = prostorija
        self._sprat_broj_prostorije = '|'.join([prostorija.get_sprat(), prostorija.get_broj_prostorije()])
        self._naziv_opreme = naziv_opreme
        self._broj_opreme_prva = int(broj_opreme1)
        self._broj_opreme_druga = int(broj_opreme2)
        self._visak_opreme = int(visak_opreme)
        self._namena_prve = namena1
        self._namena_druge = namena2
        self._broj_prve_prostorije = broj_prostorije1
        self._broj_druge_prostorije = broj_prostorije2

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
    def broj_termina(self):
        return self._broj_termina

    @property
    def vreme(self):
        return self._vreme

    @property
    def stara_prostorija(self):
        return self._stara_prostorija

    @property
    def sprat_broj_prostorije(self):
        return self._sprat_broj_prostorije

    @property
    def naziv_opreme(self):
        return self._naziv_opreme

    @property
    def broj_opreme_prva(self):
        return self._broj_opreme_prva

    @property
    def broj_opreme_druga(self):
        return self._broj_opreme_druga

    @property
    def visak_opreme(self):
        return self._visak_opreme

    @property
    def namena_prve(self):
        return self._namena_prve

    @property
    def namena_druge(self):
        return self._namena_druge

    @property
    def broj_prve_prostorije(self):
        return self._broj_prve_prostorije

    @property
    def broj_druge_prostorije(self):
        return self._broj_druge_prostorije
