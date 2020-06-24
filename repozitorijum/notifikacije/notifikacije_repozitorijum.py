import csv
import datetime
from pathlib import Path

from model.kalendarski_dogadjaj import KalendarskiDogadjaj
from model.konstante.konstante import PUTANJA_FAJL_NOTIFIKACIJE
from repozitorijum.notifikacije.interfejs_notifikacije_repozitorijum import InterfejsNotifikacijeRepozitorijum


class NotifikacijeRepozitorijumImpl(InterfejsNotifikacijeRepozitorijum):

    def __init__(self):
        self._lista_notifikacija = []
        self._lista_proslih_notifikacija = []
        self.ucitaj_dogadjaje()

    def ucitaj_dogadjaje(self):
        path = Path(PUTANJA_FAJL_NOTIFIKACIJE)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                dogadjaj = KalendarskiDogadjaj(*red)
                self.rasporedi_dogadjaj_po_listama(dogadjaj)

    def rasporedi_dogadjaj_po_listama(self, dogadjaj):
        if dogadjaj.datum_vreme >= datetime.datetime.now():
            self._lista_notifikacija.append(dogadjaj)
        elif dogadjaj.datum_vreme_zavrsetka < datetime.datetime.now():
            self._lista_proslih_notifikacija.append(dogadjaj)
        else:
            self._lista_notifikacija.append(dogadjaj)

    def sacuvaj_dogadjaje(self):
        path = Path(PUTANJA_FAJL_NOTIFIKACIJE)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for notifikacija in self._lista_notifikacija:
                writer.writerow(notifikacija.vrati_za_upis_u_fajl())
            for notifikacija in self._lista_proslih_notifikacija:
                writer.writerow(notifikacija.vrati_za_upis_u_fajl())

    def posalji_notifikaciju(self, dogadjaj):
        self._lista_notifikacija.append(dogadjaj)
        self.sacuvaj_dogadjaje()

    def dobavi_sve_hitne_operacije(self):
        hitne_operacije = []
        for notifikacija in self._lista_notifikacija:
            if notifikacija.hitno:
                hitne_operacije.append(notifikacija)
        return hitne_operacije

    def brisi_selektovane_notifikacije(self, selektovane):
        for selektovana in selektovane:
            for notifikacija in self._lista_notifikacija:
                if selektovana.datum_pocetka == notifikacija.datum and \
                        selektovana.vreme_pocetka == notifikacija.vreme_pocetka_str and \
                        selektovana.prostorija == notifikacija.prostorija and \
                        selektovana.lekar in notifikacija.spisak_doktora and \
                        selektovana.pacijent == notifikacija.pacijent:

                    self._lista_notifikacija.remove(notifikacija)
        self.sacuvaj_dogadjaje()
