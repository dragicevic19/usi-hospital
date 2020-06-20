from datetime import datetime

class PretragaProstorijaDTO:

    def __init__(self,spisak_zahtevane_oprem,pocetni_datum,pocetno_vreme,krajnji_datum,krajnje_vreme,zauzece):
        self.spisak_zahtevane_opreme = spisak_zahtevane_oprem
        spisak_Od = pocetni_datum.split("/")
        vreme_Od = pocetno_vreme.split(":")
        self.pocetno_vreme = datetime(int(spisak_Od[2]),int(spisak_Od[1]),int(spisak_Od[0]),int(vreme_Od[0]),
                                      int(vreme_Od[1]))
        spisak_Do = krajnji_datum.split("/")
        vreme_Do = krajnje_vreme.split(":")
        self.krajnje_vreme = datetime(int(spisak_Do[2]), int(spisak_Do[1]), int(spisak_Do[0]), int(vreme_Do[0]),
                                      int(vreme_Do[1]))


        self.zauzece = zauzece
