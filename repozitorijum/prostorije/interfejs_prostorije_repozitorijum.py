from abc import ABC, abstractmethod


class InterfejsProstorijeRepo(ABC):

    @abstractmethod
    def dodaj_prostoriju(self, prostorija):
        pass

    @abstractmethod
    def sacuvaj_prostorije(self):
        pass

    @abstractmethod
    def pretvori_opremu_iz_prostorije_u_string(self, prostorija):
        pass

    @abstractmethod
    def vrati_prostoriju_po_broju_i_spratu(self, sprat, broj_sobe):
        pass

    @abstractmethod
    def obrisi_sobe(self, *prostorije_za_brisanje):
        pass

    @abstractmethod
    def brisanje_opreme_iz_prostorija(self, naziv_opreme):
        pass

    @abstractmethod
    def vrati_listu_prostorija_za_prikaz(self):
        pass
