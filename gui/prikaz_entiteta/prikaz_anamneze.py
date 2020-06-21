from servis.unos_anamneze.unos_anamneze_servis import UnosAnamnezeServis
from tkinter import ttk


class PrikazAnamneze:

    def __init__(self, root, ulogovan_korisnik):
        self._root = root
        self._ulogovan_korisnik = ulogovan_korisnik
        self.treeview = ttk.Treeview(self._root)
        self.scroll = ttk.Scrollbar(self._root, orient='vertical', command=self.treeview.yview)
        self.scroll.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scroll.set)
        self.napravi_treeview()

    def napravi_treeview(self):
        self.treeview["columns"] = ["ime_lekara", "opis_anamneze", "datum_i_vreme"]
        self.treeview["show"] = "headings"
        self.treeview.heading("ime_lekara", text="Ime lekara")
        self.treeview.heading("opis_anamneze", text="Opis anamneze")
        self.treeview.heading("datum_i_vreme", text="Datum i vreme")
        self.treeview.pack()
        self.treeview.config(height=13)
        self.__popuni_treeview()

    def __popuni_treeview(self):
        index = iid = 0

        lista_anamneza_po_pacijentu = UnosAnamnezeServis().dobavi_anamnezu_ulogovanog_pacijenta(self._ulogovan_korisnik)
        for unos_anamneze in lista_anamneza_po_pacijentu:
            u = (unos_anamneze.get_lekar(), unos_anamneze.get_opis(),
                 unos_anamneze.get_datum_i_vreme())
            self.treeview.insert("", index, iid, values=u)
            index = iid = index + 1
