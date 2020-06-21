from repozitorijum.kalendar.interfejs_kalendar_repozitorijum import InterfejsKalendarRepozitorijum
from model.kalendarski_dogadjaj import KalendarskiDogadjaj
from model.konstante.konstante import PUTANJA_FAJL_DOGADJAJI
from pathlib import Path
import datetime
import csv


class KalendarRepozitorijumImpl(InterfejsKalendarRepozitorijum):

    def __init__(self):
        self._lista_dogadjaja = []
        self._lista_proslih_dogadjaja = []
        self._vremenski_slotovi = ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00',
                                   '04:30',
                                   '05:00',
                                   '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30',
                                   '10:00',
                                   '10:30',
                                   '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00',
                                   '15:30',
                                   '16:00',
                                   '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30',
                                   '21:00',
                                   '21:30',
                                   '22:00', '22:30', '23:00', '23:30', "         ", "         "]
        self.ucitaj_dogadjaje()
        self._lista_dogadjaja.sort(key=lambda d: d.datum_vreme)
        self._lista_proslih_dogadjaja.sort(key=lambda d: d.datum_vreme)

    def ucitaj_dogadjaje(self):
        path = Path(PUTANJA_FAJL_DOGADJAJI)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                dogadjaj = KalendarskiDogadjaj(*red)
                self.rasporedi_dogadjaj_po_listama(dogadjaj)

    def rasporedi_dogadjaj_po_listama(self, dogadjaj):
        if dogadjaj.datum_vreme >= datetime.datetime.now():
            self._lista_dogadjaja.append(dogadjaj)
        elif dogadjaj.datum_vreme_zavrsetka < datetime.datetime.now():
            self._lista_proslih_dogadjaja.append(dogadjaj)
        else:
            self._lista_dogadjaja.append(dogadjaj)

    def sacuvaj_dogadjaj(self):
        path = Path(PUTANJA_FAJL_DOGADJAJI)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for dogadjaj in self._lista_proslih_dogadjaja:
                writer.writerow(dogadjaj.vrati_za_upis_u_fajl())
            for dogadjaj in self._lista_dogadjaja:
                writer.writerow(dogadjaj.vrati_za_upis_u_fajl())

    def vrati_zauzeca_za_datum_i_sobu(self, datum, sprat, broj_prostorije):
        lista_zauzeca = []
        dan, mes, god = datum.split("/")
        for dogadjaj in self._lista_dogadjaja:
            if dogadjaj.sprat == sprat and dogadjaj.broj_prostorije == broj_prostorije:
                for i in range(len(self._vremenski_slotovi) - 2):
                    sat, min = self._vremenski_slotovi[i].split(":")
                    datum_za_proveru = datetime.datetime(int(god), int(mes), int(dan), int(sat), int(min))
                    if dogadjaj.datum_vreme_zavrsetka > datum_za_proveru >= dogadjaj.datum_vreme:
                        lista_zauzeca.append(self._vremenski_slotovi[i])
        return lista_zauzeca

    def dodaj_dogadjaj(self, dogadjaj):
        self._lista_dogadjaja.append(dogadjaj)
        self.sacuvaj_dogadjaj()

    def slobodna_prostorija_za_period(self, renoviranjeDTO):
        danasnji_datum = datetime.date.today()
        for dogadjaj in self._lista_dogadjaja:
            if dogadjaj.prostorija == renoviranjeDTO.sprat_broj_prostorije:
                dana_do_renoviranja = (renoviranjeDTO.datum_pocetkaDate - danasnji_datum).days
                if dana_do_renoviranja < 10:  # proverava samo da li ima operacija ili pregleda za narednih 10ak dana
                    # koji upadaju u termin renoviranja, za ostale ima vremena da se prebaci npr operacija u drugu prostoriju
                    if not self.__proveri_dostupnost_prostorije(dogadjaj, renoviranjeDTO):
                        return False
                else:
                    if not self.__proveri_dostupnost_prostorije(dogadjaj, renoviranjeDTO):
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

    def kreiraj_listu_zauzeca_lekara(self, lekar, datum_od):
        lista_zauzeca = []
        for dogadjaj in self._lista_proslih_dogadjaja:
            if dogadjaj.datum_vreme > datum_od and lekar in dogadjaj.spisak_doktora:
                lista_zauzeca.append(dogadjaj)
        return lista_zauzeca

    def vrati_vremenske_slotove(self):
        return self._vremenski_slotovi

    def vrati_listu_dogadjaja(self):
        return self._lista_dogadjaja

    def vrati_listu_proslih_dogadjaja(self):
        return self._lista_proslih_dogadjaja
