import datetime


class PregledAnamnezeDTO:

    def __init__(self, lekar, opis, datum_i_vreme=datetime.datetime.now()):
        super().__init__(pacijent=None, spisak_pojedinacnih_unosa=[])
        self._lekar = lekar
        self._opis = opis
        self._datum_i_vreme = datum_i_vreme