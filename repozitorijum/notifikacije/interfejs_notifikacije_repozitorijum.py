from abc import ABC, abstractmethod


class InterfejsNotifikacijeRepozitorijum(ABC):

    @abstractmethod
    def posalji_notifikaciju(self, dogadjaj):
        pass
