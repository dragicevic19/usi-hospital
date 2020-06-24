from repozitorijum.kalendar.interfejs_kalendar_repozitorijum import InterfejsKalendarRepozitorijum
from model.kalendarski_dogadjaj import KalendarskiDogadjaj
import datetime
from repozitorijum.korisnik.korisnik_repozitorijum import *


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

    def vrati_zauzeca_za_datum_i_lekara(self, datum, lekar):
        lista_zauzeca = []
        dan, mes, god = datum.split("/")
        for dogadjaj in self._lista_dogadjaja:
            if lekar in dogadjaj.spisak_doktora:
                for i in range(len(self._vremenski_slotovi) - 2):
                    sat, min = self._vremenski_slotovi[i].split(":")
                    datum_za_proveru = datetime.datetime(int(god), int(mes), int(dan), int(sat), int(min))
                    if dogadjaj.datum_vreme_zavrsetka > datum_za_proveru >= dogadjaj.datum_vreme:
                        lista_zauzeca.append(self._vremenski_slotovi[i])
        return lista_zauzeca

    def dodaj_dogadjaj(self, dogadjaj):
        self._lista_dogadjaja.append(dogadjaj)
        self.sacuvaj_dogadjaj()

    def slobodna_prostorija_za_period(self, novi_dogadjajDTO):
        danasnji_datum = datetime.datetime.now()
        for dogadjaj in self._lista_dogadjaja:
            if dogadjaj.prostorija == novi_dogadjajDTO.sprat_broj_prostorije:
                dana_do_dogadjaja = (novi_dogadjajDTO.pocetak_vreme_datum - danasnji_datum).days
                if not self.__proveri_dostupnost_prostorije(dogadjaj, novi_dogadjajDTO):
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
        if pocetak < pocetak_novog < zavrsetak:
            return False
        if pocetak < zavrsetak_novog < zavrsetak:
            return False
        if pocetak_novog < pocetak and zavrsetak_novog > zavrsetak:
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

    def dobavi_sve_renovacije(self):
        lista_renovacija = []
        for dogadjaj in self._lista_dogadjaja:
            if not dogadjaj.zahvat:
                lista_renovacija.append(dogadjaj)
        return lista_renovacija

    def brisi_selektovane_notifikacije(self, selektovane):
        for selektovana in selektovane:
            for dogadjaj in self._lista_dogadjaja:
                if selektovana.datum_pocetka == dogadjaj.datum and \
                        selektovana.vreme_pocetka == dogadjaj.vreme_pocetka_str and \
                        selektovana.prostorija == dogadjaj.prostorija and \
                        selektovana.lekar in dogadjaj.spisak_doktora and selektovana.pacijent == dogadjaj.pacijent:
                    self._lista_dogadjaja.remove(dogadjaj)
        self.sacuvaj_dogadjaj()

    def vrati_radne_slotove_za_lekara(self, lekar):
        radno_vreme = lekar.get_radno_vreme()
        pocetno, krajnje = radno_vreme.split("-")
        return self.vrati_vremenske_slotovo_od_do(pocetno, krajnje)

    def vrati_vremenske_slotovo_od_do(self, pocetni, krajnji):

        lista_slotova = []
        dodaj = False
        for i in self._vremenski_slotovi[:-2]:
            if pocetni == i:
                dodaj = True
            if krajnji == i:
                dodaj = False
            if dodaj:
                lista_slotova.append(i)
        return lista_slotova

    def vrati_slobodne_termine_lekara_za_datum(self, datum, lekar):
        lista_mogucnosti = self.vrati_radne_slotove_za_lekara(lekar)
        lista_zauzeca = self.vrati_zauzeca_za_datum_i_lekara(datum, lekar.get_korisnicko_ime())
        lista_slobodnih_termina = []
        for i in lista_mogucnosti:
            if i not in lista_zauzeca:
                lista_slobodnih_termina.append(i)
        return lista_slobodnih_termina

    def da_li_lekar_radi_u_zeljenim_slotovima(self, zeljeni_slotovi, lekar):
        radni_slotovi_lekara = self.vrati_radne_slotove_za_lekara(lekar)
        for vreme in radni_slotovi_lekara:
            if vreme in zeljeni_slotovi:
                return True
        return False
