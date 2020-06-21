from gui.upravnik.renoviranje.izmena_namene import *
from model.dto.dogadjaji_dto.dogadjaj_dto import DogadjajDTO


class OstaleRenovacije:

    def __init__(self, root, selektovana_prostorija):
        self._root = root
        self._root.title('Ostale renovacije')
        self._prostorija = selektovana_prostorija
        self._datum_pocetka_radova = None
        self._datum_zavrsetka_radova = None

        self.izaberi_datum()
        potvrdi_dugme = ttk.Button(self._root, text="POTVRDI", command=self.provera_unosa)
        potvrdi_dugme.grid(row=4, column=1, columnspan=10)

    def izaberi_datum(self):
        Label(self._root, justify=LEFT, text="Datum pocetka radova (dd/mm/gggg):", font="Times 15").grid(row=1,
                                                                                                         column=1,
                                                                                                         pady=10)
        self._datum_pocetka_radova = ttk.Entry(self._root)
        self._datum_pocetka_radova.grid(row=1, column=2, columnspan=10)

        Label(self._root, justify=LEFT, text="Datum pocetka radova (dd/mm/gggg)", font="Times 15").grid(row=2,
                                                                                                        column=1,
                                                                                                        pady=10)
        self._datum_zavrsetka_radova = ttk.Entry(self._root)
        self._datum_zavrsetka_radova.grid(row=2, column=2, columnspan=10)

    def provera_unosa(self):
        if not self.provera_datuma():
            messagebox.showerror("GRESKA", "Niste uneli validan datum (DD/MM/GGGG)")
        else:
            renoviranjeDTO = DogadjajDTO(self._datum_pocetka, self._datum_zavrsetka, self._prostorija)
            self.provera_zauzeca(renoviranjeDTO)

    def provera_zauzeca(self, renoviranjeDTO):
        if ProstorijeServis().izmeni_namenu(renoviranjeDTO):
            messagebox.showinfo("USPESNO", "Uspesno ste zakazali renoviranje prostorije")
            self._root.destroy()
        else:
            messagebox.showerror("GRESKA", "Prostorija je zauzeta u tom periodu")

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


def ostale_renovacije(selektovana_prostorija):
    root = Tk()
    root.geometry('550x200')
    application = OstaleRenovacije(root, selektovana_prostorija)
    root.mainloop()
