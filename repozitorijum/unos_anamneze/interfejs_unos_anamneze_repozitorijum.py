from abc import ABC, abstractmethod


class InterfejsUnosAnamnezeRepo(ABC):

    @abstractmethod
    def pronadji_anamnezu_za_pacijenta(self, pacijent):
        pass

    @abstractmethod
    def sacuvaj_anamnezu(self, unos_anamneze_dto):
        pass
