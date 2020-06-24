from model.dto.dogadjaji_dto.dogadjaj_dto import DogadjajDTO


class PremestanjeOpremeDTO(DogadjajDTO):

    def __init__(self, datum_pocetka, datum_zavrsetka, prostorija, naziv_opreme, broj_opreme):
        super().__init__(datum_pocetka, datum_zavrsetka, prostorija)
        self._naziv_opreme = naziv_opreme
        self._broj_opreme = int(broj_opreme)

    @property
    def naziv_opreme(self):
        return self._naziv_opreme

    @property
    def broj_opreme(self):
        return self._broj_opreme
