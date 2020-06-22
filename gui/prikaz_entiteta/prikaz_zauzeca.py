from tkinter import ttk
from tkinter import *
from servis.kalendar.kalendar_servis import KalendarServis


class PrikazZauzeca(object):

    def __init__(self, root, korisnicko_ime_lekara):
        self._root = root
        self.treeview = ttk.Treeview(self._root)
        self.scroll = ttk.Scrollbar(self._root, orient='vertical', command=self.treeview.yview)
        self.scroll.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scroll.set)
        self._korisnicko_ime_lekara = korisnicko_ime_lekara
        self.napravi_treeview()

    def napravi_treeview(self):
        self.treeview["columns"] = ["datum", "vreme", "broj_slotova", "soba", "pacijent"]
        self.treeview["show"] = "headings"
        self.treeview.heading("datum", text="Datum")
        self.treeview.heading("vreme", text="Vreme")
        self.treeview.heading("broj_slotova", text="Vreme trajanja")
        self.treeview.heading("soba", text="Soba")
        self.treeview.heading("pacijent", text="Pacijent")
        self.treeview.pack()
        self.treeview.config(height=13)
        self.__popuni_treeview()

    def __popuni_treeview(self):
        index = iid = 0
        lista_dogadjaja = KalendarServis().dobavi_listu_dogadjaja()
        for dogadjaj in lista_dogadjaja:
            if self._korisnicko_ime_lekara in dogadjaj.spisak_doktora:
                dog = (dogadjaj.datum, dogadjaj.vreme_pocetka_str, str(dogadjaj.broj_termina * 30) + " minuta",
                       "sprat: " + dogadjaj.sprat + " | soba: " + dogadjaj.broj_prostorije,
                       dogadjaj.pacijent)
                self.treeview.insert("", index, iid, values=dog)
                index = iid = index + 1


if __name__ == '__main__':
    root = Tk()
    PrikazZauzeca(root, "goran431")
    root.mainloop()
