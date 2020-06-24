from tkinter import ttk, messagebox
from tkinter import *
from gui.prikaz_entiteta.prikaz_notifikacija import PrikazNotifikacija
from gui.sekretar.zakazivanje_pregleda import poziv_forme_za_zakazivanje_pregleda
from model.enum.tip_notifikacije import TipNotifikacije


class ZakazivanjePregledaBiranje(PrikazNotifikacija):

    def __init__(self, root):
        self._root = root
        super().__init__(self._root, TipNotifikacije.ZAHTEV_ZA_PREGLED)
        ttk.Button(self._root, text='ZAKAZI SELEKTOVAN PREGLED', command=self.zakazi_pregled).pack(fill='x')

    def zakazi_pregled(self):
        if not self._lista_selektovanih_notifikacija:
            messagebox.showerror('GRESKA', 'Niste selektovali notifikaciju!')
        elif len(self._lista_selektovanih_notifikacija) > 1:
            messagebox.showerror('GRESKA', 'Selektujte samo jednu notifikaciju!')
        else:
            self._root.destroy()
            poziv_forme_za_zakazivanje_pregleda(self._lista_selektovanih_notifikacija[0])


def zakazivanje_operacija_i_pregleda(root):
    app = ZakazivanjePregledaBiranje(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    zakazivanje_operacija_i_pregleda(root)
