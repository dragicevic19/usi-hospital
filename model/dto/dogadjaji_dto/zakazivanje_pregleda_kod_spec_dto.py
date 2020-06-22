from model.enum.tip_zahvata import TipZahvata


class ZakazivanjePregledaKodSpecijalisteDTO:

    def __init__(self, pocetni_datum, krajnji_datum, specijalista, pacijent):
        self._pocetni_datum = pocetni_datum
        self._krajnji_datum = krajnji_datum
        specijalista, specijalnost = specijalista.split('|')
        self._specijalista = specijalista.strip()
        self._pacijent = pacijent

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

    def vrati_za_upis_u_fajl(self):
        return self._pocetni_datum, self._krajnji_datum, self._specijalista, self._pacijent, ''
