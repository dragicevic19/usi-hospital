

class UnosAnamnezeDTO:
    def __init__(self, lekar, anamneza, pacijent):
        self._lekar = lekar.get_korisnicko_ime()
        self._anamneza = anamneza
        self._pacijent = pacijent

    @property
    def lekar(self):
        return self._lekar

    @property
    def anamneza(self):
        return self._anamneza

    @property
    def pacijent(self):
        return self._pacijent



