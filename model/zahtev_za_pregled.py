class ZahtevZaPregled(object):

    def __init__(self, pocetni_datum, krajnji_datum, specijalista, pacijent, resen=''):
        self._pocetni_datum = pocetni_datum
        self._krajnji_datum = krajnji_datum
        self._specijalista = specijalista
        self._pacijent = pacijent
        self._resen = resen

    @property
    def pocetni_datum(self):
        return self._pocetni_datum

    @property
    def krajnji_datum(self):
        return self._krajnji_datum

    @property
    def specijalista(self):
        return self._specijalista

    @property
    def pacijent(self):
        return self._pacijent

    @property
    def resen(self):
        return self._resen

    def vrati_za_upis_u_fajl(self):
        return self._pocetni_datum, self._krajnji_datum, self._specijalista, self._pacijent, self._resen
