from repozitorijum.prostorije.prostorije_repozitorijum import *
from repozitorijum.kalendar.kalendar_repozitorijum import lista_dogadjaja

# ProstorijeRepository.ucitavanje_prostorije()


class ZauzecaProstorijaServis:

    def zauzece_prostorije_od_do(self, dto_prenosa):
        lista_prostorija_za_prikaz = []
        for prostorija in _lista_ucitanih_prostorija:
            if prostorija.sadrzi_opremu(dto_prenosa.spisak_zahtevane_opreme):
                if self.da_li_je_slobodna(prostorija, dto_prenosa.pocetno_vreme, dto_prenosa.krajnje_vreme):
                    lista_prostorija_za_prikaz.append(prostorija)

        return lista_prostorija_za_prikaz

    def da_li_je_slobodna(self, prostorija, vreme_od, vreme_do):
        for dogadjaj in lista_dogadjaja:
            if dogadjaj.sprat == prostorija.get_sprat() and dogadjaj.broj_prostorije == prostorija.get_broj_prostorije():
                if vreme_od < dogadjaj.datum_vreme < vreme_do:
                    return False
        return True
