from tkinter import *
from gui.upravnik import ispis_kalendara
from gui.upravnik.ispis_kalendara import PrikazKalendara
from model.prostorija import Prostorija
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar


class IzmenaNamene:
    namene_prostorija = ('sala za preglede', 'operaciona sala', 'sala za lezanje')
    root1 = Tk()
    datum_pocetka = PrikazKalendara(root1)
    root1.withdraw()

    def __init__(self, root, selektovana_prostorija):
        self._root = root
        self._datum_pocetka_radova = None
        self._datum_zavrsetka_radova = None
        self._prostorija = selektovana_prostorija
        self._namena = StringVar(self._root)
        self._namena.set(self.namene_prostorija[0])
        self._prostorija = selektovana_prostorija
        self._ispis = "---------"

        self.izaberi_datum()
        self.promeni_namenu()

    def prikaz_kalendara(self):

        datum_pocetka1 = self.datum_pocetka.get_datum()
        print(datum_pocetka1)
        self._ispis = self.datum_pocetka

    def izaberi_datum(self):
        Label(self._root, text="Datum pocetka radova:", font="Times 15").grid(row=1, column=1, pady=10)
        ttk.Button(self._root, text="Izaberi", command=self.prikaz_kalendara).grid(row=1, column=16)

        self._datum_pocetka_radova = Label(self._root, text=self._ispis, font="Times 15").grid(row=1, column=2,
                                                                                               columnspan=10)
        Label(self._root, text="Datum kraja radova:", font="Times 15").grid(row=2, column=1, pady=10)
        self._datum_zavrsetka_radova = Label(self._root, text=self._ispis, font="Times 15").grid(row=2, column=2,
                                                                                                 columnspan=11)
        ttk.Button(self._root, text="Izaberi", command=self.prikaz_kalendara).grid(row=2, column=16)

    def promeni_namenu(self):
        Label(self._root, text="Izaberite novu namenu", font="Times 15").grid(row=3, column=1, pady=10)
        default = self._prostorija.get_namena_prostorije()
        ttk.OptionMenu(self._root, self._namena, default, *self.namene_prostorija).grid(row=3, column=2)


def izmena_namene(selektovana_prostorija):
    root = Tk()
    root.geometry('425x425')
    application = IzmenaNamene(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x200')
    prostorija = Prostorija('3', '301', 'krevet;20|stalak za infuziju;20|rendgen aparat;10', 'operaciona sala', )
    application = IzmenaNamene(root, prostorija)
    root.mainloop()
