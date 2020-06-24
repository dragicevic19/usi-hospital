from abc import ABC, abstractmethod


class InterfejsKalendarRepozitorijum(ABC):

    @abstractmethod
    def vrati_zauzeca_za_datum_i_sobu(self, datum, sprat, broj_prostorije):
        pass

    @abstractmethod
    def dodaj_dogadjaj(self, dogadjaj):
        pass

    @abstractmethod
    def slobodna_prostorija_za_period(self, renoviranjeDTO):
        pass

    @abstractmethod
    def kreiraj_listu_zauzeca_lekara(self, lekar, datum_od):
        pass

    @abstractmethod
    def vrati_vremenske_slotove(self):
        pass

    @abstractmethod
    def vrati_listu_dogadjaja(self):
        pass

    @abstractmethod
    def vrati_listu_proslih_dogadjaja(self):
        pass
