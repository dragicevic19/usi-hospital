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
    def izmeni_namenu(prostorija, namena):
        prostorija._namena_prostorije = namena
        ProstorijeRepository.sacuvaj_prostorije()


