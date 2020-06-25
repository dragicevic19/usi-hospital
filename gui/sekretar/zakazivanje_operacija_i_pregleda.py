from tkinter import ttk, messagebox
from tkinter import *
from gui.prikaz_entiteta.prikaz_notifikacija import PrikazNotifikacija
from gui.sekretar.zakazivanje_pregleda import poziv_forme_za_zakazivanje_pregleda
from model.enum.tip_notifikacije import TipNotifikacije


class ZakazivanjePregledaBiranje(PrikazNotifikacija):

    def __init__(self, root,kalendar_servis,korisnik_servis):
        self._root = root
        self._kalendar_servis = kalendar_servis
        self._korisnik_servis = korisnik_servis
        super().__init__(self._root, TipNotifikacije.ZAHTEV_ZA_PREGLED,self._kalendar_servis)
        ttk.Button(self._root, text='ZAKAZI SELEKTOVAN PREGLED', command=self.zakazi_pregled).pack(fill='x')

    def zakazi_pregled(self):
        if not self._lista_selektovanih_notifikacija:
            messagebox.showerror('GRESKA', 'Niste selektovali notifikaciju!')
        elif len(self._lista_selektovanih_notifikacija) > 1:
            messagebox.showerror('GRESKA', 'Selektujte samo jednu notifikaciju!')
        else:
            self._root.destroy()
            poziv_forme_za_zakazivanje_pregleda(self._lista_selektovanih_notifikacija[0],self._kalendar_servis,self._korisnik_servis)


def zakazivanje_operacija_i_pregleda(root,kalendar_servis,korisnik_servis):
    ZakazivanjePregledaBiranje(root,kalendar_servis,korisnik_servis)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    zakazivanje_operacija_i_pregleda(root)
