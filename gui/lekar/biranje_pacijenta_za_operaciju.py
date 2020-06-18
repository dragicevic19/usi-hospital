from tkinter import ttk, messagebox
from tkinter import *

from gui.lekar.zakazivanje_opreacije import poziv_forme_zakazivanje_operacije
from gui.prikaz_entiteta.prikaz_pacijenata_po_lekaru import PrikazPacijenataPoLekaru

from repozitorijum.korisnik.korisnik_repozitorijum import lista_ucitanih_korisnika


class BiranjePacijentaZaOperaciju(PrikazPacijenataPoLekaru):

    def __init__(self, root, ulogovani_lekar):
        super().__init__(root, ulogovani_lekar)
        self._ulogovani_lekar = ulogovani_lekar
        potvrdi_dugme = ttk.Button(self._root, text="ZAKAZI OPERACIJU", command=self.double_click)
        potvrdi_dugme.pack(fill='x')

    def double_click(self):
        try:
            odabrani = self.treeview.focus()
            odabrani_korisnik = self.treeview.item(odabrani)['values']
            korisnicko_ime_odabranog = odabrani_korisnik[0]
            self._root.destroy()
            poziv_forme_zakazivanje_operacije(self._ulogovani_lekar, korisnicko_ime_odabranog)
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali korisnika!")


def poziv_forme_biranje_pacijenata_za_operaciju(root, ulogovani_lekar):
    app = BiranjePacijentaZaOperaciju(root, ulogovani_lekar)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    ulogovani_lekar = lista_ucitanih_korisnika[6]
    poziv_forme_biranje_pacijenata_za_operaciju(root, ulogovani_lekar)
