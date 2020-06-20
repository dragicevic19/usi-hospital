from tkinter import *
from tkinter import ttk
from gui.model_pocetne import ModelPocetne
from repozitorijum.korisnik.korisnik_repozitorijum import lista_ucitanih_korisnika
from gui.upravnik.dodavanje_opreme import poziv_forme_unos_opreme
from gui.upravnik.azuriranje_opreme import poziv_forme_azuriranje_opreme
from gui.upravnik.brisanje_opreme import poziv_forme_brisanje_opreme
from gui.upravnik.renoviranje_meni import poziv_forme_za_renovaciju_prostorije

SIRINA_DUGMETA = 40
DUZINA_DUGMETA = 150


class PocetnaFormaUpravnik(ModelPocetne):

    def __init__(self, root, korisnik):
        super().__init__(root, korisnik)
        self.postavi_dugmice_gornje()
        self.postavi_dugmice_donje()

    def postavi_dugmice_gornje(self):
        b1 = ttk.Button(self._frejm_dugmici, text="Renoviranje prostorije", command=self.akcija1)
        b1.place(x=10, y=10, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

        b2 = ttk.Button(self._frejm_dugmici, text="Pretraga prostorije", command=self.akcija2)
        b2.place(x=220, y=10, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

        b3 = ttk.Button(self._frejm_dugmici, text="Dodavanje opreme", command=self.akcija3)
        b3.place(x=430, y=10, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

        b4 = ttk.Button(self._frejm_dugmici, text="Azuriranje opeme", command=self.akcija4)
        b4.place(x=640, y=10, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

        b5 = ttk.Button(self._frejm_dugmici, text="Brisanje opreme", command=self.akcija5)
        b5.place(x=850, y=10, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

    def postavi_dugmice_donje(self):
        b4 = ttk.Button(self._frejm_dugmici, text="Azuriranje informacija o lekarima", command=self.akcija6)
        b4.place(x=335, y=60, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

        b5 = ttk.Button(self._frejm_dugmici, text="Generisanje izvestaja", command=self.akcija7)
        b5.place(x=535, y=60, height=SIRINA_DUGMETA, width=DUZINA_DUGMETA)

    def visa_akcija(self):
        self._frejm_izvrsavanja.destroy()
        super().kreiranje_frejma_za_izvrsavanje()

    def akcija1(self):
        self.visa_akcija()
        poziv_forme_za_renovaciju_prostorije(self._frejm_izvrsavanja)

    def akcija2(self):
        pass

    def akcija3(self):
        self.visa_akcija()
        poziv_forme_unos_opreme(self._frejm_izvrsavanja)

    def akcija4(self):
        self.visa_akcija()
        poziv_forme_azuriranje_opreme(self._frejm_izvrsavanja)

    def akcija5(self):
        self.visa_akcija()
        poziv_forme_brisanje_opreme(self._frejm_izvrsavanja)

    def akcija6(self):
        pass

    def akcija7(self):
        pass


def poziv_forme_upravnik(korisnik):
    root = Tk()
    kreni = PocetnaFormaUpravnik(root, korisnik)
    root.mainloop()


if __name__ == '__main__':
    poziv_forme_upravnik(lista_ucitanih_korisnika[0])
