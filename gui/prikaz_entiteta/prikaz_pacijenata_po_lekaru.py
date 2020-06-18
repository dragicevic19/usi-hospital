from tkinter import ttk
from tkinter import *

from repozitorijum.korisnik.korisnik_repozitorijum import lista_ucitanih_korisnika
from servisi.korisnik.korisnik_servis import KorisnikServis


class PrikazPacijenataPoLekaru:
    def __init__(self, root, lekar=None):
        self._root = root
        self._lekar = lekar
        self.treeview = ttk.Treeview(self._root)
        self.scroll = ttk.Scrollbar(self._root, orient='vertical', command=self.treeview.yview)
        self.scroll.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scroll.set)
        self.napravi_treeview()

    def napravi_treeview(self):
        self._napravi_zaglavlja()
        self.treeview.pack()
        self.treeview.config(height=13)
        self._popuni_treeview()

    def _napravi_zaglavlja(self):
        self.treeview["columns"] = ["korisnicko_ime", "br_zdravstvene", "ime", "prezime"]
        self.treeview["show"] = "headings"
        self.treeview.heading("korisnicko_ime", text="Korisnicko ime")
        self.treeview.heading("br_zdravstvene", text="Broj zdravstvene")
        self.treeview.heading("ime", text="Ime")
        self.treeview.heading("prezime", text="Prezime")

    def _popuni_treeview(self):
        lista_pacijenata = KorisnikServis.dobavi_spisak_pacijenata_po_lekaru(self._lekar.get_korisnicko_ime())
        print(lista_pacijenata)
        index = iid = 0
        for korisnik in lista_pacijenata:
            k = (
                korisnik.get_korisnicko_ime(), korisnik.get_br_zdravstvene(), korisnik.get_ime(),
                korisnik.get_prezime())
            self.treeview.insert("", index, iid, values=k)
            index = iid = index + 1


if __name__ == '__main__':
    root = Tk()
    lekar = lista_ucitanih_korisnika[10]
    a = PrikazPacijenataPoLekaru(root,lekar)
    root.mainloop()