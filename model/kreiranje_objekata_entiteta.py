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

lista_ucitanih_korisnika = []
zavrsna_lista_korisnika = []
lista_ucitane_bolnicke_opreme = []
zavrsna_lista_bolnicke_opreme = []
lista_ucitanih_unosa_anamneza = []
zavrsna_lista_unosa_anamneza = []
lista_ucitanih_anamneza = []
zavrsna_lista_anamneza = []
lista_ucitanih_prostorija = []
zavrsna_lista_prostorija = []

INDEX_ULOGE_SEKRETARA = 4
INDEX_ULOGE_ADMINISTRATORA = 4
INDEX_ULOGE_UPRAVNIKA = 4
INDEX_ULOGE_LEKARA = 7
INDEX_ULOGE_PACIJENTA = 7


class KreiranjeObjekataEntiteta:

    @staticmethod
    def ucitavanje_korisnika():

        with open("korisnici.csv", newline='') as file:
            reader = csv.reader(file)

            for red in reader:
                lista_ucitanih_korisnika.append(red)
                # KreiranjeObjekataEntiteta.ova_bira_korisnika(red[INDEX_ULOGE_KORISNIKA])

    # @staticmethod
    # def ova_bira_korisnika(self, uloga):
    #     if uloga == "upravnik bolnice":
    #         KreiranjeObjekataEntiteta.kreiranje_upravnika_bolnice()
    #     elif uloga == "administrator":
    #

    @staticmethod
    def kreiranje_upravnika_bolnice():

        for korisnik in lista_ucitanih_korisnika:

            if korisnik[INDEX_ULOGE_UPRAVNIKA] == "upravnik bolnice":

                upravnik = Upravnik(korisnik[0], korisnik[1], korisnik[2], korisnik[3])
                zavrsna_lista_korisnika.append(upravnik)

    @staticmethod
    def kreiranje_administratora():

        for korisnik in lista_ucitanih_korisnika:

            if korisnik[INDEX_ULOGE_ADMINISTRATORA] == "administrator":
                administrator = Administrator(korisnik[0], korisnik[1], korisnik[2], korisnik[3])
                zavrsna_lista_korisnika.append(administrator)

    @staticmethod
    def kreiranje_sekretara():

        for korisnik in lista_ucitanih_korisnika:

            if korisnik[INDEX_ULOGE_SEKRETARA] == "sekretar":
                sekretar = Sekretar(korisnik[0], korisnik[1], korisnik[2], korisnik[3])
                zavrsna_lista_korisnika.append(sekretar)

    @staticmethod
    def kreiranje_lekara():

        for korisnik in lista_ucitanih_korisnika:

            if len(korisnik) > INDEX_ULOGE_LEKARA and korisnik[INDEX_ULOGE_LEKARA] == "lekar":
                lekar = Lekar(korisnik[0], korisnik[1], korisnik[2], korisnik[3], korisnik[4], korisnik[5],
                                korisnik[6])
                zavrsna_lista_korisnika.append(lekar)

    @staticmethod
    def kreiranje_pacijenta():

        for korisnik in lista_ucitanih_korisnika:

            if len(korisnik) > INDEX_ULOGE_PACIJENTA and korisnik[INDEX_ULOGE_PACIJENTA] == "pacijent":
                pacijent = Pacijent(korisnik[0], korisnik[1], korisnik[2], korisnik[3], korisnik[4], korisnik[5],
                                    korisnik[6])
                zavrsna_lista_korisnika.append(pacijent)

    @staticmethod
    def ucitavanje_bolnicke_opreme():

        with open("bolnicka_oprema.csv", newline='') as file:
            reader = csv.reader(file)

            for red in reader:
                lista_ucitane_bolnicke_opreme.append(red)

    @staticmethod
    def kreiranje_bolnicke_opreme():

        KreiranjeObjekataEntiteta.ucitavanje_bolnicke_opreme()
        for oprema in lista_ucitane_bolnicke_opreme:
            bolnicka_oprema = BolnickaOprema(oprema[0], oprema[1], oprema[2])
            zavrsna_lista_bolnicke_opreme.append(bolnicka_oprema)


    @staticmethod
    def ucitavanje_unosa_anamneze():

        with open("unos_anamneze.csv", newline='') as file:
            reader = csv.reader(file)

            for red in reader:
                lista_ucitanih_unosa_anamneza.append(red)

    @staticmethod
    def kreiranje_unosa_anamneze():

        KreiranjeObjekataEntiteta.ucitavanje_unosa_anamneze()
        for unos in lista_ucitanih_unosa_anamneza:
            unos_anamneze = UnosAnamneze(unos[0], unos[1], unos[2])
            zavrsna_lista_unosa_anamneza.append(unos_anamneze)


    @staticmethod
    def ucitavanje_anamneze():

        with open("anamneza.csv", newline='') as file:
            reader = csv.reader(file)

            for red in reader:
                lista_ucitanih_anamneza.append(red)


    @staticmethod
    def kreiranje_anamneze():

        KreiranjeObjekataEntiteta.ucitavanje_anamneze()
        for anam in lista_ucitanih_anamneza:
            pojedinacni_unos_anamneze = anam[1].split("|")
            anamneza = Anamneza(anam[0], pojedinacni_unos_anamneze)
            zavrsna_lista_anamneza.append(anamneza)


    @staticmethod
    def ucitavanje_prostorije():

        with open("prostorije.csv", newline='') as file:
            reader = csv.reader(file)

            for red in reader:
                lista_ucitanih_prostorija.append(red)


    @staticmethod
    def kreiranje_prostorije():

        KreiranjeObjekataEntiteta.ucitavanje_prostorije()
        for prost in lista_ucitanih_prostorija:
            pojedinacna_oprema = prost[2].split("|")
            prostorija = Prostorija(prost[0], prost[1], pojedinacna_oprema, prost[3])
            zavrsna_lista_prostorija.append(prostorija)

    @staticmethod
    def postoji_prostorija(sprat, broj_sobe):
        for prostorija in zavrsna_lista_prostorija:
            if prostorija.get_sprat() == sprat and prostorija.get_broj_prostorije() == broj_sobe:
                return True
        return False

    @staticmethod
    def postoji_korisnik(korisniko_ime):
        for korisnik in zavrsna_lista_korisnika:
            if korisnik.get_korisnicko_ime() == korisniko_ime:
                return True
        return False

    @staticmethod
    def postoji_oprema(naziv_opreme):
        for oprema in zavrsna_lista_bolnicke_opreme:
            if oprema.get_naziv_opreme == naziv_opreme:
                return True
        return False


KreiranjeObjekataEntiteta.ucitavanje_korisnika()
KreiranjeObjekataEntiteta.kreiranje_upravnika_bolnice()
KreiranjeObjekataEntiteta.kreiranje_administratora()
KreiranjeObjekataEntiteta.kreiranje_lekara()
KreiranjeObjekataEntiteta.kreiranje_pacijenta()
KreiranjeObjekataEntiteta.kreiranje_sekretara()
KreiranjeObjekataEntiteta.kreiranje_bolnicke_opreme()
KreiranjeObjekataEntiteta.kreiranje_unosa_anamneze()
KreiranjeObjekataEntiteta.kreiranje_anamneze()
KreiranjeObjekataEntiteta.kreiranje_prostorije()


# NAPOMENA!!!!
#1) IMPORTUJ LISTU ODGORAJUCEG ENTITETA
#2) PRISTUPI METODAMA KREIRANOG OBJEKTA
#3) UZIVAJ!











