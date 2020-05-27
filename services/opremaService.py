from model.kreiranje_objekata_entiteta import KreiranjeObjekata
from model.bolnickaOprema import BolnickaOprema
from model.kreiranje_objekata_entiteta import lista_ucitanih_prostorija
from repository.oprema.oprema_repository import OpremaRepository, lista_ucitane_bolnicke_opreme


class OpremaService(object):

    @staticmethod
    def dodaj_postojecu_opremu(oprema, kolicina, opis):
        oprema._ukupan_broj_opreme += int(kolicina)
        oprema._slobodna_oprema += int(kolicina)
        oprema._opis += ' ' + opis
        KreiranjeObjekata.sacuvaj_entitete()

    @staticmethod
    def dodaj_opremu_nova(naziv, opis, kolicina):
        oprema = BolnickaOprema(naziv, int(kolicina), int(kolicina), opis)
        lista_ucitane_bolnicke_opreme.append(oprema)
        KreiranjeObjekata.sacuvaj_entitete()

    @staticmethod
    def azuriraj_opremu(selektovan_naziv, naziv, opis, kolicina):
        oprema = OpremaRepository.postoji_oprema(selektovan_naziv)
        oprema._naziv_opreme = naziv
        oprema._opis = opis
        zauzeta_oprema = oprema._ukupan_broj_opreme - oprema._slobodna_oprema
        oprema._slobodna_oprema = kolicina
        oprema._ukupan_broj_opreme = int(zauzeta_oprema) + int(kolicina)
        KreiranjeObjekata.sacuvaj_entitete()

    @staticmethod
    def obrisi_opremu(naziv_opreme):
        oprema = OpremaRepository.postoji_oprema(naziv_opreme)
        oprema._obrisan = True
        lista_ucitane_bolnicke_opreme.remove(oprema)
        KreiranjeObjekata.sacuvaj_entitete()

    @staticmethod
    def obrisi_opremu_iz_prostorija(naziv_opreme):
        for prostorija in lista_ucitanih_prostorija:
            if naziv_opreme in prostorija.get_spisak_opreme():
                prostorija.get_spisak_opreme().pop(naziv_opreme)
                KreiranjeObjekata.sacuvaj_entitete()
