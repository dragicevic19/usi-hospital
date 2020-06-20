from repozitorijum.prostorije.prostorije_repozitorijum import *
from model.DTO.prenos_prostorija import PretragaProstorijaDTO
<<<<<<< HEAD:services/prostorije/zauzeca_prostorija_servis.py
from repository.kalendar.kalendar_repozitorijum import lista_dogadjaja,lista_proslih_dogadjaja
=======
from repozitorijum.kalendar.kalendar_repozitorijum import lista_dogadjaja
>>>>>>> 47c86f94e7cf1642cfccf26133699b4eb127ff20:servisi/prostorije/zauzeca_prostorija_servis.py

# ProstorijeRepository.ucitavanje_prostorije()


class ZauzecaProstorijaServis:

    def zauzece_prostorije_od_do(self, dto_prenosa):

        lista_prostorija_za_prikaz = []
        for prostorija in lista_ucitanih_prostorija:
            if prostorija.ima_svu_trazenu_opremu(dto_prenosa.spisak_zahtevane_opreme):


                if self.da_li_je_slobodna(prostorija, dto_prenosa.pocetno_vreme, dto_prenosa.krajnje_vreme):

                    lista_prostorija_za_prikaz.append(prostorija)

        return lista_prostorija_za_prikaz

    def da_li_je_slobodna(self, prostorija, vremeod, vremedo):
        lista = lista_proslih_dogadjaja+lista_dogadjaja
        for dogadjaj in lista:
            if dogadjaj.sprat == prostorija.get_sprat() and dogadjaj.broj_prostorije == prostorija.get_broj_prostorije():
                if dogadjaj.datum_vreme > vremeod and dogadjaj.datum_vreme < vremedo:
                    return False
        return True
