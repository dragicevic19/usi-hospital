from tkinter import ttk
from tkinter import *
from model.enum.uloga import Uloga
from servis.korisnik.korisnik_servis import KorisnikServis


class PrikazPacijenata:
    def __init__(self, root, lekar=None):
        self._root = root
        self._lekar = lekar
        self._lista_pacijenata = self._vrati_listu_pacijenata()
        self._korisnicko_ime_pretraga = ttk.Entry(self._root)
        self.treeview = ttk.Treeview(self._root)
        self.scroll = ttk.Scrollbar(self._root, orient='vertical', command=self.treeview.yview)
        self.scroll.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scroll.set)
        self.napravi_pretragu()
        self.napravi_treeview()

    def _vrati_listu_pacijenata(self):
        if self._lekar:
            return KorisnikServis().dobavi_spisak_pacijenata_po_lekaru(self._lekar.get_korisnicko_ime())
        else:
            return KorisnikServis().vrati_sve_korisnike_po_ulozi(Uloga.PACIJENT.name)

    def napravi_pretragu(self):
        Label(self._root, justify=LEFT, text="Pretraga pacijenta (korisnicko ime):", font="Times 12").pack()
        self._korisnicko_ime_pretraga.pack(pady=5)
        ttk.Button(self._root, text="Pretrazi", command=self.pronadji_pacijenta).pack()

    def pronadji_pacijenta(self):
        if self._lekar:
            self.pronadji_pacijente_za_specijalistu()
        else:
            self.pronadji_pacijente_za_lop()
        self.treeview.delete(*self.treeview.get_children())
        self._popuni_treeview()

    def pronadji_pacijente_za_specijalistu(self):
        if self._korisnicko_ime_pretraga.get():
            lista_pronadjenih = KorisnikServis().pronadji_pacijenta(self._korisnicko_ime_pretraga.get())
            if any(pacijent in lista_pronadjenih for pacijent in self._lista_pacijenata):
                self._lista_pacijenata = lista_pronadjenih
        else:
            self._lista_pacijenata = KorisnikServis().dobavi_spisak_pacijenata_po_lekaru(self._lekar.get_korisnicko_ime())

    def pronadji_pacijente_za_lop(self):
        if self._korisnicko_ime_pretraga.get():
            self._lista_pacijenata = KorisnikServis().pronadji_pacijenta(self._korisnicko_ime_pretraga.get())
        else:
            self._lista_pacijenata = KorisnikServis().vrati_sve_korisnike_po_ulozi(Uloga.PACIJENT.name)

    def napravi_treeview(self):
        self._napravi_zaglavlja()
        self.treeview.pack(pady=10)
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
        index = iid = 0
        for korisnik in self._lista_pacijenata:
            k = (
                korisnik.get_korisnicko_ime(), korisnik.get_br_zdravstvene(), korisnik.get_ime(),
                korisnik.get_prezime())
            self.treeview.insert("", index, iid, values=k)
            index = iid = index + 1


if __name__ == '__main__':
    root = Tk()
    lekar = KorisnikServis().dobavi_sve_korisnike_u_sistemu()[10]
    a = PrikazPacijenata(root, lekar)
    root.mainloop()
