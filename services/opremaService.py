from model.kreiranje_objekata_entiteta import lista_ucitane_bolnicke_opreme, KreiranjeObjekata
from model.bolnickaOprema import BolnickaOprema

class OpremaService(object):

    @staticmethod
    def dodaj_opremu_postoji(kolicina):
        oprema = BolnickaOprema(kolicina)
        lista_ucitane_bolnicke_opreme.append(oprema)
        KreiranjeObjekata.sacuvaj_entitete()

