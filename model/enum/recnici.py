from model.administrator import Administrator
from model.enum.tip_notifikacije import TipNotifikacije
from model.lekar import Lekar
from model.pacijent import Pacijent
from model.sekretar import Sekretar
from model.upravnik import Upravnik

konstruktor_po_ulozi = {'UPRAVNIK': Upravnik, 'ADMINISTRATOR': Administrator, 'SEKRETAR': Sekretar, 'LEKAR': Lekar,
                        'PACIJENT': Pacijent}

