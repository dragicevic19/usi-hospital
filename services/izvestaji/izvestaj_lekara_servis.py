from repository.izvestaji.izvestaji_repozitorijum import IzvestajRepozitorijum
from repository.kalendar.kalendar_repozitorijum import lista_dogadjaja, lista_proslih_dogadjaja
from datetime import datetime

from repository.korisnik.korisnik_repozitorijum import KorisnikRepository


class IzvestajLekaraServis:
    lista_dogadjaja_spojeno = lista_proslih_dogadjaja + lista_dogadjaja
    mapa_lekara = {}
    broj_dana_za_izvestaj = 0
    ukupan_broj_sati_zauzeca_svih = 0

    @staticmethod
    def generisanje(prvi_datum, drugi_datum):
        dan, mes, god = prvi_datum.split("/")
        d, m, g = drugi_datum.split("/")
        datum_od = datetime(int(god), int(mes), int(dan))
        datum_do = datetime(int(g), int(m), int(d))

        string_za_pdf = "IZVESTAJ ZA SVE LEKARE OD " + prvi_datum + " DO " + drugi_datum + "\n\n"

        IzvestajLekaraServis.broj_dana_za_izvestaj = (datum_do - datum_od).days
        IzvestajLekaraServis.ukupno_termina_po_lekaru(datum_od, datum_do)
        string_za_pdf += IzvestajLekaraServis.ukupan_broj_sati_po_lekaru()
        string_za_pdf += IzvestajLekaraServis.prosecan_broj_sati_po_lekaru()
        string_za_pdf += IzvestajLekaraServis.prosecno_i_ukupno_sati_svi_lekari()

        IzvestajRepozitorijum.generisi_izvestaj(string_za_pdf, False)

    @staticmethod
    def ukupno_termina_po_lekaru(datum_od, datum_do):
        for dogadjaj in IzvestajLekaraServis.lista_dogadjaja_spojeno:
            if datum_od <= dogadjaj.datum_vreme <= datum_do:
                for lekar in dogadjaj.spisak_doktora:
                    if lekar in IzvestajLekaraServis.mapa_lekara:
                        IzvestajLekaraServis.mapa_lekara[lekar] += dogadjaj.broj_termina
                    else:
                        IzvestajLekaraServis.mapa_lekara[lekar] = dogadjaj.broj_termina
                    IzvestajLekaraServis.ukupan_broj_sati_zauzeca_svih += dogadjaj.broj_termina
        IzvestajLekaraServis.ukupan_broj_sati_zauzeca_svih /= 2

    @staticmethod
    def ukupan_broj_sati_po_lekaru():
        ispis = ""
        for lekar in IzvestajLekaraServis.mapa_lekara:
            pronadjeni_lekar = KorisnikRepository.nadji_po_korisnickom_imenu(lekar)
            # ime, prezime = pronadjeni_lekar.get_ime(), pronadjeni_lekar.get_prezime()
            ime, prezime = "Pera", "Peric"
            ispis += "Ukupno zauzece lekara " + lekar + "pod imenom " + ime + " " + prezime + " je: " + str(
                int(IzvestajLekaraServis.mapa_lekara[lekar]) * 30) \
                     + " minuta \n "
        return ispis


    @staticmethod
    def prosecan_broj_sati_po_lekaru():
        ispis = ""
        for lekar in IzvestajLekaraServis.mapa_lekara:
            ispis += "Prosecno zauzece lekara " + lekar + " po danu je: " \
                     + str(
                int(IzvestajLekaraServis.mapa_lekara[lekar]) * 30 / IzvestajLekaraServis.broj_dana_za_izvestaj) \
                     + " minuta \n "
        return ispis

    @staticmethod
    def prosecno_i_ukupno_sati_svi_lekari():
        return ("Ukupan broj sati svih lekara je: "
                + str(IzvestajLekaraServis.ukupan_broj_sati_zauzeca_svih) + " sati, a prosecan broj sati zauzeca je: " +
                str(IzvestajLekaraServis.ukupan_broj_sati_zauzeca_svih / IzvestajLekaraServis.broj_dana_za_izvestaj) +
                " sati po danu.")

