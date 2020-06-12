from tkinter import *
from gui.upravnik.renoviranje.premestanje_opreme import PremestanjeOpreme
from model.DTO.broj_i_naziv_opreme_DTO import BrojINazivOpremeDTO
from model.enum.renoviranje import TipPremestanjaOpreme
from repozitorijum.prostorije.prostorije_repozitorijum import lista_ucitanih_prostorija


class UklanjenjeOpremeIzProstorije(PremestanjeOpreme):

    def __init__(self, root, selektovana_prostorija):
        root.title('Uklanjanje opreme iz prostorije')
        self._prostorija = selektovana_prostorija
        self._oprema_za_izbacivanje = []
        self.pronadji_opremu_za_izbacivanje()
        super().__init__(root, self._prostorija, self._oprema_za_izbacivanje,
                         TipPremestanjaOpreme.IZBACIVANJE_OPREME)

    def pronadji_opremu_za_izbacivanje(self):
        for naziv, broj_opreme in self._prostorija.get_spisak_opreme().items():
            opremaDTO = BrojINazivOpremeDTO(naziv, int(broj_opreme))
            self._oprema_za_izbacivanje.append(opremaDTO)


def uklanjanje_opreme_iz_prostorije(selektovana_prostorija):
    root = Tk()
    root.geometry('800x450')
    application = UklanjenjeOpremeIzProstorije(root, selektovana_prostorija)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x500')
    prostorija = lista_ucitanih_prostorija[0]
    application = UklanjenjeOpremeIzProstorije(root, prostorija)
    root.mainloop()
