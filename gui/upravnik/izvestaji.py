from tkinter import *
from tkinter import ttk
from tkinter import Radiobutton, messagebox
from model.konstante.konstante import REGEX_DATUM
from servis.izvestaji.izvestaj_lekara_servis import IzvestajLekaraServis
from servis.izvestaji.izvestaj_prostorije_servis import IzvestajProstorijeServis


class FormaZaIzvestaje:

    def __init__(self, root):
        self._root = root
        self._datum_od = None
        self._datum_do = None
        self._radio_parametar = IntVar()
        self.postavka_za_datume()
        self.postavi_dugmice()

    def postavka_za_datume(self):
        datum_od_labela = ttk.Label(self._root, font="Times 14", text="Pocetni datum (dd/mm/gggg):")
        datum_od_labela.grid(row=1, column=1, padx=10, pady=10)
        self._datum_od = ttk.Entry(self._root)
        self._datum_od.grid(row=1, column=2, padx=10, pady=10)

        datum_do_labela = ttk.Label(self._root, font="Times 14", text="Krajnji datum (dd/mm/gggg):")
        datum_do_labela.grid(row=2, column=1, padx=10, pady=10)
        self._datum_do = ttk.Entry(self._root)
        self._datum_do.grid(row=2, column=2, padx=10, pady=10)

    def postavi_dugmice(self):
        izvestaj_lekar = Radiobutton(self._root, text="Izvestaj za lekare", variable=self._radio_parametar, value=0)
        izvestaj_lekar.grid(row=3, column=1, padx=10, pady=10)

        izvestaj_sobe = Radiobutton(self._root, text="Izvestaj za sobe", variable=self._radio_parametar, value=1)
        izvestaj_sobe.grid(row=3, column=2, padx=10, pady=10)

        ttk.Button(self._root, text="Izgenerisi izvestaj", command=self.generisi).grid(row=4, column=1, padx=10, pady=10)

    def generisi(self):
        if not REGEX_DATUM.match(self._datum_od.get()) or not REGEX_DATUM.match(self._datum_do.get()):
            messagebox.showerror("GRESKA", "Neispravan format datuma!")

        # videti da se koriste dto klase za datume
        if self._radio_parametar.get() == 1:
            IzvestajProstorijeServis(self._datum_od.get(), self._datum_do.get()).pripremi_i_izgenerisi_izvestaj()
        else:
            IzvestajLekaraServis(self._datum_od.get(), self._datum_do.get()).pripremi_i_izgenerisi_izvestaj()

def poziv_forma_za_izvestaje_za_upravnika(root):
    FormaZaIzvestaje(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    FormaZaIzvestaje(root)
    root.mainloop()
