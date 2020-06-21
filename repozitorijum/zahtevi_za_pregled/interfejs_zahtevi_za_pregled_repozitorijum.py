from abc import ABC, abstractmethod


class InterfejsZahteviZaPregledRepozitorijum(ABC):

    @abstractmethod
    def posalji_zahtev_za_pregled(self, dogadjaj):
        pass
