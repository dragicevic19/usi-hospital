from repository.izvestaji.izvestaji_repozitorijum import IzvestajRepozitorijum
from repository.kalendar.kalendar_repozitorijum import lista_dogadjaja, lista_proslih_dogadjaja
from datetime import datetime

from repository.korisnik.korisnik_repozitorijum import KorisnikRepository
from services.izvestaji.izvestaji import IzvestajServis


class IzvestajLekaraServis(IzvestajServis):
    def __init__(self, pocetni_datum, krajnji_datum):

        super().__init__("lekare", pocetni_datum, krajnji_datum)

    def pocni(self):
        self._string_za_pdf = self.generisanje(self._tip_izvestaja)

        self._string_za_pdf += self.ukupan_broj_sati_po_lekaru()
        self._string_za_pdf += self.prosecan_broj_sati_po_lekaru()
        self._string_za_pdf += self.prosecno_i_ukupno_sati_svi_lekari()

        IzvestajRepozitorijum.generisi_izvestaj(self._string_za_pdf, False)


    def ukupan_broj_sati_po_lekaru(self):
        ispis = ""
        for lekar in self._mapa:
            pronadjeni_lekar = KorisnikRepository.nadji_po_korisnickom_imenu(lekar)
            # ime, prezime = pronadjeni_lekar.get_ime(), pronadjeni_lekar.get_prezime()
            ime, prezime = "Pera", "Peric"
            ispis += "Ukupno zauzece lekara " + lekar + "pod imenom " + ime + " " + prezime + " je: " + str(
                int(self._mapa[lekar]) * 30) \
                     + " minuta \n "
        return ispis



    def prosecan_broj_sati_po_lekaru(self):
        ispis = ""
        for lekar in self._mapa:
            ispis += "Prosecno zauzece lekara " + lekar + " po danu je: " \
                     + str(
                int(self._mapa[lekar]) * 30 / self._broj_dana_za_izvestaj) \
                     + " minuta \n "
        return ispis


    def prosecno_i_ukupno_sati_svi_lekari(self):
        return ("Ukupan broj sati svih lekara je: "
                + str(self._ukupan_broj_sati_zauzeca_svih) + " sati, a prosecan broj sati zauzeca je: " +
                str(self._ukupan_broj_sati_zauzeca_svih / self._broj_dana_za_izvestaj) +
                " sati po danu.")

