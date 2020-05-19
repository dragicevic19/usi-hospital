import csv
from data.konstante import *
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
lista_obrisanih_korisnika = []
lista_obrisanih_prostorija = []

INDEX_ULOGE_KORISNIKA = 2


class KreiranjeObjekata:

    @staticmethod
    def sacuvaj_entitete():
        KreiranjeObjekata.__sacuvaj_korisnika()
        KreiranjeObjekata.__sacuvaj_anamnezu()
        KreiranjeObjekata.__sacuvaj_bolnicku_opremu()
        KreiranjeObjekata.__sacuvaj_prostorije()
        KreiranjeObjekata.__sacuvaj_unos_anamneze()

    @staticmethod
    def ucitaj_entitete():
        KreiranjeObjekata.ucitavanje_korisnika()
        KreiranjeObjekata.ucitavanje_bolnicke_opreme()
        KreiranjeObjekata.ucitavanje_unosa_anamneze()
        KreiranjeObjekata.ucitavanje_anamneze()
        KreiranjeObjekata.ucitavanje_prostorije()

    @staticmethod
    def ucitavanje_korisnika():
        path = Path(PATH_TO_KORISNICI)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                obrisan = bool(red[5])
                if not obrisan:
                    KreiranjeObjekata.__kreiraj_po_ulozi(red, lista_ucitanih_korisnika)
                else:
                    KreiranjeObjekata.__kreiraj_po_ulozi(red, lista_obrisanih_korisnika)

    @staticmethod
    def __kreiraj_po_ulozi(red, lista):
        uloga = red[INDEX_ULOGE_KORISNIKA]
        if uloga == "upravnik bolnice":
            KreiranjeObjekata.__kreiranje_upravnika_bolnice(red, lista)
        elif uloga == "administrator":
            KreiranjeObjekata.__kreiranje_administratora(red, lista)
        elif uloga == "sekretar":
            KreiranjeObjekata.__kreiranje_sekretara(red, lista)
        elif uloga == "lekar":
            KreiranjeObjekata.__kreiranje_lekara(red, lista)
        elif uloga == "pacijent":
            KreiranjeObjekata.__kreiranje_pacijenta(red, lista)

    @staticmethod
    def __kreiranje_upravnika_bolnice(red, lista):
        upravnik = Upravnik(red[0], red[1], red[3], red[4], red[5])
        lista.append(upravnik)

    @staticmethod
    def __kreiranje_administratora(red, lista):
        administrator = Administrator(red[0], red[1], red[3], red[4], red[5])
        lista.append(administrator)

    @staticmethod
    def __kreiranje_sekretara(red, lista):
        sekretar = Sekretar(red[0], red[1], red[3], red[4], red[5])
        lista.append(sekretar)

    @staticmethod
    def __kreiranje_lekara(red, lista):
        spisak_specijalizacija = red[8].split(';')
        spisak_pacijenata = red[7].split(';')
        lekar = Lekar(red[0], red[1], red[3], red[4], red[6], spisak_pacijenata, spisak_specijalizacija, red[5])
        lista.append(lekar)

    @staticmethod
    def __kreiranje_pacijenta(red, lista):
        pacijent = Pacijent(red[0], red[1], red[3], red[4], red[6], red[7], red[8], red[5])
        lista.append(pacijent)

    ########################################################################
    @staticmethod
    def ucitavanje_bolnicke_opreme():
        path = Path(PATH_TO_BOLNICKA_OPREMA)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                bolnicka_oprema = BolnickaOprema(red[0], int(red[1]), int(red[2]), red[3])
                lista_ucitane_bolnicke_opreme.append(bolnicka_oprema)

    @staticmethod
    def ucitavanje_unosa_anamneze():
        path = Path(PATH_TO_UNOS_ANAMNEZE)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                unos_anamneze = UnosAnamneze(red[0], red[1], red[2], red[3])
                lista_ucitanih_unosa_anamneza.append(unos_anamneze)

    @staticmethod
    def ucitavanje_anamneze():
        path = Path(PATH_TO_ANAMNEZA)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                pojedinacni_unos_anamneze = red[1].split("|")
                anamneza = Anamneza(red[0], pojedinacni_unos_anamneze)
                lista_ucitanih_anamneza.append(anamneza)

    @staticmethod
    def ucitavanje_prostorije():
        path = Path(PATH_TO_PROSTORIJE)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                obrisana = bool(red[4])
                if not obrisana:
                    KreiranjeObjekata.__ucitaj_prostoriju(red, lista_ucitanih_prostorija)
                else:
                    KreiranjeObjekata.__ucitaj_prostoriju(red, lista_obrisanih_prostorija)

    @staticmethod
    def __ucitaj_prostoriju(red, lista):
        pojedinacna_oprema = red[2].split("|")
        lista_oprema = []
        for stavka in pojedinacna_oprema:
            oprema = {}
            naziv, kolicina = stavka.split(";")
            oprema[naziv] = kolicina
            lista_oprema.append(oprema)
        prostorija = Prostorija(red[0], red[1], lista_oprema, red[3], red[4])
        lista.append(prostorija)

    ############################################################################################################
    @staticmethod
    def __sacuvaj_korisnika():
        path = Path(PATH_TO_KORISNICI)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            KreiranjeObjekata.__upisi_korisnike_csv(writer, lista_ucitanih_korisnika)
            KreiranjeObjekata.__upisi_korisnike_csv(writer, lista_obrisanih_korisnika)

    @staticmethod
    def __upisi_korisnike_csv(writer, lista):
        for korisnik in lista:
            uloga = korisnik.get_uloga()
            # if not korisnik.get_obrisan():
            #     obrisan = ''
            # else:
            #     obrisan = True
            KreiranjeObjekata.sacuvaj_po_ulozi(korisnik, uloga, writer)

    @staticmethod
    def sacuvaj_po_ulozi(korisnik, uloga, writer):

        if uloga == 'upravnik bolnice' or uloga == 'administrator' or uloga == 'sekretar':
            writer.writerow([korisnik.get_korisnicko_ime(), korisnik.get_lozinka(), uloga, korisnik.get_ime(),
                             korisnik.get_prezime(), korisnik.get_obrisan()])
        # ako nam bude pravilo problem to sto nemaju svi redovi isto kolona, dodacemo ,,,
        elif uloga == 'lekar':
            KreiranjeObjekata.__sacuvaj_lekara(korisnik, uloga, writer)

        elif uloga == 'pacijent':
            KreiranjeObjekata.__sacuvaj_pacijenta(korisnik, uloga, writer)

    @staticmethod
    def __sacuvaj_lekara(korisnik, uloga, writer):
        spisak_spec = ';'.join(korisnik.get_spisak_specijalizacija())
        spisak_pacijenata = ';'.join(korisnik.get_spisak_pacijenata())
        writer.writerow([korisnik.get_korisnicko_ime(), korisnik.get_lozinka(), uloga,
                         korisnik.get_ime(), korisnik.get_prezime(), korisnik.get_obrisan(), korisnik.get_radno_vreme(),
                         spisak_pacijenata, spisak_spec])

    @staticmethod
    def __sacuvaj_pacijenta(korisnik, uloga, writer):
        writer.writerow([korisnik.get_korisnicko_ime(), korisnik.get_lozinka(), uloga,
                         korisnik.get_ime(), korisnik.get_prezime(), korisnik.get_obrisan(),
                         korisnik.get_br_zdravstvene(), korisnik.get_pol(), korisnik.get_anamneza()])

    ####################################################################################################

    @staticmethod
    def __sacuvaj_anamnezu():
        path = Path(PATH_TO_ANAMNEZA)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for anamneza in lista_ucitanih_anamneza:
                unosi_anamneza = '|'.join(anamneza.get_spisak_pojedinacnih_unosa())  # spisak u string
                writer.writerow([anamneza.get_pacijent(), unosi_anamneza])

    @staticmethod
    def __sacuvaj_bolnicku_opremu():
        path = Path(PATH_TO_BOLNICKA_OPREMA)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for oprema in lista_ucitane_bolnicke_opreme:
                writer.writerow([oprema.get_naziv_opreme(), oprema.get_ukupan_broj_opreme(),
                                 oprema.get_slobodna_oprema(), oprema.get_opis()])

    @staticmethod
    def __sacuvaj_prostorije():
        path = Path(PATH_TO_PROSTORIJE)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            KreiranjeObjekata.__upisi_prostorije_csv(writer, lista_ucitanih_prostorija)
            KreiranjeObjekata.__upisi_prostorije_csv(writer, lista_obrisanih_prostorija)

    @staticmethod
    def __upisi_prostorije_csv(writer, lista_prostorija):

        lista_opreme = []
        for prostorija in lista_prostorija:
            for oprema in prostorija.get_spisak_opreme():
                for k, v in oprema.items():
                    lista_opreme.append(k + ";" + v)

            spisak_opreme = '|'.join(lista_opreme)
            lista_opreme.clear()
            writer.writerow([prostorija.get_sprat(), prostorija.get_broj_prostorije(), spisak_opreme,
                             prostorija.get_namena_prostorije(), prostorija.get_obrisana()])

    @staticmethod
    def __sacuvaj_unos_anamneze():
        path = Path(PATH_TO_UNOS_ANAMNEZE)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')

            for unos in lista_ucitanih_unosa_anamneza:
                writer.writerow([unos.get_id(), unos.get_lekar(), unos.get_opis(), unos.get_datum_i_vreme()])

    ################################################################################################################

    @staticmethod
    def postoji_prostorija(sprat, broj_sobe):
        for prostorija in lista_ucitanih_prostorija:
            if prostorija.get_sprat() == sprat and prostorija.get_broj_prostorije() == broj_sobe:
                return prostorija
        return False

    @staticmethod
    def postoji_korisnik(korisniko_ime):
        for korisnik in lista_ucitanih_korisnika:
            if korisnik.get_korisnicko_ime() == korisniko_ime:
                return korisnik
        return False

    @staticmethod
    def postoji_oprema(naziv_opreme):
        for oprema in lista_ucitane_bolnicke_opreme:
            if oprema.get_naziv_opreme() == naziv_opreme:
                return oprema
        return False


# zbog testiranja se ovde poziva, posle treba obrisati jer se poziva u login.py
KreiranjeObjekata.ucitaj_entitete()
