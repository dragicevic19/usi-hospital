from tkinter import *
from gui.upravnik.renoviranje.uklanjanje_opreme_iz_prostorije import PremestanjeOpreme
from model.DTO.broj_i_naziv_opremeDTO import BrojINazivOpremeDTO
from model.enum.renoviranje import TipPremestanjaOpreme
from repository.oprema.oprema_repozitorijum import lista_ucitane_bolnicke_opreme
from repository.prostorije.prostorije_repozitorijum import lista_ucitanih_prostorija


class DodavanjeOpremeUProstoriju(PremestanjeOpreme):

    def __init__(self, root, selektovana_prostorija):
        root.title('Dodavanje opreme u prostoriju')
        self._prostorija = selektovana_prostorija
        self._oprema_za_dodavanje = []
        self.pronadji_opremu_za_dodavanje()
        super().__init__(root, self._prostorija, self._oprema_za_dodavanje,
                         TipPremestanjaOpreme.DODAVANJE_OPREME)

    def pronadji_opremu_za_dodavanje(self):
        for oprema in lista_ucitane_bolnicke_opreme:
            if int(oprema.get_slobodna_oprema()) > 0:
                slobodna_opremaDTO = BrojINazivOpremeDTO(oprema.get_naziv_opreme(), int(oprema.get_slobodna_oprema()))
                self._oprema_za_dodavanje.append(slobodna_opremaDTO)


def dodavanje_opreme(selektovana_prostorija):
    root = Tk()
    root.geometry('800x450')

    application = DodavanjeOpremeUProstoriju(root, selektovana_prostorija)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x450')
    # OpremaRepository.ucitavanje_bolnicke_opreme()
    # ProstorijeRepository.ucitavanje_prostorije()
    prostorija = lista_ucitanih_prostorija[0]
    application = DodavanjeOpremeUProstoriju(root, prostorija)
    root.mainloop()
