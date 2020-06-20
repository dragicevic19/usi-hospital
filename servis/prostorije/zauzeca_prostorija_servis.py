from repozitorijum.prostorije.prostorije_repozitorijum import *
<<<<<<< HEAD:servisi/prostorije/zauzeca_prostorija_servis.py
=======
from repozitorijum.kalendar.kalendar_repozitorijum import lista_dogadjaja
>>>>>>> 7902c8fab737ed47f2caeb2f3f5f755d7db8fbc9:servis/prostorije/zauzeca_prostorija_servis.py

from repozitorijum.kalendar.kalendar_repozitorijum import lista_dogadjaja,lista_proslih_dogadjaja





class ZauzecaProstorijaServis:

    def zauzece_prostorije_od_do(self, dto_prenosa):

        lista_prostorija_za_prikaz = []
        for prostorija in lista_ucitanih_prostorija:
            if prostorija.ima_svu_trazenu_opremu(dto_prenosa.spisak_zahtevane_opreme):


                if self.da_li_je_slobodna(prostorija, dto_prenosa.pocetno_vreme, dto_prenosa.krajnje_vreme):

                    lista_prostorija_za_prikaz.append(prostorija)

        return lista_prostorija_za_prikaz

<<<<<<< HEAD:servisi/prostorije/zauzeca_prostorija_servis.py
    def da_li_je_slobodna(self, prostorija, vremeod, vremedo):
        lista = lista_proslih_dogadjaja+lista_dogadjaja
        for dogadjaj in lista:
=======
    def da_li_je_slobodna(self, prostorija, vreme_od, vreme_do):
        for dogadjaj in lista_dogadjaja:
>>>>>>> 7902c8fab737ed47f2caeb2f3f5f755d7db8fbc9:servis/prostorije/zauzeca_prostorija_servis.py
            if dogadjaj.sprat == prostorija.get_sprat() and dogadjaj.broj_prostorije == prostorija.get_broj_prostorije():
                if vreme_od < dogadjaj.datum_vreme < vreme_do:
                    return False
        return True
