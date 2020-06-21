from abc import ABC, abstractmethod


class InterfejsIzvestajRepozitorijum(ABC):

    @abstractmethod
    def generisi_izvestaj_upravnik(self, string_za_upis, tip_izvestaja):
        pass

    @abstractmethod
    def generisi_izvestaj_lekar(self, string_za_upis):
        pass
