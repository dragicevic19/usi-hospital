import csv
from pathlib import Path
import datetime

from model.kalendarski_dogadjaj import KalendarskiDogadjaj
from model.konstante.konstante import PATH_TO_DOGADJAJI

lista_dogadjaja = []
lista_proslih_dogadjaja = []

vremenski_slotovi = ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00',
                     '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30',
                     '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00',
                     '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30',
                     '22:00', '22:30', '23:00', '23:30', "         ", "         "]


class KalendarRepozitorijum:
    @staticmethod
    def ucitaj_dogadjaje():
        path = Path(PATH_TO_DOGADJAJI)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                dogadjaj = KalendarskiDogadjaj(*red)
                KalendarRepozitorijum.rasporedi_dogadjaj_po_listama(dogadjaj)

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
        path = Path(PATH_TO_DOGADJAJI)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for dogadjaj in lista_dogadjaja:
                writer.writerow(dogadjaj.vrati_za_upis_u_fajl())
            for dogadjaj in lista_proslih_dogadjaja:
                writer.writerow(dogadjaj.vrati_za_upis_u_fajl())

    @staticmethod
    def vrati_zauzeca_za_datum_i_sobu(datum, sprat, broj_prostorije):
        lista_zauzeca = []
        dan, mes, god = datum.split("/")
        for dogadjaj in lista_dogadjaja:
            if dogadjaj.sprat == sprat and dogadjaj.broj_prostorije == broj_prostorije:
                for i in range(len(vremenski_slotovi) - 2):
                    sat, min = vremenski_slotovi[i].split(":")
                    datum_za_proveru = datetime.datetime(int(god), int(mes), int(dan), int(sat), int(min))
                    if dogadjaj.datum_vreme_zavrsetka > datum_za_proveru >= dogadjaj.datum_vreme:
                        lista_zauzeca.append(vremenski_slotovi[i])
        return lista_zauzeca

    @staticmethod
    def dodaj_dogadjaj(dogadjaj):
        lista_dogadjaja.append(dogadjaj)
        KalendarRepozitorijum.sacuvaj_dogadjaje()

    @staticmethod
    def slobodna_prostorija_za_period(novi_dogadjajDTO):
        danasnji_datum = datetime.datetime.now()
        for dogadjaj in lista_dogadjaja:
            if dogadjaj.prostorija == novi_dogadjajDTO.sprat_broj_prostorije:
                dana_do_dogadjaja = (novi_dogadjajDTO.pocetak_vreme_datum - danasnji_datum).days
                if not KalendarRepozitorijum.__proveri_dostupnost_prostorije(dogadjaj, novi_dogadjajDTO):
                    if dana_do_dogadjaja < 10 or not dogadjaj.zahvat or novi_dogadjajDTO.zahvat:
                        return False
        return True

    @staticmethod
    def __proveri_dostupnost_prostorije(dogadjaj, novi_dogadjajDTO):
        # pocetak = dogadjaj.datum_vreme.date()
        pocetak = dogadjaj.datum_vreme
        zavrsetak = pocetak + datetime.timedelta(minutes=30 * dogadjaj.broj_termina)
        pocetak_novog = novi_dogadjajDTO.pocetak_vreme_datum
        zavrsetak_novog = novi_dogadjajDTO.zavrsetak_vreme_datum

        if pocetak <= pocetak_novog <= zavrsetak:
            return False
        if pocetak <= zavrsetak_novog <= zavrsetak:
            return False
        if pocetak_novog <= pocetak and zavrsetak_novog >= zavrsetak:
            return False
        return True


KalendarRepozitorijum.ucitaj_dogadjaje()
KalendarRepozitorijum.sacuvaj_dogadjaje()
