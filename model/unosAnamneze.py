import datetime


class UnosAnamneze():

    def __init__(self, id, lekar, opis, datum_i_vreme=datetime.datetime.now()):
        self._id = id
        self._lekar = lekar
        self._opis = opis
        self._datum_i_vreme = datum_i_vreme

    def get_id(self):
        return self._id

    def get_lekar(self):
        return self._lekar

    def get_opis(self):
        return self._opis

    def get_datum_i_vreme(self):
        return self._datum_i_vreme

    def set_lekar(self, lekar):
        self._lekar = lekar

    def set_opis(self, opis):
        self._opis = opis

    def set_datum_i_vreme(self, datum_i_vreme):
        self._datum_i_vreme = datum_i_vreme


