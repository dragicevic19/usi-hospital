from services.file.file_servis import FileService
from repository.prostorije.prostorije_repozitorijum import lista_ucitanih_prostorija


class ProstorijeService(object):

    @staticmethod
    def dodavanje_prostorije(prostorija):
        lista_ucitanih_prostorija.append(prostorija)
        FileService.sacuvaj_entitete()

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
