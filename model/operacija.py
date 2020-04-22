from model.pacijent import Pacijent
from model.prostorija import Prostorija
from model.lekar import Lekar


class Operacija(object):

    def __init__(self, status, lekar, pacijent, prostorija, rezervisani_vremenski_slotovi):
        self._status = status
        self._lekar = lekar
        self._pacijent = pacijent
        self._prostorija = prostorija
        self._rezervisani_vremenski_slotovi = rezervisani_vremenski_slotovi

    def get_status(self):
        return self._status

    def get_lekar(self):
        return self._lekar

    def get_pacijent(self):
        return self._pacijent

    def get_prostorija(self):
        return self._prostorija

    def get_rezervisani_vremenski_slotovi(self):
        return self._rezervisani_vremenski_slotovi

    def set_status(self, status):
        self._status = status

    def set_lekar(self, lekar):
        self._lekar = lekar

    def set_pacijent(self, pacijent):
        self._pacijent = pacijent

    def set_prostorija(self, prostorija):
        self._prostorija = prostorija

    def set_rezervisani_vremenski_slotvovi(self, rezervisani_vremenski_slotovi):
        self._rezervisani_vremenski_slotovi = rezervisani_vremenski_slotovi