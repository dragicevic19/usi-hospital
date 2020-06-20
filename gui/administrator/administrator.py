from tkinter import *
from tkinter import ttk
from gui.administrator.brisanje_korisnika import poziv_forme_brisanje_korisnika
from gui.administrator.dodavanje_korisnika import poziv_forme_unos_korisnika
from gui.administrator.azuriranje_korisnika import poziv_forme_azuriranje_korisnika
from gui.administrator.unos_prostorije import poziv_forme_unos_prostorije
from gui.administrator.brisanje_prostorije import poziv_forme_brisanje_prostorije
from gui.model_pocetne import ModelPocetne


class PocetnaFormaAdministrator(ModelPocetne):

    def __init__(self, root, korisnik):
        super().__init__(root, korisnik)
        self.postavljanje_dugmica()

    def postavljanje_dugmica(self):
        b1 = ttk.Button(self._frejm_dugmici, text="Dodavanje korisnika", command=self.akcija)
        b1.place(x=10, y=10, height=60, width=150)

        b2 = ttk.Button(self._frejm_dugmici, text="Azuriranje korisnika", command=self.akcija1)
        b2.place(x=220, y=10, height=60, width=150)

        b3 = ttk.Button(self._frejm_dugmici, text="Brisanje korisnika", command=self.akcija2)
        b3.place(x=430, y=10, height=60, width=150)

        b4 = ttk.Button(self._frejm_dugmici, text="Dodavanje prostorije", command=self.akcija3)
        b4.place(x=640, y=10, height=60, width=150)

        b5 = ttk.Button(self._frejm_dugmici, text="Brisanje prostorije", command=self.akcija4)
        b5.place(x=850, y=10, height=60, width=150)

    def priprema_akcije(self):
        self._okvir_izvrsavanja.destroy()
        super().kreiranje_frejma_za_izvrsavanje()

    #  IZMENITI NAZIVE METODA AKCIJA
    def akcija(self):
        self.priprema_akcije()
        poziv_forme_unos_korisnika(self._okvir_izvrsavanja)

    def akcija1(self):
        self.priprema_akcije()
        poziv_forme_azuriranje_korisnika(self._okvir_izvrsavanja)

    def akcija2(self):
        self.priprema_akcije()
        poziv_forme_brisanje_korisnika(self._okvir_izvrsavanja)

    def akcija3(self):
        self.priprema_akcije()
        poziv_forme_unos_prostorije(self._okvir_izvrsavanja)

    def akcija4(self):
        self.priprema_akcije()
        poziv_forme_brisanje_prostorije(self._okvir_izvrsavanja)


# PROMENITI NES
def poziv_forme_administrator(korisnik):
    root = Tk()
    # root.geometry('400x190')
    nes = PocetnaFormaAdministrator(root, korisnik)
    root.mainloop()


# if __name__ == '__main__':
#     poziv_forme_administrator(lista_ucitanih_korisnika[0])
