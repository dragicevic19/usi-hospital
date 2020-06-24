import datetime


class KalendarskiDogadjaj:

    def __init__(self, datum, vreme, prostorija, broj_termina, spisak_doktora='', pacijent='', zahvat='',
                 hitno=''):
        self._prostorija = prostorija
        self._sprat, self._broj_prostorije = prostorija.split('|')
        self._broj_termina = int(broj_termina)
        self._spisak_doktora = spisak_doktora.split('|')
        self._pacijent = pacijent
        d, m, g = datum.split("/")
        sat, min = vreme.split(":")
        self._datum_vreme = datetime.datetime(int(g), int(m), int(d), int(sat), int(min))
        self._datum = datum
        self._vreme_pocetka_str = vreme
        self._zahvat = zahvat
        self._hitno = hitno

    @property
    def prostorija(self):
        return self._prostorija

    @property
    def datum_vreme(self):
        return self._datum_vreme

    @property
    def datum(self):
        return self._datum

    @property
    def vreme_pocetka_str(self):
        return self._vreme_pocetka_str

    @property
    def datum_vreme_zavrsetka(self):
        return self._datum_vreme + datetime.timedelta(minutes=30 * self._broj_termina)

    @property
    def sprat(self):
        return self._sprat

    @property
    def broj_prostorije(self):
        return self._broj_prostorije

    @property
    def broj_termina(self):
        return self._broj_termina

    @property
    def spisak_doktora(self):
        return self._spisak_doktora

    @property
    def zahvat(self):
        return self._zahvat

    @property
    def pacijent(self):
        return self._pacijent

    @property
    def hitno(self):
        return self._hitno

    def vrati_za_upis_u_fajl(self):
        return self._datum, self._vreme_pocetka_str, self._sprat + "|" + self._broj_prostorije, \
               self._broj_termina, "|".join(self._spisak_doktora), self._pacijent, self._zahvat, self._hitno

    def vrati_za_tabelu_notifikacija(self):
        n = (
            self.datum_vreme.date().strftime('%d/%m/%Y'), self.datum_vreme_zavrsetka.date().strftime('%d/%m/%Y'),
            str(self.datum_vreme.time())[0:5],
            str(self.datum_vreme_zavrsetka.time())[0:5], self.prostorija, self.spisak_doktora[0], self.pacijent)
        return n

    # def __str__(self):
    #     return [str(self.datum_vreme.date()) + str(self.datum_vreme_zavrsetka.date()) + str(
    #         self.datum_vreme.time()) + str(self.datum_vreme_zavrsetka.time()) + self.prostorija + str(
    #         self.spisak_doktora) + self.pacijent]
