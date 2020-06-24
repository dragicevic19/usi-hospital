from datetime import *
from repozitorijum.izvestaji.izvestaji_repozitorijum import IzvestajRepozitorijumImpl
from repozitorijum.kalendar.kalendar_repozitorijum import KalendarRepozitorijumImpl
from servis.korisnik.korisnik_servis import KorisnikServis


class SopstveniIzvestajLekaraServis:
    def __init__(self, ulogovani_lekar, broj_dana_za_izvestaj, repo_izvestaj=IzvestajRepozitorijumImpl(),
                 repo_kalendar=KalendarRepozitorijumImpl()):
        self._repo_izvestaj = repo_izvestaj
        self._repo_kalendar = repo_kalendar
        self._ulogovani_lekar = ulogovani_lekar
        self._broj_dana_za_izvestaj = broj_dana_za_izvestaj
        self._vremenski_period_izvestaja = timedelta(days=int(self._broj_dana_za_izvestaj))
        self._trenutni_datum = datetime.now()
        self._pocetni_datum = self._trenutni_datum - self._vremenski_period_izvestaja
        self.pripremi_izvestaj()


    def glavni_naslov(self):
        return "IZVESTAJ ZA LEKARA " + self._ulogovani_lekar + " I NJEGOVIH PACIJENATA U PRETHODNIH " + \
               str(self._broj_dana_za_izvestaj) + " DANA\n\n"

    @staticmethod
    def naslov_za_pacijente():
        return "\nPACIJENTI:\n\n"

    def formiraj_ispis_zauzeca(self):
        string_za_ispis = ""
        ukupno_zauzece = 0
        for dogadjaj in self._repo_kalendar.kreiraj_listu_zauzeca_lekara(self._ulogovani_lekar, self._pocetni_datum):
            vreme_zauzeca = int(dogadjaj.broj_termina * 30)
            string_za_ispis += "Datum: " + str(dogadjaj.datum_vreme) + " - Zauzece: " + str(
                vreme_zauzeca) + " minuta\n"
            ukupno_zauzece += vreme_zauzeca
        string_za_ispis += "Ukupan broj sati u prethodnih mesec dana za lekara " + self._ulogovani_lekar + " iznosi: " \
                           + str(ukupno_zauzece / 60) + "\n"
        return string_za_ispis

    def pripremi_izvestaj(self):
        sadrzaj = self.glavni_naslov() + self.formiraj_ispis_zauzeca() + self.naslov_za_pacijente() + \
                  self.formiraj_spisak_pacijenata()
        self._repo_izvestaj.generisi_izvestaj_lekar(sadrzaj)

    def formiraj_spisak_pacijenata(self):
        string_za_ispis = ""
        for pacijent in KorisnikServis().dobavi_spisak_pacijenata_po_lekaru(self._ulogovani_lekar):
            string_za_ispis += "Pacijent: " + pacijent.get_ime() + " " + pacijent.get_prezime() + \
                               " sa brojem zdravstvene knjizice:  " + pacijent.get_br_zdravstvene() + "\n"
        return string_za_ispis

def poziv_forme_za_prikaz_izvestaja( korisnik, broj_dana):
    kor_ime = korisnik.get_korisnicko_ime()
    SopstveniIzvestajLekaraServis(kor_ime,broj_dana)


if __name__ == '__main__':
    SopstveniIzvestajLekaraServis("horacije442", 150)
