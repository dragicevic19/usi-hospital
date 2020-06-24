from tkinter import ttk, messagebox
from tkinter import *
from gui.lekar.zahtev_za_pregled_lop import poziv_forme_zahtev_za_pregled_lop
from gui.lekar.zakazivanje_opreacije_specijalista import poziv_forme_zakazivanje_operacije
from gui.prikaz_entiteta.prikaz_pacijenata_po_lekaru import PrikazPacijenata
from servis.korisnik.korisnik_servis import KorisnikServis


class BiranjePacijenta(PrikazPacijenata):

    def __init__(self, root, ulogovani_lekar=None):
        super().__init__(root, ulogovani_lekar)
        self._ulogovani_lekar = ulogovani_lekar

        potvrdi_dugme = ttk.Button(self._root, text="ZAKAZI", command=self.zakazivanje)
        potvrdi_dugme.pack(fill='x')

    def zakazivanje(self):
        if self._ulogovani_lekar:
            self.otvori_formu_za_zakazivanje_specijalista()
        else:
            self.otvori_formu_za_zakazivanje_lop()

    def otvori_formu_za_zakazivanje_specijalista(self):
        try:
            odabrani = self.treeview.focus()
            odabrani_korisnik = self.treeview.item(odabrani)['values']
            korisnicko_ime_odabranog = odabrani_korisnik[0]
            self._root.destroy()
            poziv_forme_zakazivanje_operacije(self._ulogovani_lekar, korisnicko_ime_odabranog)
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali korisnika!")

    def otvori_formu_za_zakazivanje_lop(self):
        try:
            odabrani = self.treeview.focus()
            odabrani_korisnik = self.treeview.item(odabrani)['values']
            korisnicko_ime_odabranog = odabrani_korisnik[0]
            self._root.destroy()
            poziv_forme_zahtev_za_pregled_lop(korisnicko_ime_odabranog)
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali korisnika!")


def poziv_forme_biranje_pacijenata_za_operaciju(root, ulogovani_lekar=None):
    app = BiranjePacijenta(root, ulogovani_lekar)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    lekar = KorisnikServis().dobavi_sve_korisnike_u_sistemu()[5]
    poziv_forme_biranje_pacijenata_za_operaciju(root, lekar)
