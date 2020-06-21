from model.dto.dogadjaji_dto.dogadjaj_dto import DogadjajDTO


class DeljenjeProstorijeDTO(DogadjajDTO):

    def __init__(self, datum_pocetka, datum_zavrsetka, prostorija, naziv_opreme, broj_opreme1, broj_opreme2,
                 visak_opreme, namena1, namena2, broj_prostorije1, broj_prostorije2):

        super().__init__(datum_pocetka, datum_zavrsetka, prostorija)
        self._naziv_opreme = naziv_opreme
        self._broj_opreme_prva = int(broj_opreme1)
        self._broj_opreme_druga = int(broj_opreme2)
        self._visak_opreme = int(visak_opreme)
        self._namena_prve = namena1
        self._namena_druge = namena2
        self._broj_prve_prostorije = broj_prostorije1
        self._broj_druge_prostorije = broj_prostorije2

    @property
    def naziv_opreme(self):
        return self._naziv_opreme

    @property
    def broj_opreme_prva(self):
        return self._broj_opreme_prva

    @property
    def broj_opreme_druga(self):
        return self._broj_opreme_druga

    @property
    def visak_opreme(self):
        return self._visak_opreme

    @property
    def namena_prve(self):
        return self._namena_prve

    @property
    def namena_druge(self):
        return self._namena_druge

    @property
    def broj_prve_prostorije(self):
        return self._broj_prve_prostorije

    @property
    def broj_druge_prostorije(self):
        return self._broj_druge_prostorije
