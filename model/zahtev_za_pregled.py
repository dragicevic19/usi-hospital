import datetime


class ZahtevZaPregled(object):

    def __init__(self, pocetni_datum, krajnji_datum, specijalista, pacijent, resen=''):
        g, m, d = pocetni_datum.split('-')
        self._pocetni_datum = datetime.datetime(int(g), int(m), int(d))
        g, m, d = krajnji_datum.split('-')
        self._krajnji_datum = datetime.datetime(int(g), int(m), int(d))
        self._specijalista = specijalista
        self._pacijent = pacijent
        self._resen = resen

    @property
    def pocetni_datum(self):
        return self._pocetni_datum

    @property
    def pocetni_datum_str(self):
        return self._pocetni_datum.strftime('%d/%m/%Y')

    @property
    def krajnji_datum_str(self):
        return self.krajnji_datum.strftime('%d/%m/%Y')

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
        return self._pocetni_datum.date(), self._krajnji_datum.date(), self._specijalista, self._pacijent, self._resen

    def vrati_za_tabelu_notifikacija(self):
        n = (self.pocetni_datum_str, self.krajnji_datum_str, '', '', '', self.specijalista, self.pacijent)
        return n
