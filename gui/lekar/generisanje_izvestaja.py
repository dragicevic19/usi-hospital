from tkinter import ttk

from servis.izvestaji.sopstveni_izvestaj_lekara_servis import poziv_forme_za_prikaz_izvestaja


class FormaIzvestajaLekara:


    def __init__(self,root,korisnik):
        self._root = root
        self._korisnik = korisnik
        ttk.Label(self._root,text = "Unesi broj dana za izvestaj: ").pack()
        self.unos = ttk.Entry(self._root)
        self.unos.pack()
        self.dugme = ttk.Button(self._root,text = "Stampaj izvestaj",command = self.generisi).pack()

    def generisi(self):
        broj_dana = int(self.unos.get())
        poziv_forme_za_prikaz_izvestaja(self._korisnik,broj_dana)


def poziv_forme_za_izvestaj_lekara_sopstveni(root,korisnik):
    FormaIzvestajaLekara(root,korisnik)
    root.mainloop()
