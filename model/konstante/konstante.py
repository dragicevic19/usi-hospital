import re

PATH_TO_KORISNICI = '../../data/korisnici.csv'
PATH_TO_BOLNICKA_OPREMA = '../../data/bolnicka_oprema.csv'
PATH_TO_UNOS_ANAMNEZE = '../../data/unos_anamneze.csv'
PATH_TO_ANAMNEZA = '../../data/anamneza.csv'
PATH_TO_PROSTORIJE = '../../data/prostorije.csv'
PATH_TO_DOGADJAJI = '../../data/dogadjaji.csv'
PATH_TO_IZVESTAJ_PROSTORIJE = "../../data/izvestaj_prostorije.pdf"
PATH_TO_IZVESTAJ_PROSTORIJE_CITANJE_WEB = r'..\..\data\izvestaj_prostorije.pdf'
PATH_TO_IZVESTAJ_LEKARA = "../../data/izvestaj_lekar.pdf"
PATH_TO_IZVESTAJ_LEKARA_CITANJE_WEB = r'..\..\data\izvestaj_lekar.pdf'
PATH_TO_NOTIFIKACIJE = '../../data/notifikacije.csv'

REGEX_VREME = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
REGEX_VREME_OD_DO = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)-(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
REGEX_DATUM = re.compile(r'([0-2][0-9]|(3)[0-1])(/)(((0)[0-9])|((1)[0-2]))(/)\d{4}')
LEN_BR_KNJIZICE = 8
INDEX_PACIJENTA_DOGADJAJ_TREEVIEW = 4

MINUTA_U_DANU = 1440
VREMENSKI_SLOT = 30
INDEX_LEKARA_TREEVIEW_PRIKAZ_PREGLEDA = 3
