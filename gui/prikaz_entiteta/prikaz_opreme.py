from tkinter import ttk
from servis.oprema.oprema_servis import OpremaServis


class PrikazOpreme:

    def __init__(self, root):
        self._root = root

        self.treeview = ttk.Treeview(self._root)
        self.scroll = ttk.Scrollbar(self._root, orient='vertical', command=self.treeview.yview)
        self.scroll.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scroll.set)

        self.napravi_treeview()

    def napravi_treeview(self):
        self.treeview["columns"] = ["naziv opreme", "ukupan broj opreme", "slobodna oprema", "opis"]
        self.treeview["show"] = "headings"
        self.treeview.heading("naziv opreme", text="Naziv opreme")
        self.treeview.heading("ukupan broj opreme", text="Ukupan broj opreme")
        self.treeview.heading("slobodna oprema", text="Slobodna oprema")
        self.treeview.heading("opis", text="Opis")
        self.treeview.pack()
        self.treeview.config(height=13)
        self.__popuni_treeview()

    def __popuni_treeview(self):
        index = iid = 0
        lista_ucitane_bolnicke_opreme = OpremaServis().vrati_svu_opremu_u_sistemu()
        for oprema in lista_ucitane_bolnicke_opreme:
            o = (oprema.get_naziv_opreme(), oprema.get_ukupan_broj_opreme(), oprema.get_slobodna_oprema(),
                 oprema.get_opis())
            self.treeview.insert("", index, iid, values=o)
            index = iid = index + 1

