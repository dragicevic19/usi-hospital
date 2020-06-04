import datetime
from tkinter import *
from model.prostorija import Prostorija
from tkinter import ttk, messagebox

from repository.prostorije.prostorije_repozitorijum import lista_ucitanih_prostorija, ProstorijeRepository
from services.prostorije.prostorije_servis import ProstorijeService


class IzmenaNamene:
    namene_prostorija = ('sala za preglede', 'operaciona sala', 'soba za lezanje')

    def __init__(self, root, selektovana_prostorija):
        self._root = root
        self._datum_pocetka_radova = None
        self._datum_zavrsetka_radova = None
        self._prostorija = selektovana_prostorija
        self._namena = StringVar(self._root)
        self._namena.set(self.namene_prostorija[0])
        self._prostorija = selektovana_prostorija

        self.izaberi_datum()
        self.izaberi_namenu()

    def izaberi_datum(self):
        Label(self._root, justify=LEFT, text="Datum pocetka radova (dd/mm/gggg):", font="Times 15").grid(row=1,
                                                                                                         column=1,
                                                                                                         pady=10)
        self._datum_pocetka_radova = ttk.Entry(self._root)
        self._datum_pocetka_radova.grid(row=1, column=2, columnspan=10)

        Label(self._root, justify=LEFT, text="Datum pocetka radova (dd/mm/gggg)", font="Times 15").grid(row=2, column=1,
                                                                                                        pady=10)
        self._datum_zavrsetka_radova = ttk.Entry(self._root)
        self._datum_zavrsetka_radova.grid(row=2, column=2, columnspan=10)

        potvrdi_dugme = ttk.Button(self._root, text="AZURIRAJ PROSTORIJU", command=self.promeni_namenu)
        potvrdi_dugme.grid(row=4, column=1, columnspan=10)

    def izaberi_namenu(self):
        Label(self._root, text="Izaberite novu namenu", font="Times 15").grid(row=3, column=1, pady=10)
        default = self._prostorija.get_namena_prostorije()
        ttk.OptionMenu(self._root, self._namena, default, *self.namene_prostorija).grid(row=3, column=2)

    def promeni_namenu(self):
        if self.provera_unosa():
            ProstorijeService.izmeni_namenu(self._prostorija, self._namena.get())

    def provera_unosa(self):
        if self._prostorija.get_namena_prostorije() == self._namena.get():
            messagebox.showerror("GRESKA", "Niste promenili namenu prostorije")
            return False
        try:
            d, m, g = self._datum_pocetka_radova.get().split("/")
            datum_pocetka = datetime.date(int(g), int(m), int(d))
            d, m, g = self._datum_zavrsetka_radova.get().split("/")
            datum_zavrsetka = datetime.date(int(g), int(m), int(d))
        except:
            messagebox.showerror("GRESKA", "Niste uneli validan format datuma (DD/MM/GGGG)")
            return False
        return True


def izmena_namene(selektovana_prostorija):
    root = Tk()
    root.geometry('425x425')
    application = IzmenaNamene(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x200')
    prostorija = lista_ucitanih_prostorija[0]
    application = IzmenaNamene(root, prostorija)
    root.mainloop()
