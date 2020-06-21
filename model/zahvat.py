from model.pacijent import Pacijent
from model.lekar import Lekar


class Zahvat(object):

    def __init__(self, vrsta_zahvata,status, lekar, pacijent, prostorija,rezervisani_vremenski_slotovi,hitno):
        self._vrsta_zahvata = vrsta_zahvata
        self._status = status
        self._lekar = lekar
        self._pacijent = pacijent
        self._prostorija = prostorija
        self._rezervisani_vremenski_slotovi = rezervisani_vremenski_slotovi
        self._hitno = None

    def get_vrsta_zahvata(self):
        return self._vrsta_zahvata

    def get_status(self):
        return self._status

    def get_hitno(self):
        return self._hitno

    def get_lekar(self):
        return self._lekar

    def get_pacijent(self):
        return self._pacijent

    def get_prostorija(self):
        return self._prostorija

    def get_rezervisani_vremenski_slotovi(self):
        return self._rezervisani_vremenski_slotovi

    def set_hitno(self, hitno):
        self._hitno = hitno

    def set_status(self, status):
        self._status = status

    def set_vrsta_zahvata(self, vrsta_zahvata):
        self._vrsta_zahvata = vrsta_zahvata

    def set_lekar(self, lekar):
        self._lekar = lekar

    def set_pacijent(self, pacijent):
        self._pacijent = pacijent

    def set_prostorija(self, prostorija):
        self._prostorija = prostorija

    def set_rezervisani_vremenski_slotvovi(self, rezervisani_vremenski_slotovi):
        self._rezervisani_vremenski_slotovi = rezervisani_vremenski_slotovi

    def __str__(self):
        return "Vrsta zahvata:" + self._vrsta_zahvata + "Lekar:" + str(Lekar) + "Pacijent:" + str(Pacijent)