from gui.prikaz_entiteta.prikaz_prostorija import PrikazProstorija
from model.enum.renoviranje import TipRenoviranja
from gui.upravnik.renoviranje.izmena_namene import izmena_namene
from gui.upravnik.renoviranje.premestanje_opreme_meni import premestanje_opreme_meni
from gui.upravnik.renoviranje.spajanje_prostorije import spajanje_prostorije
from gui.upravnik.renoviranje.deljenje_prostorije import deljenje_prostorije
from gui.upravnik.renoviranje.ostale_renovacije import ostale_renovacije
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

""" STAVITI U RECNIKE """
metode_renovacija = {TipRenoviranja.IZMENA_NAMENE: izmena_namene,
                     TipRenoviranja.PREMESTANJE_OPREME: premestanje_opreme_meni,
                     TipRenoviranja.SPAJANJE_PROSTORIJA: spajanje_prostorije,
                     TipRenoviranja.DELJENJE_PROSTORIJE: deljenje_prostorije,
                     TipRenoviranja.OSTALE_RENOVACIJE: ostale_renovacije}


class RenoviranjeProstorije(PrikazProstorija):
    def __init__(self, root, tip_renoviranja):
        super().__init__(root)
        self._tip_renoviranja = tip_renoviranja
        potvrdi_dugme = ttk.Button(self._root, text="ZAKAZI RENOVIRANJE PROSTORIJE", command=self.renoviraj_prostoriju)
        potvrdi_dugme.pack(fill='x')

    def renoviraj_prostoriju(self):
        if self._tip_renoviranja == TipRenoviranja.SPAJANJE_PROSTORIJA:
            self.poziv_spajanje_prostorija()
        else:
            self.poziv_ostalih_tipova_renoviranja()

    def poziv_ostalih_tipova_renoviranja(self):
        try:
            prostorija = self.selektovana_prostorija()
            self._root.destroy()
            metode_renovacija[self._tip_renoviranja](prostorija)
        except:
            messagebox.showerror("GRESKA", "Izaberite jednu prostoriju")

    def poziv_spajanje_prostorija(self):
        selektovane_prostorije = self.selektuj_vise_prostorija()
        if selektovane_prostorije:
            self._root.destroy()
            spajanje_prostorije(*selektovane_prostorije)
        else:
            messagebox.showerror("GRESKA", "Morate da izaberete dve prostorije!")


def poziv_forme_odabir_prostorije(tip_renoviranja):
    root = Tk()
    application = RenoviranjeProstorije(root, tip_renoviranja)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_forme_odabir_prostorije(root)
