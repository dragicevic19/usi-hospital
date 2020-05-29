from tkinter import ttk
from repository.korisnik.korisnik_repozitorijum import lista_ucitanih_korisnika


class PrikazKorisnika(object):

    def __init__(self, root, uloga=None):
        self._root = root
        self._uloga = uloga
        self.treeview = ttk.Treeview(self._root)
        self.scroll = ttk.Scrollbar(self._root, orient='vertical', command=self.treeview.yview)
        self.scroll.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scroll.set)
        self.napravi_treeview()

    def napravi_treeview(self):
        self.treeview["columns"] = ["korisnicko_ime", "uloga", "ime", "prezime"]
        self.treeview["show"] = "headings"
        self.treeview.heading("korisnicko_ime", text="Korisnicko ime")
        self.treeview.heading("uloga", text="Uloga")
        self.treeview.heading("ime", text="Ime")
        self.treeview.heading("prezime", text="Prezime")
        self.treeview.pack()
        self.treeview.config(height=13)
        self.__popuni_treeview()

    def __popuni_treeview(self):
        index = iid = 0
        for korisnik in lista_ucitanih_korisnika:
            k = (korisnik.get_korisnicko_ime(), korisnik.get_uloga(), korisnik.get_ime(), korisnik.get_prezime())
            self.treeview.insert("", index, iid, values=k)
            index = iid = index + 1
