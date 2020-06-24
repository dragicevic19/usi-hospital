import re

# PUTANJE ZA UPIS U FAJL
PUTANJA_FAJL_KORISNICI = r'../../data/korisnici.csv'
PUTANJA_FAJL_BOLNICKA_OPREMA = r'../../data/bolnicka_oprema.csv'
PUTANJA_FAJL_UNOS_ANAMNEZE = r'../../data/unos_anamneze.csv'
PUTANJA_FAJL_ANAMNEZA = r'../../data/anamneza.csv'
PUTANJA_FAJL_PROSTORIJE = r'../../data/prostorije.csv'
PUTANJA_FAJL_DOGADJAJI = r'../../data/dogadjaji.csv'
PUTANJA_FAJL_NOTIFIKACIJE = '../../data/notifikacije.csv'
PUTANJA_FAJL_ZAHTEVI_ZA_PREGLED = '../../data/zahtevi_za_pregled.csv'

# IZVESTAJI UPRAVNIK
PUTANJA_ZA_IZVESTAJ_PROSTORIJE = r'../../data/izvestaj_prostorije.pdf'
PUTANJA_ZA_IZVESTAJ_PROSTORIJE_CITANJE = r'....\data\izvestaj_prostorije.pdf'
PUTANJA_ZA_IZVESTAJ_UPRAVNIK_LEKAR = r'../../data/izvestaj_lekar.pdf'
PUTANJA_ZA_IZVESTAJ_LEKARA_CITANJE = r'....\data\izvestaj_lekar.pdf'

# IZVESTAJI LEKAR
PUTANJA_ZA_IZVESTAJ_LEKAR_SOPSTVENI = r'../../data/izvestaj_lekar_zauzece.pdf'
PUTANJA_ZA_IZVESTAJ_LEKAR_SOPSTVENI_CITANJE = r'....\data\izvestaj_lekar_zauzece.pdf'

# DATUMI, VREMENA

REGEX_VREME_OD_DO = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)-(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
REGEX_DATUM = re.compile(r'([0-2][0-9]|(3)[0-1])(/)(((0)[0-9])|((1)[0-2]))(/)\d{4}')
REGEX_VREME = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')


MINUTA_U_DANU = 1440
VREMENSKI_SLOT = 30

# INDEXI
INDEX_PACIJENTA_DOGADJAJ_TREEVIEW = 4
INDEX_LEKARA_TREEVIEW_PRIKAZ_PREGLEDA = 3

# OSTALO
DUZINA_BR_KNJIZICE = 8