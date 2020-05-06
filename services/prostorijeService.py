from model.kreiranje_objekata_entiteta import lista_ucitanih_prostorija, KreiranjeObjekata


class ProstorijeService(object):

    @staticmethod
    def dodavanje_prostorije(prostorija):
        lista_ucitanih_prostorija.append(prostorija)
        KreiranjeObjekata.sacuvaj_entitete()

    @staticmethod
    def brisanje_prostorije(prostorija):
        prostorija._obrisana = True
        KreiranjeObjekata.sacuvaj_entitete()

    @staticmethod
    def pretraga_prostorije():
        pass
