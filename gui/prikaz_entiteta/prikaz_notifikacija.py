import tkinter as tk
from tkinter import ttk, messagebox

from gui.prikaz_entiteta.cb_treeview import CbTreeview
from model.dto.dogadjaji_dto.notifikacija_dto import NotifikacijaDTO
from model.enum.tip_notifikacije import TipNotifikacije
from servis.kalendar.kalendar_servis import KalendarServis


class PrikazNotifikacija(object):

    def __init__(self, root, tip_notifikacija):
        self._root = root

        self._tip_notifikacija = tip_notifikacija
        self._lista_notifikacija = KalendarServis().prikupi_notifikacije_po_tipu(tip_notifikacija)
        self.treeview = CbTreeview(self._root, columns=(
            'datum_od', 'datum_do', 'vreme_od', 'vreme_do', 'prostorija', 'lekar', 'pacijent',
            'zavrseno'), selectmode="extended")
        self._lista_selektovanih_notifikacija = []
        self.scroll = ttk.Scrollbar(self._root, orient='vertical', command=self.treeview.yview)
        self.scroll.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scroll.set)
        self.napravi_treeview()

    def napravi_treeview(self):
        self.treeview.heading("datum_od", text="Od")
        self.treeview.column('#1', width=100)
        self.treeview.heading("datum_do", text="Do")
        self.treeview.column('#2', width=100)
        self.treeview.heading("vreme_od", text="Vreme od")
        self.treeview.column('#3', width=100)
        self.treeview.heading("vreme_do", text="Vreme do")
        self.treeview.column('#4', width=100)
        self.treeview.heading("prostorija", text="Prostorija")
        self.treeview.column('#5', width=170)
        self.treeview.heading("lekar", text="Lekar")
        self.treeview.column('#6', width=120)
        self.treeview.heading("pacijent", text="Pacijent")
        self.treeview.column('#7', width=150)
        self.treeview.heading("zavrseno", text="Zavrseno")
        self.treeview.column('#8', width=120)
        self.treeview.pack(fill='both')
        self.treeview.config(height=13)
        self.__popuni_treeview()

    def __popuni_treeview(self):
        for notifikacija in self._lista_notifikacija:
            n = notifikacija.vrati_za_tabelu_notifikacija()
            self.treeview.insert('', 'end', values=n)
        self.treeview.bind('<Double-1>', self._da_li_je_otkaceno)

    def _da_li_je_otkaceno(self, event):
        try:
            red = self.treeview.focus()
            notifikacija = self.treeview.item(red)['values']
            notifikacijaDTO = NotifikacijaDTO(notifikacija[0], notifikacija[1], notifikacija[2], notifikacija[3],
                                              notifikacija[4], notifikacija[5], notifikacija[6])
            if notifikacija in self._lista_selektovanih_notifikacija:
                self._lista_selektovanih_notifikacija.remove(notifikacijaDTO)
            else:
                self._lista_selektovanih_notifikacija.append(notifikacijaDTO)
        except IndexError:
            pass  # kada se stisne na belu povrsinu treeview-a baci error


if __name__ == '__main__':
    root = tk.Tk()
    PrikazNotifikacija(root, TipNotifikacije.RENOVIRANJE)
    root.mainloop()
