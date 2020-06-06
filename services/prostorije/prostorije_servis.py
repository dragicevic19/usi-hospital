from model.kalendarski_dogadjaj import KalendarskiDogadjaj
from services.file.file_servis import FileService
from repository.prostorije.prostorije_repozitorijum import lista_ucitanih_prostorija, ProstorijeRepository


class ProstorijeService(object):

    @staticmethod
    def dodavanje_prostorije(prostorija):
        ProstorijeRepository.dodaj_prostoriju(prostorija)

    @staticmethod
    def brisanje_prostorije(prostorija):
        prostorija._obrisana = True
        FileService.sacuvaj_entitete()

    @staticmethod
    def pretraga_prostorije():
        pass

    @staticmethod
    def renoviranje_prostorije(prostorija):
        pass

    @staticmethod
    def izmeni_namenu(prostorijaDTO):
        prostorija = prostorijaDTO.objekat_prostorije
        prostorija._namena_prostorije = prostorijaDTO.nova_namena
        dogadjaj = KalendarskiDogadjaj(prostorijaDTO.datum_pocetka_radova, prostorijaDTO.vreme, prostorijaDTO.prostorija,
                                       prostorijaDTO.broj_termina)
        ProstorijeRepository.dodaj_dogadjaj_za_prostoriju(dogadjaj)
        # ProstorijeRepository.sacuvaj_prostorije()

    @staticmethod
    def ostale_renovacije(prostorijaDTO):
        dogadjaj = KalendarskiDogadjaj(prostorijaDTO.datum_pocetka_radova, prostorijaDTO.vreme, prostorijaDTO.prostorija,
                                       prostorijaDTO.broj_termina)
        ProstorijeRepository.dodaj_dogadjaj_za_prostoriju(dogadjaj)

