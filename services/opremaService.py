from model.kreiranje_objekata_entiteta import lista_ucitane_bolnicke_opreme, KreiranjeObjekata
from model.bolnickaOprema import BolnickaOprema


class OpremaService(object):

    @staticmethod
    def dodaj_postojecu_opremu(oprema, kolicina):
        oprema._ukupan_broj_opreme += int(kolicina)
        oprema._slobodna_oprema += int(kolicina)
        KreiranjeObjekata.sacuvaj_entitete()

    @staticmethod
    def dodaj_opremu_nova(naziv, opis, kolicina):
        oprema = BolnickaOprema(naziv, int(kolicina))
        lista_ucitane_bolnicke_opreme.append(oprema)
        KreiranjeObjekata.sacuvaj_entitete()
