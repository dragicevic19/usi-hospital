from model.dto.dogadjaji_dto.dogadjaj_dto import DogadjajDTO


class IzmenaNameneDTO(DogadjajDTO):
    def __init__(self, datum_pocetka, datum_zavrsetka, prostorija, namena):
        super().__init__(datum_pocetka, datum_zavrsetka, prostorija)
        self._nova_namena = namena

    @property
    def nova_namena(self):
        return self._nova_namena
