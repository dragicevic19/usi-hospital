# mm/dd/gg
import datetime


class KalendarskiDogadjaj:

    def __init__(self, datum, vreme, prostorija, broj_termina, spisak_doktora='', spisak_pacijenata='', zahvat='',
                 hitno=''):
        self._prostorija = prostorija
        self._sprat, self._broj_prostorije = prostorija.split('|')
        self._broj_termina = int(broj_termina)
        self._spisak_doktora = spisak_doktora.split('|')
        self._spisak_pacijenata = spisak_pacijenata.split('|')  # mozda ne treba split nego samo jedan pacijent
        d, m, g = datum.split("/")
        sat, min = vreme.split(":")
        self._datum_vreme = datetime.datetime(int(g), int(m), int(d), int(sat), int(min))
        self._datum = datum
        self._vreme = vreme
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
    def vreme(self):
        return self._vreme

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
    def spisak_pacijenata(self):
        return self._spisak_pacijenata

    @property
    def hitno(self):
        return self._hitno

    def vrati_za_upis_u_fajl(self):
        return self._datum, self._vreme, self._sprat + "|" + self._broj_prostorije, \
               self._broj_termina, "|".join(self._spisak_doktora), "|".join(self._spisak_pacijenata), \
               self._zahvat, self._hitno
