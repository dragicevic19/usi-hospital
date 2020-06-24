from model.konstante.konstante import INDEX_LEKARA_TREEVIEW_PRIKAZ_PREGLEDA
from servis.kalendar.kalendar_servis import KalendarServis
from servis.korisnik.korisnik_servis import KorisnikServis
from tkinter import ttk, Tk, messagebox


class PrikazPregleda:

    def __init__(self, root, ulogovan_pacijent):
        self._root = root
        self._ulogovan_pacijent = ulogovan_pacijent
        self.treeview = ttk.Treeview(self._root)
        self.scroll = ttk.Scrollbar(self._root, orient='vertical', command=self.treeview.yview)
        self.scroll.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scroll.set)
        self.napravi_treeview()
        self.postava_dugmica()

    def postava_dugmica(self):
        prikaz_prosli = ttk.Button(self._root, text="PRIKAZI PROSLE PREGLEDE",
                                   command=lambda: self.__popuni_treeview(True))
        prikaz_prosli.pack(fill='x')
        prikaz_buduci = ttk.Button(self._root, text="PRIKAZI BUDUCE PREGLEDE",
                                   command=lambda: self.__popuni_treeview(False))
        prikaz_buduci.pack(fill='x')

    def napravi_treeview(self):
        self.treeview["columns"] = ["datum", "vreme", "zahvat", "spisak_doktora"]
        self.treeview["show"] = "headings"
        self.treeview.heading("datum", text="Datum")
        self.treeview.heading("vreme", text="Vreme")
        self.treeview.heading("zahvat", text="Zahvat")
        self.treeview.heading("spisak_doktora", text="Spisak doktora")
        self.treeview.pack()
        self.treeview.config(height=13)

    def __popuni_treeview(self, prosli):
        self.treeview.delete(*self.treeview.get_children())
        index = 0
        if prosli:
            lista = KalendarServis().dobavi_listu_proslih_dogadjaja()
        else:
            lista = KalendarServis().dobavi_listu_dogadjaja()
        for dogadjaj in lista:
            if self._ulogovan_pacijent == dogadjaj.pacijent:
                red = (str(dogadjaj.datum), str(dogadjaj.vreme_pocetka_str), dogadjaj.zahvat, ",".join(dogadjaj.spisak_doktora))
                self.treeview.insert("", index, index, values=red)
                index = index + 1
        self.treeview.bind('<Double-1>', self.__prikazi_detalje_lekara)

    def __prikazi_detalje_lekara(self, event):
        odabrana = self.treeview.focus()
        odabrani_doktor = self.treeview.item(odabrana)["values"]
        ispis = KorisnikServis().vrati_imena_lekara(odabrani_doktor[INDEX_LEKARA_TREEVIEW_PRIKAZ_PREGLEDA])
        messagebox.showinfo("Imena lekara:", ispis)


def poziv_prikaza_pregleda(root, ulogovani_pacijent):  # korisnicko ime ulogovanog
    kor_ime = ulogovani_pacijent.get_korisnicko_ime()
    PrikazPregleda(root, kor_ime)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_prikaza_pregleda(root, "predrag")
