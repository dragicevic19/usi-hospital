import datetime
from model.konstante.konstante import MINUTA_U_DANU, VREMENSKI_SLOT
from math import ceil


class DogadjajDTO:

    def __init__(self, datum_pocetka, datum_zavrsetka, prostorija, vreme_pocetka='00:00', vreme_zavrsetka='00:00',
                 pacijent='', lekar='', zahvat='', hitno=''):
        self._vreme_pocetka_str = vreme_pocetka
        sati_pocetak, minuti_pocetak = vreme_pocetka.split(':')
        sati_kraj, minuti_kraj = vreme_zavrsetka.split(':')
        self._vreme_pocetka = datetime.time(int(sati_pocetak), int(minuti_pocetak))
        vreme_zavrsetka = datetime.time(int(sati_kraj), int(minuti_kraj))
        self._pocetak_vreme_datum = datetime.datetime.combine(datum_pocetka, self._vreme_pocetka)
        self._zavrsetak_vreme_datum = datetime.datetime.combine(datum_zavrsetka, vreme_zavrsetka)
        razlika_datuma = self._zavrsetak_vreme_datum - self._pocetak_vreme_datum
        termini = razlika_datuma.days * MINUTA_U_DANU / VREMENSKI_SLOT + razlika_datuma.seconds / 60 / VREMENSKI_SLOT
        self._broj_termina = ceil(termini)

        self._datum_pocetka_radova = datum_pocetka.strftime("%d/%m/%Y")
        sprat, broj_prostorije = prostorija.get_sprat(), prostorija.get_broj_prostorije()
        self._sprat_broj_prostorije = '|'.join([sprat, broj_prostorije])
        self._prostorija = prostorija
        self._pacijent = pacijent
        self._lekar = lekar
        self._zahvat = zahvat
        self._hitno = hitno

    @property
    def datum_pocetka_radova(self):
        return self._datum_pocetka_radova

    @property
    def pocetak_vreme_datum(self):
        return self._pocetak_vreme_datum

    @property
    def zavrsetak_vreme_datum(self):
        return self._zavrsetak_vreme_datum

    @property
    def vreme_pocetka_str(self):
        return self._vreme_pocetka_str

    @property
    def vreme_pocetka(self):
        return self._vreme_pocetka

    @property
    def sprat_broj_prostorije(self):
        return self._sprat_broj_prostorije

    @property
    def broj_termina(self):
        return self._broj_termina

    @property
    def prostorija(self):
        return self._prostorija

    @property
    def pacijent(self):
        return self._pacijent

    @property
    def lekar(self):
        return self._lekar

    @property
    def zahvat(self):
        return self._zahvat

    @property
    def hitno(self):
        return self._hitno
