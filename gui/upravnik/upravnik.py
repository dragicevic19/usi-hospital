from tkinter import *
from tkinter import ttk
from gui.model_pocetne import ModelPocetne
from gui.upravnik.dodavanje_opreme import poziv_forme_unos_opreme
from gui.upravnik.azuriranje_opreme import poziv_forme_azuriranje_opreme
from gui.upravnik.brisanje_opreme import poziv_forme_brisanje_opreme
from gui.upravnik.renoviranje_meni import poziv_forme_za_renovaciju_prostorije

SIRINA_DUGMETA = 40
DUZINA_DUGMETA = 150


class PocetnaFormaUpravnik(ModelPocetne):

    def __init__(self, root, korisnik):
        super().__init__(root, korisnik)
        self.postavi_gornje_dugmice()
        self.postavi_donje_dugmice()

    def postavi_gornje_dugmice(self):
        b1 = ttk.Button(self._frejm_dugmici, text="Renoviranje prostorije", command=self.pokretanje_renoviranje_prostorije)
        b1.place(x=10, y=10, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

        b2 = ttk.Button(self._frejm_dugmici, text="Pretraga prostorije", command=self.akcija2)
        b2.place(x=220, y=10, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

        b3 = ttk.Button(self._frejm_dugmici, text="Dodavanje opreme", command=self.pokretanje_unos_opreme)
        b3.place(x=430, y=10, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

        b4 = ttk.Button(self._frejm_dugmici, text="Azuriranje opeme", command=self.pokretanje_azuriranje_opreme)
        b4.place(x=640, y=10, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

        b5 = ttk.Button(self._frejm_dugmici, text="Brisanje opreme", command=self.pokretanje_brisanje_opreme)
        b5.place(x=850, y=10, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

    def postavi_donje_dugmice(self):
        b4 = ttk.Button(self._frejm_dugmici, text="Azuriranje informacija o lekarima", command=self.akcija6)
        b4.place(x=335, y=60, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

        b5 = ttk.Button(self._frejm_dugmici, text="Generisanje izvestaja", command=self.akcija7)
        b5.place(x=535, y=60, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

    """
        IZMENITI NAZIVE SVIH AKCIJA
        
    """

    def osvezi_okvir_za_izvrsavanje(self):
        self._okvir_izvrsavanja.destroy()
        super().kreiranje_frejma_za_izvrsavanje()

    def pokretanje_renoviranje_prostorije(self):
        self.osvezi_okvir_za_izvrsavanje()
        poziv_forme_za_renovaciju_prostorije(self._okvir_izvrsavanja)

    def akcija2(self):
        pass

    def pokretanje_unos_opreme(self):
        self.osvezi_okvir_za_izvrsavanje()
        poziv_forme_unos_opreme(self._okvir_izvrsavanja)

    def pokretanje_azuriranje_opreme(self):
        self.osvezi_okvir_za_izvrsavanje()
        poziv_forme_azuriranje_opreme(self._okvir_izvrsavanja)

    def pokretanje_brisanje_opreme(self):
        self.osvezi_okvir_za_izvrsavanje()
        poziv_forme_brisanje_opreme(self._okvir_izvrsavanja)

    def akcija6(self):
        pass

    def akcija7(self):
        pass


def poziv_forme_upravnik(korisnik):
    root = Tk()
    # promeniti naziv kreni
    kreni = PocetnaFormaUpravnik(root, korisnik)
    root.mainloop()


# if __name__ == '__main__':
#     poziv_forme_upravnik(lista_ucitanih_korisnika[0])
