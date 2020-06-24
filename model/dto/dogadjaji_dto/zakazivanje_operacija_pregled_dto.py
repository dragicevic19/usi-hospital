from model.dto.dogadjaji_dto.dogadjaj_dto import DogadjajDTO
from servis.prostorije.prostorije_servis import ProstorijeServis


class ZakazivanjeOperacijaPregledDTO(DogadjajDTO):
    def __init__(self, datum_pocetka, vreme_pocetka, vreme_zavrsetka, lekar, pacijent, prostorija_sprat_br,
                 zahvat, hitna_operacija=''):
        sprat, broj = prostorija_sprat_br.split('|')
        prostorija = ProstorijeServis().pronadji_prostoriju(sprat, broj)
        datum_zavrsetka = datum_pocetka  # za sad jer operacija ne moze da predje u sledeci dan
        super().__init__(datum_pocetka, datum_zavrsetka, prostorija, vreme_pocetka, vreme_zavrsetka, pacijent, lekar,
                         zahvat, hitna_operacija)
