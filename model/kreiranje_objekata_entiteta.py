import csv
from model.lekar import Lekar
from model.pacijent import Pacijent
from model.upravnik import Upravnik
from model.administrator import Administrator
from model.sekretar import Sekretar
from model.bolnickaOprema import BolnickaOprema
from model.unosAnamneze import UnosAnamneze
from model.anamneza import Anamneza
from model.prostorija import Prostorija
from pathlib import Path

lista_ucitanih_korisnika = []
lista_ucitane_bolnicke_opreme = []
lista_ucitanih_unosa_anamneza = []
lista_ucitanih_anamneza = []
lista_ucitanih_prostorija = []

INDEX_ULOGE_KORISNIKA = 2


class KreiranjeObjekata:

    @staticmethod
    def ucitavanje_korisnika():
        path = Path('../data/korisnici.csv')
        with path.open('r') as file:
            reader = csv.reader(file)

            for red in reader:
                KreiranjeObjekata.__kreiraj_po_ulozi(red)

    @staticmethod
    def __kreiraj_po_ulozi(red):
        uloga = red[INDEX_ULOGE_KORISNIKA]
        if uloga == "upravnik bolnice":
            KreiranjeObjekata.__kreiranje_upravnika_bolnice(red)
        elif uloga == "administrator":
            KreiranjeObjekata.__kreiranje_administratora(red)
        elif uloga == "sekretar":
            KreiranjeObjekata.__kreiranje_sekretara(red)
        elif uloga == "lekar":
            KreiranjeObjekata.__kreiranje_lekara(red)
        elif uloga == "pacijent":
            KreiranjeObjekata.__kreiranje_pacijenta(red)

    @staticmethod
    def __kreiranje_upravnika_bolnice(red):
        upravnik = Upravnik(red[0], red[1], red[3], red[4])
        lista_ucitanih_korisnika.append(upravnik)

    @staticmethod
    def __kreiranje_administratora(red):
        administrator = Administrator(red[0], red[1], red[3], red[4])
        lista_ucitanih_korisnika.append(administrator)

    @staticmethod
    def __kreiranje_sekretara(red):
        sekretar = Sekretar(red[0], red[1], red[3], red[4])
        lista_ucitanih_korisnika.append(sekretar)

    @staticmethod
    def __kreiranje_lekara(red):
        spisak_specijalizacija = red[7].split(';')
        lekar = Lekar(red[0], red[1], red[3], red[4], red[5], red[6], spisak_specijalizacija)

        lista_ucitanih_korisnika.append(lekar)

    @staticmethod
    def __kreiranje_pacijenta(red):
        pacijent = Pacijent(red[0], red[1], red[3], red[4], red[5], red[6], red[7])

        lista_ucitanih_korisnika.append(pacijent)

    ########################################################################
    @staticmethod
    def ucitavanje_bolnicke_opreme():

        path = Path('../data/bolnicka_oprema.csv')
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                bolnicka_oprema = BolnickaOprema(red[0], red[1], red[2])
                lista_ucitane_bolnicke_opreme.append(bolnicka_oprema)

    @staticmethod
    def ucitavanje_unosa_anamneze():

        path = Path('../data/unos_anamneze.csv')
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                unos_anamneze = UnosAnamneze(red[0], red[1], red[2], red[3])
                lista_ucitanih_unosa_anamneza.append(unos_anamneze)

    @staticmethod
    def ucitavanje_anamneze():

        path = Path('../data/anamneza.csv')
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                pojedinacni_unos_anamneze = red[1].split("|")
                anamneza = Anamneza(red[0], pojedinacni_unos_anamneze)
                lista_ucitanih_anamneza.append(anamneza)

    @staticmethod
    def ucitavanje_prostorije():
        path = Path('../data/prostorije.csv')
        with path.open('r') as file:
            reader = csv.reader(file)

            for red in reader:
                pojedinacna_oprema = red[2].split("|")
                prostorija = Prostorija(red[0], red[1], pojedinacna_oprema, red[3])
                lista_ucitanih_prostorija.append(prostorija)

    @staticmethod
    def sacuvaj_korisnika():
        path = Path('../data/korisniciProba.csv')
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for korisnik in lista_ucitanih_korisnika:
                uloga = korisnik.get_uloga()
                if uloga == 'upravnik bolnice' or uloga == 'administrator' or uloga == 'sekretar':
                    writer.writerow([korisnik.get_korisnicko_ime(), korisnik.get_lozinka(), uloga,
                                     korisnik.get_ime(), korisnik.get_prezime()])
                elif uloga == 'lekar':  #u spisak_specijalizacija nam bukvalno stoji neurohirurg;kardiohirurg???
                    spisak_spec = KreiranjeObjekata.__spisak_u_string(korisnik.get_spisak_specijalizacija)
                    spisak_pacijenata = KreiranjeObjekata.__spisak_u_string(korisnik.get_spisak_specijalizacija)

                    writer.writerow([korisnik.get_korisnicko_ime(), korisnik.get_lozinka(), uloga,
                                     korisnik.get_ime(), korisnik.get_prezime(), korisnik.get_radno_vreme(),
                                     spisak_pacijenata, spisak_spec])
                # elif uloga == 'pacijent':
                #
                #     writer.writerow([korisnik.get_korisnicko_ime(), korisnik.get_lozinka(), uloga,
                #                      korisnik.get_ime(), korisnik.get_prezime(), korisnik.get_br_zdravstvene(),
                #                      korisnik.get_pol(), korisnik.get_anamneza()])

    @staticmethod
    def __spisak_u_string(spisak):
        rec = ''
        for polje in spisak:
            rec += polje
            rec += ';'
        rec = rec[:-1]
        return rec

    @staticmethod
    def postoji_prostorija(sprat, broj_sobe):
        for prostorija in lista_ucitanih_prostorija:
            if prostorija.get_sprat() == sprat and prostorija.get_broj_prostorije() == broj_sobe:
                return True
        return False

    @staticmethod
    def postoji_korisnik(korisniko_ime):
        for korisnik in lista_ucitanih_korisnika:
            if korisnik.get_korisnicko_ime() == korisniko_ime:
                return True
        return False

    @staticmethod
    def postoji_oprema(naziv_opreme):
        for oprema in lista_ucitane_bolnicke_opreme:
            if oprema.get_naziv_opreme == naziv_opreme:
                return True
        return False


KreiranjeObjekata.ucitavanje_korisnika()
KreiranjeObjekata.ucitavanje_bolnicke_opreme()
KreiranjeObjekata.ucitavanje_unosa_anamneze()
KreiranjeObjekata.ucitavanje_anamneze()
KreiranjeObjekata.ucitavanje_prostorije()
KreiranjeObjekata.sacuvaj_korisnika()


# NAPOMENA!!!!
# 1) IMPORTUJ LISTU ODGORAJUCEG ENTITETA
# 2) PRISTUPI METODAMA KREIRANOG OBJEKTA
# 3) UZIVAJ!
