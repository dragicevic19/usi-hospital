class Anamneza(object):

    def __init__(self, pacijent=None, spisak_pojedinacnih_unosa=[]):
        self._pacijent = pacijent
        self._spisak_pojedinacnih_unosa = spisak_pojedinacnih_unosa

    def get_pacijent(self):
        return self._pacijent

    def get_spisak_pojedinacnih_unosa(self):
        return self._spisak_pojedinacnih_unosa

    def set_pacijent(self, pacijent):
        self._pacijent = pacijent

    def set_spisak_pojedinacnih_unosa(self, spisak_pojedinacnih_unosa):
        self._spisak_pojedinacnih_unosa = spisak_pojedinacnih_unosa






