from model.prostorija import Prostorija
from repozitorijum.kalendar.kalendar_repozitorijum import KalendarRepozitorijumImpl
from repozitorijum.oprema.oprema_repozitorijum_impl import OpremaRepozitorijumImpl
from repozitorijum.prostorije.prostorije_repozitorijum import ProstorijeRepozitorijumImpl
from servis.kalendar.kalendar_servis import KalendarServis


class ProstorijeServis(object):

    def __init__(self, repo_prostorije=ProstorijeRepozitorijumImpl(), repo_oprema=OpremaRepozitorijumImpl(),repo_kalendar = KalendarRepozitorijumImpl()):
        self._repo_prostorije = repo_prostorije
        self._repo_oprema = repo_oprema
        self._repo_kalendar = repo_kalendar

    def dodavanje_prostorije(self, prostorija):
        self._repo_prostorije.dodaj_prostoriju(prostorija)

    def brisanje_prostorije(self, prostorija):
        prostorija._obrisana = True
        self._repo_prostorije.sacuvaj_prostorije()

    def pretraga_prostorije(self):
        pass

    def renoviranje_prostorije(self, prostorija):
        pass

    def izmeni_namenu(self, renoviranjeDTO):
        if KalendarServis().dodaj_dogadjaj_ako_je_slobodna(renoviranjeDTO):
            prostorija = renoviranjeDTO.prostorija
            prostorija._namena_prostorije = renoviranjeDTO.nova_namena
            self._repo_prostorije.sacuvaj_prostorije()
            return True
        else:
            return False

    def ostale_renovacije(self, renoviranjeDTO):
        if KalendarServis().dodaj_dogadjaj_ako_je_slobodna(renoviranjeDTO):
            self._repo_prostorije.sacuvaj_prostorije()
            return True
        else:
            return False

    def dodavanje_slobodne_opreme_u_prostoriju(self, lista_renoviranjaDTO):

        if KalendarServis().dodaj_dogadjaj_ako_je_slobodna(lista_renoviranjaDTO[0]):
            for renoviranjeDTO in lista_renoviranjaDTO:
                prostorija_za_izmenu = renoviranjeDTO.prostorija
                self.__dodavanje_opreme(renoviranjeDTO, prostorija_za_izmenu)
                self._repo_oprema.smanji_broj_slobodne_opreme(renoviranjeDTO)
                self._repo_prostorije.sacuvaj_prostorije()
            return True
        else:
            return False

    def __dodavanje_opreme(self, renoviranjeDTO, prostorija_za_izmenu):
        stara_oprema = False
        for naziv, broj_opreme in prostorija_za_izmenu.get_spisak_opreme().items():
            if naziv == renoviranjeDTO.naziv_opreme:
                stara_oprema = True
                broj_opreme += renoviranjeDTO.broj_opreme
                prostorija_za_izmenu.promena_opreme(naziv, broj_opreme)
        if not stara_oprema:
            prostorija_za_izmenu.promena_opreme(renoviranjeDTO.naziv_opreme, renoviranjeDTO.broj_opreme)

    def izbacivanje_opreme_iz_prostorije(self, lista_renoviranjaDTO):
        # razlikuje se od dodavanje opreme samo u 2 linije,  da li refaktorisati?
        if KalendarServis().dodaj_dogadjaj_ako_je_slobodna(lista_renoviranjaDTO[0]):
            for renoviranjeDTO in lista_renoviranjaDTO:
                prostorija_za_izmenu = renoviranjeDTO.prostorija
                self.__izbacivanje_opreme(renoviranjeDTO, prostorija_za_izmenu)  # 1
                self._repo_oprema.povecaj_broj_slobodne_opreme(renoviranjeDTO.naziv_opreme,
                                                               renoviranjeDTO.broj_opreme)  # 2
                self._repo_prostorije.sacuvaj_prostorije()
            return True
        else:
            return False

    def __izbacivanje_opreme(self, renoviranjeDTO, prostorija_za_izmenu):
        for naziv, broj_opreme in prostorija_za_izmenu.get_spisak_opreme().items():
            if naziv == renoviranjeDTO.naziv_opreme:
                broj_opreme -= renoviranjeDTO.broj_opreme
                prostorija_za_izmenu.promena_opreme(naziv, broj_opreme)

    def obrisi_sobe(self, *args):
        self._repo_prostorije.obrisi_sobe(*args)

    def slobodan_broj_prostorije(self, sprat, novi_broj):
        if self._repo_prostorije.vrati_prostoriju_po_broju_i_spratu(sprat, novi_broj):
            return False
        return True

    def spajanje_prostorija(self, prva_prostorijaDTO, druga_prostorijaDTO):
        prostorija1 = prva_prostorijaDTO.prostorija
        prostorija2 = druga_prostorijaDTO.prostorija
        if KalendarServis().dodaj_dogadjaj_ako_je_slobodna(
                prva_prostorijaDTO):  # todo: da li da pravim dogadjaj za ove dve stare prostorije koje se brisu ili za novu?
            if KalendarServis().dodaj_dogadjaj_ako_je_slobodna(druga_prostorijaDTO):
                spisak_opreme = self.napravi_spisak_opreme(prostorija1, prostorija2)
                nova = Prostorija(prostorija1.get_sprat(), prva_prostorijaDTO.novi_broj_prostorije,
                                  spisak_opreme, prva_prostorijaDTO.nova_namena)

                self.dodavanje_prostorije(nova)
                return True
        return False

    def napravi_spisak_opreme(self, prostorija1, prostorija2):
        novi_spisak = {}
        for naziv, broj_opreme in prostorija1.get_spisak_opreme().items():
            novi_spisak[naziv] = broj_opreme

        for naziv, broj_opreme in prostorija2.get_spisak_opreme().items():
            if naziv in novi_spisak:
                novi_spisak[naziv] += broj_opreme
            else:
                novi_spisak[naziv] = broj_opreme
        return novi_spisak

    def deljenje_prostorije(self, lista_deljenjeDTO):
        prostorija_za_deljenje = lista_deljenjeDTO[0]
        if KalendarServis().dodaj_dogadjaj_ako_je_slobodna(prostorija_za_deljenje):
            oprema_za_prvu, oprema_za_drugu = self.podeli_opremu_po_prostorijama(lista_deljenjeDTO)
            self.napravi_prostorije(oprema_za_drugu, oprema_za_prvu, prostorija_za_deljenje)
            return True
        else:
            return False

    def napravi_prostorije(self, oprema_za_drugu, oprema_za_prvu, prostorija_za_deljenje):
        sprat = prostorija_za_deljenje.stara_prostorija.get_sprat()
        p1 = Prostorija(sprat, prostorija_za_deljenje.broj_prve_prostorije, oprema_za_prvu,
                        prostorija_za_deljenje.namena_prve)
        p2 = Prostorija(sprat, prostorija_za_deljenje.broj_druge_prostorije, oprema_za_drugu,
                        prostorija_za_deljenje.namena_druge)
        self.dodavanje_prostorije(p1)
        self.dodavanje_prostorije(p2)

    def podeli_opremu_po_prostorijama(self, lista_deljenjeDTO):
        oprema_za_prvu = {}
        oprema_za_drugu = {}
        for deljenjeDTO in lista_deljenjeDTO:
            oprema_za_prvu[deljenjeDTO.naziv_opreme] = deljenjeDTO.broj_opreme_prva
            oprema_za_drugu[deljenjeDTO.naziv_opreme] = deljenjeDTO.broj_opreme_druga
            if deljenjeDTO.visak_opreme:
                self._repo_oprema.povecaj_broj_slobodne_opreme(deljenjeDTO.naziv_opreme,
                                                               deljenjeDTO.visak_opreme)
        return oprema_za_prvu, oprema_za_drugu

    def obrisi_opremu_iz_prostorija(self, naziv_opreme_odabrane):
        self._repo_prostorije.brisanje_opreme_iz_prostorija(naziv_opreme_odabrane)

    def prikupi_prostorije_za_prikaz(self):
        return self._repo_prostorije.vrati_listu_prostorija_za_prikaz()

    def vrati_string_opreme_za_prostoriju(self, prostorija):
        return self._repo_prostorije.pretvori_opremu_iz_prostorije_u_string(prostorija)

    # VRACA FALSE AKO NE POSTOJI!
    def pronadji_prostoriju(self, sprat, broj_sobe):
        return self._repo_prostorije.vrati_prostoriju_po_broju_i_spratu(sprat, broj_sobe)

    def pronadji_prostorije_po_nameni(self, namena_prostorije):
        return self._repo_prostorije.pronadji_prostorije_po_nameni(namena_prostorije)

    @staticmethod
    def zakazivanje_operacije_i_pregleda(zakazivanje_operacijeDTO):
        if KalendarServis().dodaj_dogadjaj_ako_je_slobodna(zakazivanje_operacijeDTO):
            return True
        else:
            return False

