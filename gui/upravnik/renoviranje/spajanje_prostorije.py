import datetime
from tkinter import *
from tkinter import ttk, messagebox

from model.DTO.renoviranjeDogadjajDTO import RenoviranjeDTO
from services.prostorije.prostorije_servis import ProstorijeService


class SpajanjeProstorije(object):
    namene_prostorija = ('sala za preglede', 'operaciona sala', 'soba za lezanje')

    def __init__(self, root, prostorija1, prostorija2):

        self._root = root
        self._root.title("Spajanje prostorija")
        self._prostorija1 = prostorija1
        self._prostorija2 = prostorija2
        self._datum_pocetka_radova = ttk.Entry(self._root)
        self._datum_zavrsetka_radova = ttk.Entry(self._root)
        self._novi_broj = ttk.Entry(self._root)
        self._nova_namena = StringVar(self._root)
        self._nova_namena.set(self.namene_prostorija[0])

        self.izaberi_datum()
        self.unesi_podatke()
        potvrdi_dugme = ttk.Button(self._root, text="AZURIRAJ PROSTORIJU", command=self.provera_unosa)
        potvrdi_dugme.grid(row=6, column=2, columnspan=10)

    def izaberi_datum(self):
        Label(self._root, justify=LEFT, text="Datum pocetka radova (dd/mm/gggg):", font="Times 15").grid(row=1,
                                                                                                         column=1,
                                                                                                         pady=10)
        self._datum_pocetka_radova.grid(row=1, column=2, columnspan=10)

        Label(self._root, justify=LEFT, text="Datum zavrsetka radova (dd/mm/gggg)", font="Times 15").grid(row=2,
                                                                                                          column=1,
                                                                                                          pady=10)
        self._datum_zavrsetka_radova.grid(row=2, column=2, columnspan=10)

    def unesi_podatke(self):
        Label(self._root, justify=LEFT, text='Novi broj prostorije: ', font="Times 15").grid(row=4, column=1, pady=10)
        self._novi_broj.grid(row=4, column=2, columnspan=10)
        Label(self._root, justify=LEFT, text='Nova namena prostorije: ', font="Times 15").grid(row=5, column=1, pady=10)
        default = self._nova_namena.get()
        ttk.OptionMenu(self._root, self._nova_namena, default, *self.namene_prostorija).grid(row=5, column=2)

    def provera_unosa(self):
        if not self.provera_datuma():
            messagebox.showerror("GRESKA", "Niste uneli validan datum (DD/MM/GGGG)")
        elif not self.provera_broja_prostorije():
            messagebox.showerror("GRESKA", "Broj prostorije je zauzet!")
        else:
            prostorijaDTO1 = RenoviranjeDTO(self._datum_pocetka, self._datum_zavrsetka, self._prostorija1,
                                            namena=self._nova_namena.get(), novi_broj=self._novi_broj.get())

            prostorijaDTO2 = RenoviranjeDTO(self._datum_pocetka, self._datum_zavrsetka, self._prostorija2,
                                            namena=self._nova_namena.get(), novi_broj=self._novi_broj.get())
            self.provera_zauzeca(prostorijaDTO1, prostorijaDTO2)

    def provera_zauzeca(self, prostorijaDTO1, prostorijaDTO2):
        if ProstorijeService.spajanje_prostorija(prostorijaDTO1, prostorijaDTO2):
            messagebox.showinfo("USPESNO", "Uspesno ste zakazali renoviranje prostorije")
            self._root.destroy()
        else:
            messagebox.showerror("GRESKA", "Bar jedna od prostorija je zauzeta u tom periodu")

    def provera_datuma(self):
        try:
            d, m, g = self._datum_pocetka_radova.get().split("/")
            self._datum_pocetka = datetime.date(int(g), int(m), int(d))
            d, m, g = self._datum_zavrsetka_radova.get().split("/")
            self._datum_zavrsetka = datetime.date(int(g), int(m), int(d))
            if self._datum_pocetka < datetime.date.today() or self._datum_zavrsetka < self._datum_pocetka:
                return False
        except ValueError:
            return False
        return True

    def provera_broja_prostorije(self):
        if not ProstorijeService.slobodan_broj_prostorije(self._prostorija1, self._prostorija2, self._novi_broj.get()):
            return False
        return True


def spajanje_prostorije(prostorija1, prostorija2):
    root = Tk()
    root.geometry('600x250')
    application = SpajanjeProstorije(root, prostorija1, prostorija2)
    root.mainloop()
