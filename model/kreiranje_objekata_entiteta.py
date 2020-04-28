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


class KreiranjeObjekataEntiteta:

    @staticmethod
    def ucitavanje_korisnika():
        path = Path('../data/korisnici.csv')
        with path.open('r') as file:
            reader = csv.reader(file)

            for red in reader:
                KreiranjeObjekataEntiteta.__kreiraj_po_ulozi(red)

    @staticmethod
    def __kreiraj_po_ulozi(red):
        uloga = red[INDEX_ULOGE_KORISNIKA]
        if uloga == "upravnik bolnice":
            KreiranjeObjekataEntiteta.__kreiranje_upravnika_bolnice(red)
        elif uloga == "administrator":
            KreiranjeObjekataEntiteta.__kreiranje_administratora(red)
        elif uloga == "sekretar":
            KreiranjeObjekataEntiteta.__kreiranje_sekretara(red)
        elif uloga == "lekar":
            KreiranjeObjekataEntiteta.__kreiranje_lekara(red)
        elif uloga == "pacijent":
            KreiranjeObjekataEntiteta.__kreiranje_pacijenta(red)

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
        lekar = Lekar(red[0], red[1], red[3], red[4], red[5], red[6], red[7])

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
                # lista_ucitane_bolnicke_opreme.append(red)

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


KreiranjeObjekataEntiteta.ucitavanje_korisnika()
KreiranjeObjekataEntiteta.ucitavanje_bolnicke_opreme()
KreiranjeObjekataEntiteta.ucitavanje_unosa_anamneze()
KreiranjeObjekataEntiteta.ucitavanje_anamneze()
KreiranjeObjekataEntiteta.ucitavanje_prostorije()

# NAPOMENA!!!!
# 1) IMPORTUJ LISTU ODGORAJUCEG ENTITETA
# 2) PRISTUPI METODAMA KREIRANOG OBJEKTA
# 3) UZIVAJ!

