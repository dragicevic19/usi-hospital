from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.prikaz_entiteta.prikaz_prostorija import PrikazProstorija



class BrisanjeProstorije(PrikazProstorija):

    def __init__(self, root,prostorije_servis):
        super().__init__(root,prostorije_servis, prostorije_servis.prikupi_prostorije_za_prikaz())
        self._prostorije_servis = prostorije_servis
        potvrdi_dugme = ttk.Button(self._root, text="OBRISI", command=self.obrisi_prostoriju)
        potvrdi_dugme.pack(fill='x')

    def obrisi_prostoriju(self):
        try:
            self._prostorije_servis.brisanje_prostorije(self.selektovana_prostorija())
            messagebox.showinfo("USPESNO", "Uspesno ste obrisali prostoriju!")
            self._root.destroy()
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali prostoriju!")


def poziv_forme_brisanje_prostorije(root,prostorije_servis):
    BrisanjeProstorije(root,prostorije_servis)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_forme_brisanje_prostorije(root)
