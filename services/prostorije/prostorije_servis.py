from repository.prostorije.prostorije_repozitorijum import ProstorijeRepository
from services.kalendar.kalendar_servis import KalendarServis
from services.oprema.oprema_servis import OpremaService


class ProstorijeService(object):

    @staticmethod
    def dodavanje_prostorije(prostorija):
        ProstorijeRepository.dodaj_prostoriju(prostorija)

    @staticmethod
    def brisanje_prostorije(prostorija):
        prostorija._obrisana = True
        ProstorijeRepository.sacuvaj_prostorije()

    @staticmethod
    def pretraga_prostorije():
        pass

    @staticmethod
    def renoviranje_prostorije(prostorija):
        pass

    @staticmethod
    def izmeni_namenu(renoviranjeDTO):
        if KalendarServis.dodaj_dogadjaj_ako_je_slobodna(renoviranjeDTO):
            prostorija = renoviranjeDTO.objekat_prostorije
            prostorija._namena_prostorije = renoviranjeDTO.nova_namena
            ProstorijeRepository.sacuvaj_prostorije()
            return True
        else:
            return False

    @staticmethod
    def ostale_renovacije(renoviranjeDTO):
        if KalendarServis.dodaj_dogadjaj_ako_je_slobodna(renoviranjeDTO):
            ProstorijeRepository.sacuvaj_prostorije()
            return True
        else:
            return False

    @staticmethod
    def dodavanje_slobodne_opreme_u_prostoriju(lista_renoviranjaDTO):

        if KalendarServis.dodaj_dogadjaj_ako_je_slobodna(lista_renoviranjaDTO[0]):
            for renoviranjeDTO in lista_renoviranjaDTO:
                prostorija_za_izmenu = renoviranjeDTO.objekat_prostorije
                ProstorijeService.__dodavanje_opreme(renoviranjeDTO, prostorija_za_izmenu)
                OpremaService.smanji_broj_slobodne_opreme(renoviranjeDTO)
                ProstorijeRepository.sacuvaj_prostorije()
            return True
        else:
            return False

    @staticmethod
    def __dodavanje_opreme(prostorijaDTO, prostorija_za_izmenu):
        stara_oprema = False
        for naziv, broj_opreme in prostorija_za_izmenu.get_spisak_opreme().items():
            if naziv == prostorijaDTO.naziv_opreme:
                stara_oprema = True
                broj_opreme += prostorijaDTO.broj_opreme
                prostorija_za_izmenu.promena_opreme(naziv, broj_opreme)

        if not stara_oprema:
            prostorija_za_izmenu.promena_opreme(prostorijaDTO.naziv_opreme, prostorijaDTO.broj_opreme)

    @staticmethod
    def izbacivanje_opreme_iz_prostorije(lista_prostorijaDTO):  # razlikuje se od dodavanje opreme samo u 2 linije,  da li refaktorisati?
        if KalendarServis.dodaj_dogadjaj_ako_je_slobodna(lista_prostorijaDTO[0]):
            for prostorijaDTO in lista_prostorijaDTO:
                prostorija_za_izmenu = prostorijaDTO.objekat_prostorije
                ProstorijeService.__izbacivanje_opreme(prostorijaDTO, prostorija_za_izmenu)  # 1
                OpremaService.povecaj_broj_slobodne_opreme(prostorijaDTO)                    # 2
                ProstorijeRepository.sacuvaj_prostorije()
            return True
        else:
            return False

    @staticmethod
    def __izbacivanje_opreme(prostorijaDTO, prostorija_za_izmenu):
        for naziv, broj_opreme in prostorija_za_izmenu.get_spisak_opreme().items():
            if naziv == prostorijaDTO.naziv_opreme:
                broj_opreme -= prostorijaDTO.broj_opreme
                prostorija_za_izmenu.promena_opreme(naziv, broj_opreme)
