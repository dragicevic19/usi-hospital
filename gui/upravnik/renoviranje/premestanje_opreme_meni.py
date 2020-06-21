from gui.upravnik.renoviranje.dodavenje_opreme_u_prostoriju import dodavanje_opreme
from gui.upravnik.renoviranje.uklanjanje_opreme_iz_prostorije import uklanjanje_opreme_iz_prostorije
from tkinter import *
from tkinter import ttk

"""
MOZDA ENUM?
"""

tip_premestanja = {
    1: dodavanje_opreme,
    2: uklanjanje_opreme_iz_prostorije
}


class PremestanjeOpremeMeni:

    def __init__(self, root, selektovana_prostorija):
        self._root = root
        self._root.title("MENI")

        self.dodavanje = ttk.Button(self._root, text='Dodavanje slobodne opreme u prostoriju',
                                    command=lambda: self.otvori_novi_prozor(selektovana_prostorija, 1))
        self.dodavanje.grid(row=0, column=0, pady=10, padx=15)

        self.uklanjanje = ttk.Button(self._root, text='Uklanjanje opreme iz prostorije',
                                     command=lambda: self.otvori_novi_prozor(selektovana_prostorija, 2))
        self.uklanjanje.grid(row=1, column=0, pady=5)

    def otvori_novi_prozor(self, selektovana_prostorija, tip):
        self._root.destroy()
        tip_premestanja[tip](selektovana_prostorija)


def premestanje_opreme_meni(selektovana_prostorija):
    root = Tk()
    root.geometry('300x100')
    application = PremestanjeOpremeMeni(root, selektovana_prostorija)
    root.mainloop()
