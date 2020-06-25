class ZakazivanjeDTO:

    def __init__(self, lekar, krajnji_datum, pref_vremenski_pocetni, pref_vremenski_kranji, prioritet):
        self.lekar = lekar.split(" | ")[0]
        self.krajnji_datum = krajnji_datum
        self.pref_vremenski_pocetni = pref_vremenski_pocetni
        self.pref_vremenski_krajnji = pref_vremenski_kranji
        self.prioritet = prioritet
