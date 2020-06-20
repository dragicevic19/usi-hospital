from model.administrator import Administrator
from model.enum.renoviranje import TipPremestanjaOpreme
from model.lekar import Lekar
from model.pacijent import Pacijent
from model.sekretar import Sekretar
from model.upravnik import Upravnik
from servisi.prostorije.prostorije_servis import ProstorijeServis

konstruktor_po_ulozi = {'UPRAVNIK': Upravnik, 'ADMINISTRATOR': Administrator, 'SEKRETAR': Sekretar, 'LEKAR': Lekar,
                        'PACIJENT': Pacijent}

