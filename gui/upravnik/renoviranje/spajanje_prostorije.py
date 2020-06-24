import datetime
from tkinter import *
from tkinter import ttk, messagebox
from model.dto.dogadjaji_dto.spajanje_prostorije_dto import SpajanjeProstorijeDTO
from servis.prostorije.prostorije_servis import ProstorijeServis


class SpajanjeProstorije(object):
    namene_prostorija = ('sala za preglede', 'operaciona sala', 'soba za lezanje')

    def __init__(self, root, prostorija_1, prostorija_2):

        self._root = root
        self._root.title("Spajanje prostorija")
        self._prostorija_1 = prostorija_1
        self._prostorija_2 = prostorija_2
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
        podrazumevana_vrednost = self._nova_namena.get()
        ttk.OptionMenu(self._root, self._nova_namena, podrazumevana_vrednost, *self.namene_prostorija).grid(row=5,
                                                                                                            column=2)

    def provera_unosa(self):
        if not self.provera_datuma():
            messagebox.showerror("GRESKA", "Niste uneli validan datum (DD/MM/GGGG)")
        elif not self.provera_broja_prostorije():
            messagebox.showerror("GRESKA", "Broj prostorije je zauzet!")
        else:
            prostorijaDTO1 = SpajanjeProstorijeDTO(self._datum_pocetka, self._datum_zavrsetka, self._prostorija_1,
                                                   self._nova_namena.get(), self._novi_broj.get())

            prostorijaDTO2 = SpajanjeProstorijeDTO(self._datum_pocetka, self._datum_zavrsetka, self._prostorija_2,
                                                   self._nova_namena.get(), self._novi_broj.get())
            self.provera_zauzeca(prostorijaDTO1, prostorijaDTO2)

    def provera_zauzeca(self, prostorija_dto_1, prostorija_dto_2):
        if ProstorijeServis().spajanje_prostorija(prostorija_dto_1, prostorija_dto_2):
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
        ProstorijeServis().obrisi_sobe(self._prostorija_1, self._prostorija_2)
        if not ProstorijeServis().slobodan_broj_prostorije(self._prostorija_1.get_sprat(), self._novi_broj.get()):
            return False
        return True


def spajanje_prostorije(prostorija_1, prostorija_2):
    root = Tk()
    root.geometry('600x250')
    application = SpajanjeProstorije(root, prostorija_1, prostorija_2)
    root.mainloop()
