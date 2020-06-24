class NotifikacijaDTO:
    def __init__(self, datum_pocetka, datum_zavrsetka, vreme_pocetka, vreme_zavrsetka, prostorija, lekar, pacijent):
        self._datum_pocetka = datum_pocetka
        self._datum_zavrsetka = datum_zavrsetka
        self._vreme_pocetka = vreme_pocetka
        self._vreme_zavrsetka = vreme_zavrsetka
        self._prostorija = prostorija
        self._lekar = lekar
        self._pacijent = pacijent

    @property
    def datum_pocetka(self):
        return self._datum_pocetka

    @property
    def datum_zavrsetka(self):
        return self._datum_zavrsetka

    @property
    def vreme_pocetka(self):
        return self._vreme_pocetka

    @property
    def vreme_zavrsetka(self):
        return self._vreme_zavrsetka

    @property
    def prostorija(self):
        return self._prostorija

    @property
    def lekar(self):
        return self._lekar

    @property
    def pacijent(self):
        return self._pacijent
