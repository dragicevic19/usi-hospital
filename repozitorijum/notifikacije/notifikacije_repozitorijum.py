import csv
import datetime
from pathlib import Path

from model.kalendarski_dogadjaj import KalendarskiDogadjaj
from model.konstante.konstante import PATH_TO_NOTIFIKACIJE

lista_dogadjaja = []
lista_proslih_dogadjaja = []


class NotifikacijeRepozitorijum:

    @staticmethod
    def ucitaj_dogadjaje():
        path = Path(PATH_TO_NOTIFIKACIJE)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                dogadjaj = KalendarskiDogadjaj(*red)
                NotifikacijeRepozitorijum.rasporedi_dogadjaj_po_listama(dogadjaj)

    @staticmethod
    def rasporedi_dogadjaj_po_listama(dogadjaj):
        if dogadjaj.datum_vreme >= datetime.datetime.now():
            lista_dogadjaja.append(dogadjaj)
        elif dogadjaj.datum_vreme_zavrsetka < datetime.datetime.now():
            lista_proslih_dogadjaja.append(dogadjaj)
        else:
            lista_dogadjaja.append(dogadjaj)

    @staticmethod
    def sacuvaj_dogadjaje():
        path = Path(PATH_TO_NOTIFIKACIJE)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for dogadjaj in lista_dogadjaja:
                writer.writerow(dogadjaj.vrati_za_upis_u_fajl())
            for dogadjaj in lista_proslih_dogadjaja:
                writer.writerow(dogadjaj.vrati_za_upis_u_fajl())

    @staticmethod
    def posalji_notifikaciju(dogadjaj):
        lista_dogadjaja.append(dogadjaj)
        NotifikacijeRepozitorijum.sacuvaj_dogadjaje()


NotifikacijeRepozitorijum.ucitaj_dogadjaje()
