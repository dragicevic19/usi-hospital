import csv
import datetime
from pathlib import Path

from model.konstante.konstante import PUTANJA_FAJL_ZAHTEVI_ZA_PREGLED
from model.zahtev_za_pregled import ZahtevZaPregled
from repozitorijum.zahtevi_za_pregled.interfejs_zahtevi_za_pregled_repozitorijum import InterfejsZahteviZaPregledRepozitorijum


class ZahtevZaPregledRepozitorijumImpl(InterfejsZahteviZaPregledRepozitorijum):

    def __init__(self):
        self._lista_zahteva = []
        self._lista_proslih_zahteva = []
        self.ucitaj_dogadjaje()

    def ucitaj_dogadjaje(self):
        path = Path(PUTANJA_FAJL_ZAHTEVI_ZA_PREGLED)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                dogadjaj = ZahtevZaPregled(*red)
                self.rasporedi_dogadjaj_po_listama(dogadjaj)

    def rasporedi_dogadjaj_po_listama(self, dogadjaj):
        if dogadjaj.resen:
            self._lista_proslih_zahteva.append(dogadjaj)
        if dogadjaj.pocetni_datum >= datetime.datetime.now():
            self._lista_zahteva.append(dogadjaj)
        elif dogadjaj.krajnji_datum < datetime.datetime.now():
            self._lista_proslih_zahteva.append(dogadjaj)
        else:
            self._lista_zahteva.append(dogadjaj)

    def sacuvaj_dogadjaje(self):
        path = Path(PUTANJA_FAJL_ZAHTEVI_ZA_PREGLED)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for dogadjaj in self._lista_zahteva:
                writer.writerow(dogadjaj.vrati_za_upis_u_fajl())
            for dogadjaj in self._lista_proslih_zahteva:
                writer.writerow(dogadjaj.vrati_za_upis_u_fajl())

    def posalji_zahtev_za_pregled(self, dogadjaj):
        self._lista_zahteva.append(dogadjaj)
        self.sacuvaj_dogadjaje()
