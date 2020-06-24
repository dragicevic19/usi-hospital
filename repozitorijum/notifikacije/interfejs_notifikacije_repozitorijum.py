from abc import ABC, abstractmethod


class InterfejsNotifikacijeRepozitorijum(ABC):

    @abstractmethod
    def posalji_notifikaciju(self, dogadjaj):
        pass

    @abstractmethod
    def brisi_selektovane_notifikacije(self, selektovane):
        pass
