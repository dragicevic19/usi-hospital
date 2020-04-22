class Notifikacija(object):

    def __init__(self, zahvat, prvobitni_status, izmenjeni_status, poruka):
        self._zahvat = zahvat
        self._prvobitni_status = prvobitni_status
        self._izmenjeni_status = izmenjeni_status
        self._poruka = poruka

    def get_zahvat(self):
        return self._zahvat

    def get_prvobitni_status(self):
        return self._prvobitni_status

    def get_izmenjeni_status(self):
        return self._izmenjeni_status

    def get_poruka(self):
        return self._poruka

    def set_pregled(self, zahvat):
        self._zahvat = zahvat

    def set_prvobitni_status(self, prvobitni_status):
        self._prvobitni_status = prvobitni_status

    def set_izmenjeni_status(self, izmenjeni_status):
        self._izmenjeni_status = izmenjeni_status

    def set_poruka(self, poruka):
        self._poruka = poruka
