import re

PATH_TO_KORISNICI = '../../data/korisnici.csv'
PATH_TO_BOLNICKA_OPREMA = '../../data/bolnicka_oprema.csv'
PATH_TO_UNOS_ANAMNEZE = '../../data/unos_anamneze.csv'
PATH_TO_ANAMNEZA = '../../data/anamneza.csv'
PATH_TO_PROSTORIJE = '../../data/prostorije.csv'
PATH_TO_DOGADJAJI = '../../data/dogadjaji.csv'

REGEX_VREME = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)-(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
LEN_BR_KNJIZICE = 8
INDEX_PACIJENTA_DOGADJAJ_TREEVIEW = 4

MINUTA_U_DANU = 1440
VREMENSKI_SLOT = 30
