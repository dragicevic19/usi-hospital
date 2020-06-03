# mm/dd/gg
import datetime


class KalendarskiDogadjaj:

    def __init__(self, datum, vreme, prostorija, broj_termina=1, spisak_doktora='', spisak_pacijenata=''):
        self._sprat, self._broj_prostorije = prostorija.split('|')
        self._broj_termina = int(broj_termina)
        self._spisak_doktora = spisak_doktora.split('|')
        self._spisak_pacijenata = spisak_pacijenata.split('|')
        d, m, g = datum.split("/")
        sat, min = vreme.split(":")
        self._datum_vreme = datetime.datetime(int(g), int(m), int(d), int(sat), int(min))

    # dodati setter
    @property
    def datum_vreme(self):
        return self._datum_vreme

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
    def spisak_pacijenata(self):
        return self._spisak_pacijenata

    @sprat.setter
    def sprat(self, sprat):
        self._sprat = sprat

    @broj_prostorije.setter
    def broj_prostorije(self, broj_prostorije):
        self._broj_prostorije = broj_prostorije

    @broj_termina.setter
    def broj_termina(self, broj_termina):
        self._broj_termina = broj_termina

    @spisak_doktora.setter
    def spisak_doktora(self, spisak_doktora):
        self._spisak_doktora = spisak_doktora

    @spisak_pacijenata.setter
    def spisak_pacijenata(self, spisak_pacijenata):
        self._spisak_pacijenata = spisak_pacijenata

    def vrati_za_upis_u_fajl(self):
        return self._datum, self._vreme, self._sprat + "|" + self._broj_prostorije, \
               self._broj_termina, "|".join(self._spisak_doktora), "|".join(self._spisak_pacijenata)
