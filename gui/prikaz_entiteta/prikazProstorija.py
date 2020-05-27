from tkinter import ttk
from tkinter import messagebox
from model.kreiranje_objekata_entiteta import KreiranjeObjekata
from repository.prostorije.prostorije_repository import ProstorijeRepository, lista_ucitanih_prostorija


class PrikazProstorija(object):

    def __init__(self, root):
        self._root = root
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
        for prostorija in lista_ucitanih_prostorija:
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
        prostorija = ProstorijeRepository.postoji_prostorija(sprat_odabrane, br_prostorije_odabrane)
        return prostorija

