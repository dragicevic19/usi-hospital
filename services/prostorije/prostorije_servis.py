from model.prostorija import Prostorija
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
            prostorija = renoviranjeDTO.prostorija
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
                prostorija_za_izmenu = renoviranjeDTO.prostorija
                ProstorijeService.__dodavanje_opreme(renoviranjeDTO, prostorija_za_izmenu)
                OpremaService.smanji_broj_slobodne_opreme(renoviranjeDTO)
                ProstorijeRepository.sacuvaj_prostorije()
            return True
        else:
            return False

    @staticmethod
    def __dodavanje_opreme(renoviranjeDTO, prostorija_za_izmenu):
        stara_oprema = False
        for naziv, broj_opreme in prostorija_za_izmenu.get_spisak_opreme().items():
            if naziv == renoviranjeDTO.naziv_opreme:
                stara_oprema = True
                broj_opreme += renoviranjeDTO.broj_opreme
                prostorija_za_izmenu.promena_opreme(naziv, broj_opreme)

        if not stara_oprema:
            prostorija_za_izmenu.promena_opreme(renoviranjeDTO.naziv_opreme, renoviranjeDTO.broj_opreme)

    @staticmethod
    def izbacivanje_opreme_iz_prostorije(lista_renoviranjaDTO):
        # razlikuje se od dodavanje opreme samo u 2 linije,  da li refaktorisati?

        if KalendarServis.dodaj_dogadjaj_ako_je_slobodna(lista_renoviranjaDTO[0]):
            for renoviranjeDTO in lista_renoviranjaDTO:
                prostorija_za_izmenu = renoviranjeDTO.prostorija
                ProstorijeService.__izbacivanje_opreme(renoviranjeDTO, prostorija_za_izmenu)  # 1
                OpremaService.povecaj_broj_slobodne_opreme(renoviranjeDTO)  # 2
                ProstorijeRepository.sacuvaj_prostorije()
            return True
        else:
            return False

    @staticmethod
    def __izbacivanje_opreme(renoviranjeDTO, prostorija_za_izmenu):
        for naziv, broj_opreme in prostorija_za_izmenu.get_spisak_opreme().items():
            if naziv == renoviranjeDTO.naziv_opreme:
                broj_opreme -= renoviranjeDTO.broj_opreme
                prostorija_za_izmenu.promena_opreme(naziv, broj_opreme)

    @staticmethod
    def slobodan_broj_prostorije(prostorija1, prostorija2, novi_broj):
        ProstorijeRepository.obrisi_sobe(prostorija1, prostorija2)
        sprat = prostorija1.get_sprat()
        if ProstorijeRepository.vrati_prostoriju_po_broju_i_spratu(sprat, novi_broj):
            return False
        return True

    @staticmethod
    def spajanje_prostorija(prva_prostorijaDTO, druga_prostorijaDTO):
        prostorija1 = prva_prostorijaDTO.prostorija
        prostorija2 = druga_prostorijaDTO.prostorija
        if KalendarServis.dodaj_dogadjaj_ako_je_slobodna(prva_prostorijaDTO):   # todo: da li da pravim dogadjaj za ove dve stare prostorije koje se brisu ili za novu?
            if KalendarServis.dodaj_dogadjaj_ako_je_slobodna(druga_prostorijaDTO):
                spisak_opreme = ProstorijeService.napravi_spisak_opreme(prostorija1, prostorija2)
                nova = Prostorija(prostorija1.get_sprat(), prva_prostorijaDTO.novi_broj_prostorije,
                                  spisak_opreme, prva_prostorijaDTO.nova_namena)

                ProstorijeService.dodavanje_prostorije(nova)
                return True
        return False

    @staticmethod
    def napravi_spisak_opreme(prostorija1, prostorija2):
        novi_spisak = {}
        for naziv, broj_opreme in prostorija1.get_spisak_opreme().items():
            novi_spisak[naziv] = broj_opreme

        for naziv, broj_opreme in prostorija2.get_spisak_opreme().items():
            if naziv in novi_spisak:
                novi_spisak[naziv] += broj_opreme
            else:
                novi_spisak[naziv] = broj_opreme
        return novi_spisak
