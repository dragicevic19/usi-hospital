from tkinter import *
from gui.upravnik import ispis_kalendara
from model.prostorija import Prostorija
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar


class IzmenaNamene(PrikazKalendara):
    namene_prostorija = ('sala za preglede', 'operaciona sala', 'sala za lezanje')

    def __init__(self, root, selektovana_prostorija):
        self._root = root
        self._datum_pocetka_radova = None
        self._datum_zavrsetka_radova = None
        self._prostorija = selektovana_prostorija
        self._namena = StringVar(self._root)
        self._namena.set(self.namene_prostorija[0])
        self._prostorija = selektovana_prostorija

        self.izaberi_datum()

        self.promeni_namenu()

        
    def p1rikaz_kalendara(self):
        ispis_kalendara.prikaz_kalendara(self._datum_pocetka_radova)
        print(self._datum_pocetka_radova)

    def izaberi_datum(self):
        Label(self._root, text="Izaberite datum za pocetak radova:", font="Times 15").grid(row=1, column=1, pady=10)
        ttk.Button(self._root, text="Izaberi", command=self.p1rikaz_kalendara).grid(row=1, column=2)

        self._datum_pocetka_radova = ttk.Entry(self._root).grid(row=1, column=2, columnspan=10)
        Label(self._root, text="Datum do (dd/mm/gggg):", font="Times 15").grid(row=2, column=1, pady=10)
        self._datum_zavrsetka_radova = ttk.Entry(self._root).grid(row=2, column=2, columnspan=10)

    def promeni_namenu(self):
        Label(self._root, text="Izaberite novu namenu", font="Times 15").grid(row=3, column=1, pady=10)
        default = self._prostorija.get_namena_prostorije()
        ttk.OptionMenu(self._root, self._namena, default, *self.namene_prostorija).grid(row=3, column=2)


    def pick_date_dialog(self, ROOT):

        top = tk.Toplevel(ROOT)

        cal = Calendar(top,
                       font="Arial 10", background='darkblue',
                       foreground='white', selectmode='day')
        cal.grid()
        ttk.Button(top, text="OK", command=lambda: self.print_sel(cal, ROOT)).grid()


    def print_sel(self,cal, ROOT, event):
        datum = (cal.get_date())
        ROOT.destroy()

    def prikaz_kalendara(datum):
        ROOT = tk.Tk()
        ROOT.withdraw()  # hide naff extra window
        ROOT.title('Please choose a date')

        pick_date_dialog(ROOT, datum)
        ROOT.mainloop()


def izmena_namene(selektovana_prostorija):
    root = Tk()
    root.geometry('425x425')
    application = IzmenaNamene(root)
    root.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.geometry('425x200')
    prostorija = Prostorija('3','301','krevet;20|stalak za infuziju;20|rendgen aparat;10','operaciona sala',)
    application = IzmenaNamene(root, prostorija)
    root.mainloop()