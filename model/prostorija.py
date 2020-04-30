from model.bolnickaOprema import BolnickaOprema


class Prostorija(object):

    def __init__(self, sprat, broj_prostorije, spisak_opreme=[], namena_prostorije=None, obrisana='False'):
        self._sprat = sprat
        self._broj_prostorije = broj_prostorije
        self._spisak_opreme = spisak_opreme
        self._namena_prostorije = namena_prostorije
        self._obrisana = obrisana

    def get_sprat(self):
        return self._sprat

    def get_broj_prostorije(self):
        return self._broj_prostorije

    def get_spisak_opreme(self):
        return self._spisak_opreme

    def get_namena_prostorije(self):
        return self._namena_prostorije

    def get_obrisana(self):
        return self._obrisana

    def set_sprat(self, sprat):
        self._sprat = sprat

    def set_broj_prostorije(self, broj_prostorije):
        self._broj_prostorije = broj_prostorije

    def set_spisak_opreme(self, spisak_opreme):
        self._spisak_opreme = spisak_opreme

    def set_namena_prostorije(self, namena_prostorije):
        self._namena_prostorije = namena_prostorije

    def set_obrisana(self, obrisana):
        self._obrisana = obrisana
