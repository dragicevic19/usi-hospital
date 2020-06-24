from abc import ABC, abstractmethod


class InterfejsKalendarRepozitorijum(ABC):

    @abstractmethod
    def vrati_zauzeca_za_datum_i_sobu(self, datum, sprat, broj_prostorije):
        pass

    @abstractmethod
    def vrati_zauzeca_za_datum_i_lekara(self, datum, lekar):
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
    @abstractmethod
    def vrati_slobodne_termine_lekara_za_datum(self,datum,lekar):
        pass

    @abstractmethod
    def vrati_radne_slotove_za_lekara(self, lekar):
        pass

    @abstractmethod
    def vrati_vremenske_slotovo_od_do(self, pocetni, krajnji):
        pass

    @abstractmethod
    def da_li_lekar_radi_u_zeljenim_slotovima(self, zeljeni_slotovi, lekar):
        pass
