import csv
from model.lekar import Lekar
from model.pacijent import Pacijent
from model.upravnik import Upravnik
from model.administrator import Administrator
from model.sekretar import Sekretar
from model.bolnickaOprema import BolnickaOprema


lista_korisnika = []
lista_upravnika_bolnice = []
lista_administratora = []
lista_sekretara = []
lista_lekara = []
lista_pacijenata = []
lista_opreme = []
lista_bolnicke_opreme = []

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

            for i in reader:
                lista_korisnika.append(i)

    @staticmethod
    def kreiranje_upravnika_bolnice():

        KreiranjeObjekataEntiteta.ucitavanje_korisnika()
        for korisnik in lista_korisnika:

            if korisnik[INDEX_ULOGE_UPRAVNIKA] == "upravnik bolnice":

                upravnik = Upravnik(korisnik[0], korisnik[1], korisnik[2], korisnik[3])
                lista_upravnika_bolnice.append(upravnik)

    @staticmethod
    def kreiranje_administratora():

        KreiranjeObjekataEntiteta.ucitavanje_korisnika()
        for korisnik in lista_korisnika:

            if korisnik[INDEX_ULOGE_ADMINISTRATORA] == "administrator":
                administrator = Administrator(korisnik[0], korisnik[1], korisnik[2], korisnik[3])
                lista_administratora.append(administrator)

    @staticmethod
    def kreiranje_sekretara():

        KreiranjeObjekataEntiteta.ucitavanje_korisnika()
        for korisnik in lista_korisnika:

            if korisnik[INDEX_ULOGE_SEKRETARA] == "sekretar":
                sekretar = Sekretar(korisnik[0], korisnik[1], korisnik[2], korisnik[3])
                lista_sekretara.append(sekretar)

    @staticmethod
    def kreiranje_lekara():

        KreiranjeObjekataEntiteta.ucitavanje_korisnika()
        for korisnik in lista_korisnika:

            if len(korisnik) > INDEX_ULOGE_LEKARA:

                if korisnik[INDEX_ULOGE_LEKARA] == "lekar":
                    lekar = Lekar(korisnik[0], korisnik[1], korisnik[2], korisnik[3], korisnik[4], korisnik[5],
                    korisnik[6])
                    lista_lekara.append(lekar)

    @staticmethod
    def kreiranje_pacijenta():

        KreiranjeObjekataEntiteta.ucitavanje_korisnika()
        for korisnik in lista_korisnika:

            if len(korisnik) > INDEX_ULOGE_PACIJENTA:

                if korisnik[INDEX_ULOGE_PACIJENTA] == "pacijent":
                    pacijent = Pacijent(korisnik[0], korisnik[1], korisnik[2], korisnik[3], korisnik[4], korisnik[5],
                    korisnik[6])
                    lista_pacijenata.append(pacijent)

    @staticmethod
    def ucitavanje_bolnicke_opreme():

        with open("bolnicka_oprema.csv", newline='') as file:
            reader = csv.reader(file)

            for i in reader:
                lista_opreme.append(i)

    @staticmethod
    def kreiranje_bolnicke_opreme():

        KreiranjeObjekataEntiteta.ucitavanje_bolnicke_opreme()
        for oprema in lista_opreme:
            bolnicka_oprema = BolnickaOprema(oprema[0], oprema[1], oprema[2])
            lista_bolnicke_opreme.append(bolnicka_oprema)



KreiranjeObjekataEntiteta.kreiranje_upravnika_bolnice()
KreiranjeObjekataEntiteta.kreiranje_administratora()
KreiranjeObjekataEntiteta.kreiranje_lekara()
KreiranjeObjekataEntiteta.kreiranje_pacijenta()
KreiranjeObjekataEntiteta.kreiranje_sekretara()
KreiranjeObjekataEntiteta.kreiranje_bolnicke_opreme()


# NAPOMENA!!!!
#1) IMPORTUJ LISTU ODGORAJUCEG ENTITETA
#2) PRISTUPI METODAMA KREIRANOG OBJEKTA
#3) UZIVAJ!












