import csv
import datetime
from pathlib import Path

from model.kalendarski_dogadjaj import KalendarskiDogadjaj


class DogadjajRepozitorijum(object):

    @staticmethod
    def ucitaj_dogadjaje(putanja, lista_dogadjaja, lista_proslih_dogadjaja):
        path = Path(putanja)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                dogadjaj = KalendarskiDogadjaj(*red)
                DogadjajRepozitorijum.rasporedi_dogadjaj_po_listama(dogadjaj, lista_dogadjaja, lista_proslih_dogadjaja)

    @staticmethod
    def rasporedi_dogadjaj_po_listama(dogadjaj, lista_dogadjaja, lista_proslih_dogadjaja):
        if dogadjaj.datum_vreme >= datetime.datetime.now():
            lista_dogadjaja.append(dogadjaj)
        elif dogadjaj.datum_vreme_zavrsetka < datetime.datetime.now():
            lista_proslih_dogadjaja.append(dogadjaj)
        else:
            lista_dogadjaja.append(dogadjaj)

    @staticmethod
    def sacuvaj_dogadjaj(putanja, lista_dogadjaja, lista_proslih_dogadjaja):
        path = Path(putanja)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for dogadjaj in lista_dogadjaja:
                writer.writerow(dogadjaj.vrati_za_upis_u_fajl())
            for dogadjaj in lista_proslih_dogadjaja:
                writer.writerow(dogadjaj.vrati_za_upis_u_fajl())
