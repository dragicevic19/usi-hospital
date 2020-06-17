import csv
from pathlib import Path
import datetime

from model.enum.renoviranje import TipZahvata
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
    def sacuvaj_dogadjaj():
        path = Path(PATH_TO_DOGADJAJI)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for dogadjaj in lista_proslih_dogadjaja:
                writer.writerow(dogadjaj.vrati_za_upis_u_fajl())
            for dogadjaj in lista_dogadjaja:
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
        KalendarRepozitorijum.sacuvaj_dogadjaj()

    @staticmethod
    def slobodna_prostorija_za_period(renoviranjeDTO):
        danasnji_datum = datetime.date.today()
        for dogadjaj in lista_dogadjaja:
            if dogadjaj.prostorija == renoviranjeDTO.sprat_broj_prostorije:
                dana_do_renoviranja = (renoviranjeDTO.datum_pocetkaDate - danasnji_datum).days
                if dana_do_renoviranja < 10:  # proverava samo da li ima operacija ili pregleda za narednih 10ak dana
                    # koji upadaju u termin renoviranja, za ostale ima vremena da se prebaci npr operacija u drugu prostoriju
                    if not KalendarRepozitorijum.__proveri_dostupnost_prostorije(dogadjaj, renoviranjeDTO):
                        return False
                else:
                    if not KalendarRepozitorijum.__proveri_dostupnost_prostorije(dogadjaj, renoviranjeDTO):
                        if not dogadjaj.zahvat:
                            return False
        return True

    @staticmethod
    def __proveri_dostupnost_prostorije(dogadjaj, renoviranjeDTO):
        pocetak = dogadjaj.datum_vreme.date()
        zavrsetak = pocetak + datetime.timedelta(minutes=30 * dogadjaj.broj_termina)
        datum_pocetka = renoviranjeDTO.datum_pocetkaDate
        datum_zavrsetka = renoviranjeDTO.datum_zavrsetkaDate
        if pocetak <= datum_pocetka <= zavrsetak:
            return False
        if pocetak <= datum_zavrsetka <= zavrsetak:
            return False
        if datum_pocetka <= pocetak and datum_zavrsetka >= zavrsetak:
            return False
        return True

    @staticmethod
    def kreiraj_listu_zauzeca_lekara(lekar, datum_od):
        lista_zauzeca = []
        for dogadjaj in lista_proslih_dogadjaja:
            if dogadjaj.datum_vreme > datum_od and lekar in dogadjaj.spisak_doktora:
                lista_zauzeca.append(dogadjaj)
        return lista_zauzeca


KalendarRepozitorijum.ucitaj_dogadjaje()
lista_dogadjaja.sort(key=lambda d: d.datum_vreme)
lista_proslih_dogadjaja.sort(key=lambda d: d.datum_vreme)
KalendarRepozitorijum.sacuvaj_dogadjaj()
