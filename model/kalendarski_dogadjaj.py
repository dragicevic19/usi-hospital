# mm/dd/gg
class KalendarskiDogadjaj:

    def __init__(self, datum, vreme, prostorija, broj_termina=1, spisak_doktora='', spisak_pacijenata=''):
        self._datum = datum
        self._vreme = vreme
        self._sprat, self._broj_prostorije = prostorija.split('|')
        self._broj_termina = broj_termina
        self._spisak_doktora = spisak_doktora.split('|')
        self._spisak_pacijenata = spisak_pacijenata.split('|')
