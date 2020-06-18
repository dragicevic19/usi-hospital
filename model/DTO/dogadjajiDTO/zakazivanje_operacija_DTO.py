from model.DTO.dogadjajiDTO.dogadjajDTO import DogadjajDTO
from repozitorijum.prostorije.prostorije_repozitorijum import ProstorijeRepozitorijum


class ZakazivanjeOperacijeDTO(DogadjajDTO):
    def __init__(self, datum_pocetka, vreme_pocetka, vreme_zavrsetka, lekar, pacijent, operaciona_sala_sprat_broj,
                 hitna_operacija, zahvat):
        sprat, broj = operaciona_sala_sprat_broj.split('|')
        prostorija = ProstorijeRepozitorijum.vrati_prostoriju_po_broju_i_spratu(sprat, broj)
        datum_zavrsetka = datum_pocetka  # za sad jer operacija ne moze da predje u sledeci dan
        super().__init__(datum_pocetka, datum_zavrsetka, prostorija, vreme_pocetka, vreme_zavrsetka, pacijent, lekar,
                         zahvat, hitna_operacija)
