from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.prikaz_entiteta.prikaz_zauzeca import PrikazZauzeca
from model.konstante.konstante import INDEX_PACIJENTA_DOGADJAJ_TREEVIEW
from repository.korisnik.korisnik_repozitorijum import KorisnikRepository


class PregledZauzeca(PrikazZauzeca):

    def __init__(self, root, korisnicko_ime_lekara):
        super().__init__(root, korisnicko_ime_lekara)
        detalji_dugme = ttk.Button(self._root, text="DETALJNIJE", command=self.detalji_click)
        detalji_dugme.pack(fill='x')

    def detalji_click(self):
        try:
            odabrani = self.treeview.focus()
            odabrani_dogajaj = self.treeview.item(odabrani)['values']
            pacijent_iz_dogadjaja = odabrani_dogajaj[INDEX_PACIJENTA_DOGADJAJ_TREEVIEW]
            self._pacijent = KorisnikRepository.nadji_po_korisnickom_imenu(pacijent_iz_dogadjaja)
            self.pokretanje_prikaza_podataka()
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali dogadjaj!")

    def pokretanje_prikaza_podataka(self):
        root2 = Tk()
        root2.geometry('330x260')
        application = PrikazPodataka(root2, self._pacijent, self._root)
        root2.mainloop()


class PrikazPodataka(PregledZauzeca):

    def __init__(self, root2, selektovan_pacijent, root):
        self._stari_root = root
        self._root2 = root2
        self._pacijent = selektovan_pacijent
        self._ime = None
        self._prezime = None
        self._pol = None
        self._broj_zdravstvene = None

        self._root2.title("Podaci o pacijentu")
        self.prikazi_detaljne_podatke()

    def prikazi_detaljne_podatke(self):
        Label(self._root2, justify=LEFT, text="Ime:", font="Times 15").grid(row=2, column=1, pady=10)
        Label(self._root2, justify=LEFT, text=self._pacijent._ime, font="Times 15").grid(row=2, column=2, pady=10, padx=20)
        Label(self._root2, justify=LEFT, text="Prezime:", font="Times 15").grid(row=3, column=1, pady=10)
        Label(self._root2, justify=LEFT, text=self._pacijent._prezime, font="Times 15").grid(row=3, column=2, pady=10, padx=20)
        Label(self._root2, justify=LEFT, text="Pol:", font="Times 15").grid(row=4, column=1, pady=10)
        Label(self._root2, justify=LEFT, text=self._pacijent._pol, font="Times 15").grid(row=4, column=2, pady=10, padx=20)
        Label(self._root2, justify=LEFT, text="Broj zdravstvene:", font="Times 15").grid(row=5, column=1, pady=10)
        Label(self._root2, justify=LEFT, text=self._pacijent._br_zdravstvene, font="Times 15").grid(row=5, column=2, pady=10, padx=20)


def poziv_forme_detaljni_prikaz_pacijenta(root):
    a = PregledZauzeca(root, "horacije442")
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_forme_detaljni_prikaz_pacijenta(root)
