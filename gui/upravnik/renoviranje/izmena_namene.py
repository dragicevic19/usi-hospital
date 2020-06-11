import datetime
from tkinter import *
from tkinter import ttk, messagebox

from model.DTO.renoviranjeDogadjajDTO import RenoviranjeDTO
from repository.prostorije.prostorije_repozitorijum import lista_ucitanih_prostorija
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

        potvrdi_dugme = ttk.Button(self._root, text="AZURIRAJ PROSTORIJU", command=self.provera_unosa)
        potvrdi_dugme.grid(row=4, column=1, columnspan=10)

    def izaberi_datum(self):
        Label(self._root, justify=LEFT, text="Datum pocetka radova (dd/mm/gggg):", font="Times 15").grid(row=1,
                                                                                                         column=1,
                                                                                                         pady=10)
        self._datum_pocetka_radova = ttk.Entry(self._root)
        self._datum_pocetka_radova.grid(row=1, column=2, columnspan=10)

        Label(self._root, justify=LEFT, text="Datum zavrsetka radova (dd/mm/gggg)", font="Times 15").grid(row=2,
                                                                                                          column=1,
                                                                                                          pady=10)
        self._datum_zavrsetka_radova = ttk.Entry(self._root)
        self._datum_zavrsetka_radova.grid(row=2, column=2, columnspan=10)

    def izaberi_namenu(self):
        Label(self._root, text="Izaberite novu namenu", font="Times 15").grid(row=3, column=1, pady=10)
        default = self._prostorija.get_namena_prostorije()
        ttk.OptionMenu(self._root, self._namena, default, *self.namene_prostorija).grid(row=3, column=2)

    def provera_unosa(self):
        if self._prostorija.get_namena_prostorije() == self._namena.get():
            messagebox.showerror("GRESKA", "Niste promenili namenu prostorije")
        elif not self.provera_datuma():
            messagebox.showerror("GRESKA", "Niste uneli validan datum (DD/MM/GGGG)")
        else:
            prostorijaDTO = RenoviranjeDTO(self._datum_pocetka, self._datum_zavrsetka,
                                           self._prostorija, namena=self._namena.get())
            self.provera_zauzeca(prostorijaDTO)

    def provera_zauzeca(self, prostorijaDTO):
        if ProstorijeService.izmeni_namenu(prostorijaDTO):
            messagebox.showinfo("USPESNO", "Uspesno ste zakazali renoviranje prostorije")
            self._root.destroy()
        else:
            messagebox.showerror("GRESKA", "Za prostoriju je vec zakazno renoviranje ili operacija u tom periodu")

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


def izmena_namene(selektovana_prostorija):
    root = Tk()
    root.geometry('550x200')
    application = IzmenaNamene(root, selektovana_prostorija)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('550x200')
    prostorija = lista_ucitanih_prostorija[0]
    application = IzmenaNamene(root, prostorija)
    root.mainloop()
