from model.dto.dogadjaji_dto.dogadjaj_dto import DogadjajDTO


class SpajanjeProstorijeDTO(DogadjajDTO):
    def __init__(self, datum_pocetka, datum_zavrsetka, prostorija, namena, novi_broj):
        super().__init__(datum_pocetka, datum_zavrsetka, prostorija)
        self._nova_namena = namena
        self._novi_broj_prostorije = novi_broj

    @property
    def nova_namena(self):
        return self._nova_namena

    @property
    def novi_broj_prostorije(self):
        return self._novi_broj_prostorije
