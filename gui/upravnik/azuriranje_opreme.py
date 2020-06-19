from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.prikaz_entiteta.prikaz_opreme import PrikazOpreme
from servis.oprema.oprema_servis import OpremaServis


class IzborOpreme(PrikazOpreme):

    def __init__(self, root):
        super().__init__(root)
        potvrdi_dugme = ttk.Button(self._root, text="AZURIRAJ OPREMU", command=self.odaberi_opremu)
        potvrdi_dugme.pack(fill='x')

    def odaberi_opremu(self):
        try:
            odabrana = self.treeview.focus()
            odabrana_oprema = self.treeview.item(odabrana)['values']
            naziv_opreme_odabrane = odabrana_oprema[0]
            self.pokretanje_unosa_podataka(naziv_opreme_odabrane)
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali opremu!")

    def pokretanje_unosa_podataka(self, selektovana_oprema):
        root2 = Tk()
        root2.geometry('330x260')
        application = UnosPodataka(root2, selektovana_oprema, self._root)
        root2.mainloop()


class UnosPodataka(IzborOpreme):

    def __init__(self, root2, selektovana_oprema, root):
        self._stari_root = root
        self._root2 = root2
        self._selektovan_naziv_opreme = selektovana_oprema
        self._naziv_opreme = None
        self._opis = None
        self._kolicina = None

        self._root2.title("Podaci o opremi")
        self.pronadji_podrazumevane_vrednosti()
        self.unesi_novi_naziv()
        self.unesi_novi_opis()
        self.unesi_novu_kolicinu()

        ttk.Button(self._root2, text="POTVRDI",
                   command=self.provera_unetih_podataka).grid(row=6, column=2, pady=10)

    def pronadji_podrazumevane_vrednosti(self):
        oprema = OpremaServis().pronadji_opremu_po_nazivu(self._selektovan_naziv_opreme)
        self._podrazumevan_naziv = oprema.get_naziv_opreme()
        self._podrazumevani_opis = oprema.get_opis()
        self._podrazumevana_kolicina = oprema.get_slobodna_oprema()

    def unesi_novi_naziv(self):

        Label(self._root2, justify=LEFT, text="Naziv opreme:", font="Times 15").grid(row=2, column=1, pady=10)
        self._naziv_opreme = ttk.Entry(self._root2)
        self._naziv_opreme.insert(0, self._podrazumevan_naziv)
        self._naziv_opreme.grid(row=2, column=2, columnspan=10)

    def unesi_novi_opis(self):

        Label(self._root2, justify=LEFT, text="Opis:", font="Times 15").grid(row=3, column=1, pady=10)
        self._opis = ttk.Entry(self._root2)
        self._opis.insert(0, self._podrazumevani_opis)
        self._opis.grid(row=3, column=2, columnspan=10)

    def unesi_novu_kolicinu(self):

        Label(self._root2, justify=LEFT, text="Kolicina:", font="Times 15").grid(row=4, column=1, pady=10)
        self._kolicina = ttk.Entry(self._root2)
        self._kolicina.insert(0, self._podrazumevana_kolicina)
        self._kolicina.grid(row=4, column=2, columnspan=10)

    def provera_unetih_podataka(self):

        if not self._naziv_opreme.get() or not self._opis.get() or not self._kolicina.get():
            messagebox.showerror("GRESKA", "Neispravan unos.")
            self._root2.destroy()

        elif not str(self._kolicina.get()).isnumeric() or int(self._kolicina.get()) < 0:
            messagebox.showerror("GRESKA", "Neispravan unos za kolicinu. Dozvoljeni su samo pozitivni celi brojevi!")
            self._root2.destroy()

        elif OpremaServis().pronadji_opremu_po_nazivu(self._naziv_opreme.get()):
            if self._selektovan_naziv_opreme != self._naziv_opreme.get():
                messagebox.showerror("GRESKA", "Oprema sa unetim nazivom opreme vec postoji")
                self._root2.destroy()

            else:
                self.azuriraj_opremu()
        else:
            self.azuriraj_opremu()

    def azuriraj_opremu(self):
        OpremaServis().azuriraj_opremu(self._selektovan_naziv_opreme, self._naziv_opreme.get(),
                                     self._opis.get(), self._kolicina.get())
        messagebox.showinfo("USPESNO", "Uspesno ste azurirali opremu")
        self._root2.destroy()
        self._stari_root.destroy()


def poziv_forme_azuriranje_opreme(root):
    application = IzborOpreme(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_forme_azuriranje_opreme(root)

