class BolnickaOprema(object):

    def __init__(self, naziv_opreme, ukupan_broj_opreme, slobodna_oprema=None):
        self._naziv_opreme = naziv_opreme
        self._ukupan_broj_opreme = ukupan_broj_opreme
        self._slobodna_oprema = slobodna_oprema

    def get_naziv_opreme(self):
        return self._naziv_opreme

    def get_ukupan_broj_opreme(self):
        return self._ukupan_broj_opreme

    def get_slobodna_oprema(self):
        return self._slobodna_oprema

    def set_naziv_opreme(self, naziv_opreme):
        self._naziv_opreme = naziv_opreme

    def set_ukupan_broj_opreme(self, ukupan_broj_opreme):
        self._ukupan_broj_opreme = ukupan_broj_opreme

    def set_slobodna_oprema(self, slobodna_oprema):
        self._slobodna_oprema = slobodna_oprema

    def povecaj_slobodnu_opremu(self, kolicina):
        if self._slobodna_oprema + kolicina <= self._ukupan_broj_opreme:
            self._slobodna_oprema += kolicina
        else:
            print("Stack overflow! Dok Vajo i Cezare piju belo vino, vrebaju ih Maaras, Car i Kapucino.")

    def smanji_slobodnu_opremu(self, kolicina):
        if self._slobodna_oprema - kolicina >= 0:
            self._slobodna_oprema -= kolicina
        else:
            print("Stack overflow! Dok Vajo i Cezare piju belo vino, vrebaju ih Maaras, Car i Kapucino.")



