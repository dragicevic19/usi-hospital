from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model.kreiranje_objekata_entiteta import KreiranjeObjekata
from model.prostorija import Prostorija
from services.prostorijeService import ProstorijeService
from gui.prikazProstorija import PrikazProstorija


class RenoviranjeProstorije(PrikazProstorija):
    def __init__(self, root):
        super().__init__(root)
        potvrdi_dugme = ttk.Button(self._root, text="ZAKAZI RENOVIRANJE PROSTORIJE", command=self.renoviraj_prostoriju)
        potvrdi_dugme.pack(fill='x')

    def renoviraj_prostoriju(self):
        try:
            ProstorijeService.renoviranje_prostorije(self.selektovana_prostorija())
            messagebox.showinfo("USPESNO", "Zakazali ste renoviranje prostorije!")
            self._root.destroy()
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali prostoriju!")


def poziv_forme_unos_prostorije(root):
    application = RenoviranjeProstorije(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_forme_unos_prostorije(root)
