from tkinter import ttk, Tk
from model.enum.uloga import Uloga
from servis.korisnik.korisnik_servis import KorisnikServis


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
        if self._uloga == Uloga.LEKAR.name:
            self._napravi_treeview_lekar()
        else:
            self._napravi_treeview_ostali()
        self.treeview.pack()
        self.treeview.config(height=13)
        self.__popuni_treeview()

    def _napravi_treeview_lekar(self):
        self.treeview["columns"] = ["korisnicko_ime", "uloga", "ime", "prezime", "radno_vreme",
                                    "spisak_specijalizacija"]
        self.treeview["show"] = "headings"
        self.treeview.heading("korisnicko_ime", text="Korisnicko ime")
        self.treeview.heading("uloga", text="Uloga")
        self.treeview.heading("ime", text="Ime")
        self.treeview.heading("prezime", text="Prezime")
        self.treeview.heading("radno_vreme", text="Radno vreme")
        self.treeview.heading("spisak_specijalizacija", text="Spisak specijalizacija")

    def _napravi_treeview_ostali(self):
        self.treeview["columns"] = ["korisnicko_ime", "uloga", "ime", "prezime"]
        self.treeview["show"] = "headings"
        self.treeview.heading("korisnicko_ime", text="Korisnicko ime")
        self.treeview.heading("uloga", text="Uloga")
        self.treeview.heading("ime", text="Ime")
        self.treeview.heading("prezime", text="Prezime")

    def __popuni_treeview(self):
        index = iid = 0
        lista_korisnika = KorisnikServis().dobavi_sve_korisnike_u_sistemu()
        for korisnik in lista_korisnika:
            if self._uloga:
                if self._uloga == korisnik.get_uloga() == Uloga.LEKAR.name:
                    k = (
                        korisnik.get_korisnicko_ime(), korisnik.get_uloga(), korisnik.get_ime(), korisnik.get_prezime(),
                        korisnik.get_radno_vreme(), korisnik.get_spisak_specijalizacija())
                    self.treeview.insert("", index, iid, values=k)
                    index = iid = index + 1
                elif self._uloga == korisnik.get_uloga():
                    k = (
                        korisnik.get_korisnicko_ime(), korisnik.get_uloga(), korisnik.get_ime(), korisnik.get_prezime())
                    self.treeview.insert("", index, iid, values=k)
                    index = iid = index + 1
            else:
                k = (korisnik.get_korisnicko_ime(), korisnik.get_uloga(), korisnik.get_ime(), korisnik.get_prezime())
                self.treeview.insert("", index, iid, values=k)
                index = iid = index + 1


if __name__ == '__main__':
    root = Tk()
    # PrikazKorisnika(root, "PACIJENT")
    PrikazKorisnika(root)
    root.mainloop()
