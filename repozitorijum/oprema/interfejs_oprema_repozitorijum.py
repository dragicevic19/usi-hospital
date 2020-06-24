from abc import ABC, abstractmethod


class InterfejsOpremaRepo(ABC):

    @abstractmethod
    def nadji_po_nazivu_opreme(self, naziv_opreme):
        pass

    @abstractmethod
    def dodaj_opremu(self, oprema):
        pass

    @abstractmethod
    def brisanje_opreme(self, oprema):
        pass

    @abstractmethod
    def smanji_broj_slobodne_opreme(self, prostorija_za_izmenu):
        pass

    @abstractmethod
    def povecaj_broj_slobodne_opreme(self, naziv, broj_opreme):
        pass

    @abstractmethod
    def sacuvaj_bolnicku_opremu(self, oprema=None):
        pass

    @abstractmethod
    def vrati_nazive_bolnicke_opreme_u_sistemu(self):
        pass

