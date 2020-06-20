from abc import ABC, abstractmethod


class InterfejsKorisnikRepo(ABC):

    @abstractmethod
    def nadji_po_korisnickom_imenu(self, korisnicko_ime):
        pass

    @abstractmethod
    def obrisi_korisnika(self, korisnik):
        pass

    @abstractmethod
    def dodaj_korisnika(self, korisnik):
        pass

    @abstractmethod
    def sacuvaj_korisnike(self):
        pass

    @abstractmethod
    def vrati_spisak_pacijenata_po_lekaru(self, ulogovan_lekar):
        pass

    @abstractmethod
    def dodaj_id_anamneze_pacijentu(self,pacijent, id_anamneze):
        pass

    @abstractmethod
    def vrati_listu_korisnika(self):
        pass