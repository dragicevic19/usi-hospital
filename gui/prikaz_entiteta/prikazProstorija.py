from tkinter import ttk
from tkinter import messagebox
from repository.prostorije.prostorije_repozitorijum import ProstorijeRepository, lista_ucitanih_prostorija
from tkinter import Tk


class PrikazProstorija(object):

    def __init__(self, root,lista = lista_ucitanih_prostorija):
        self._root = root
        self._lista = lista
        self.treeview = ttk.Treeview(self._root)
        self.scroll = ttk.Scrollbar(self._root, orient='vertical', command=self.treeview.yview)
        self.scroll.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scroll.set)
        self.napravi_treeview()

    def napravi_treeview(self):
        self.treeview["columns"] = ["sprat", "br_prostorije", "spisak_opreme", "namena_prostorije"]
        self.treeview["show"] = "headings"
        self.treeview.heading("sprat", text="Sprat")
        self.treeview.column('sprat', width=50)
        self.treeview.heading("br_prostorije", text="Broj prostorije")
        self.treeview.column('br_prostorije', width=100)
        self.treeview.heading("spisak_opreme", text="Spisak opreme : kolicina")
        self.treeview.column('spisak_opreme', width=250)
        self.treeview.heading("namena_prostorije", text="Namena prostorije")
        self.treeview.column('namena_prostorije', width=120)
        self.treeview.pack()
        self.treeview.config(height=13)
        self.__popuni_treeview()

    def __popuni_treeview(self):
        index = iid = 0
        for prostorija in self._lista:
            if not prostorija.get_obrisana():
                if prostorija.get_spisak_opreme():
                    spisak_opreme = str(prostorija.get_spisak_opreme()[0])
                else:
                    spisak_opreme = ''
                k = (prostorija.get_sprat(), prostorija.get_broj_prostorije(),
                     spisak_opreme + ' Dvoklik za vise...', prostorija.get_namena_prostorije())

                self.treeview.insert("", index, iid, values=k)
                index = iid = index + 1
        self.treeview.bind('<Double-1>', self.__prikazi_spisak_opreme)

    def __prikazi_spisak_opreme(self, event):
        try:
            prostorija = self.selektovana_prostorija()
            messagebox.showinfo('Prikaz opreme', str(prostorija.get_spisak_opreme()))
        except IndexError:
            pass

    def selektovana_prostorija(self):
        odabrana = self.treeview.focus()
        odabrana_prostorija = self.treeview.item(odabrana)['values']
        sprat_odabrane, br_prostorije_odabrane = str(odabrana_prostorija[0]), str(odabrana_prostorija[1])
        prostorija = ProstorijeRepository.vrati_prostoriju_po_broju_i_spratu(sprat_odabrane, br_prostorije_odabrane)
        return prostorija

    def selektuj_vise_prostorija(self):
        odabrane = self.treeview.selection()
        if len(odabrane) == 2:
            odabrana_prostorija1 = self.treeview.item(odabrane[0])['values']
            odabrana_prostorija2 = self.treeview.item(odabrane[1])['values']
            prva_prostorija = ProstorijeRepository.vrati_prostoriju_po_broju_i_spratu(str(odabrana_prostorija1[0]),
                                                                                      str(odabrana_prostorija1[1]))
            druga_prostorija = ProstorijeRepository.vrati_prostoriju_po_broju_i_spratu(str(odabrana_prostorija2[0]),
                                                                                       str(odabrana_prostorija2[1]))
            return prva_prostorija, druga_prostorija

        return False


if __name__ == '__main__':
    root = Tk()
    ProstorijeRepository.ucitavanje_prostorije()
    print(lista_ucitanih_prostorija)
    PrikazProstorija(root)
    root.mainloop()
