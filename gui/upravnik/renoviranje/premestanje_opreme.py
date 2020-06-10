from tkinter import *
from tkinter import ttk

from gui.upravnik.renoviranje.dodavenje_opreme_u_prostoriju import dodavanje_opreme
from gui.upravnik.renoviranje.uklanjanje_opreme_iz_prostorije import uklanjanje_opreme_iz_prostorije
from repository.prostorije.prostorije_repozitorijum import lista_ucitanih_prostorija, ProstorijeRepository


class PremestanjeOpremeMeni:

    def __init__(self, root, selektovana_prostorija):
        self._root = root
        self._root.title("MENI")

        self.dodavanje = ttk.Button(self._root, text='Dodavanje slobodne opreme u prostoriju',
                                    command=lambda: dodavanje_opreme(selektovana_prostorija))
        self.dodavanje.grid(row=0, column=0, pady=10, padx=15)

        self.uklanjanje = ttk.Button(self._root, text='Uklanjanje opreme iz prostorije',
                                     command=lambda: uklanjanje_opreme_iz_prostorije(selektovana_prostorija))
        self.uklanjanje.grid(row=1, column=0, pady=5)


def premestanje_opreme_meni(selektovana_prostorija):
    root = Tk()
    root.geometry('300x100')
    application = PremestanjeOpremeMeni(root, selektovana_prostorija)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('300x100')
    ProstorijeRepository.ucitavanje_prostorije()
    prostorija = lista_ucitanih_prostorija[0]
    application = PremestanjeOpremeMeni(root, prostorija)
    root.mainloop()
