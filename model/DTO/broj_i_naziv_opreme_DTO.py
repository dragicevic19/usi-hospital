

class BrojINazivOpremeDTO:
    def __init__(self, naziv, broj_slobodne_opreme):
        self._naziv_opreme = naziv
        self._broj_slobodne_opreme = broj_slobodne_opreme

    @property
    def naziv_opreme(self):
        return self._naziv_opreme

    @property
    def broj_slobodne_opreme(self):
        return self._broj_slobodne_opreme