



class ZauzecaProstorijaServis:
    def __init__(self,kalendar_servis,prostorije_servis):
        self._kalendar_servis = kalendar_servis
        self._prostorije_servis = prostorije_servis

    def zauzece_prostorije_od_do(self, dto_prenosa):
        lista_prostorija_za_prikaz = []
        for prostorija in self._prostorije_servis.prikupi_prostorije_za_prikaz():
            if prostorija.ima_svu_trazenu_opremu(dto_prenosa.spisak_zahtevane_opreme):
                if self.da_li_je_slobodna(prostorija, dto_prenosa.pocetno_vreme, dto_prenosa.krajnje_vreme):
                    lista_prostorija_za_prikaz.append(prostorija)
        return lista_prostorija_za_prikaz

    def da_li_je_slobodna(self, prostorija, vreme_od, vreme_do):
        lista_dogadjaja = self._kalendar_servis.dobavi_listu_dogadjaja()
        for dogadjaj in lista_dogadjaja:
            if dogadjaj.sprat == prostorija.get_sprat() and dogadjaj.broj_prostorije == prostorija.get_broj_prostorije():
                if vreme_od < dogadjaj.datum_vreme < vreme_do:
                    return False
        return True
