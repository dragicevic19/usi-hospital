from model.konstante.konstante import PATH_TO_NOTIFIKACIJE
from repozitorijum.dogadjaj_repozitorijum import DogadjajRepozitorijum

lista_dogadjaja = []
lista_proslih_dogadjaja = []


class NotifikacijeRepozitorijum(DogadjajRepozitorijum):

    @staticmethod
    def ucitaj_dogadjaji():
        super().ucitaj_dogadjaje(PATH_TO_NOTIFIKACIJE, lista_dogadjaja, lista_proslih_dogadjaja)

    @staticmethod
    def sacuvaj_dogadjaji():
        super().sacuvaj_dogadjaj(PATH_TO_NOTIFIKACIJE, lista_dogadjaja, lista_proslih_dogadjaja)

    @staticmethod
    def posalji_notifikaciju(dogadjaj):
        lista_dogadjaja.append(dogadjaj)
        NotifikacijeRepozitorijum.sacuvaj_dogadjaji()

