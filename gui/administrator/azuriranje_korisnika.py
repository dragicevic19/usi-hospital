from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.prikaz_entiteta.prikaz_korisnika import PrikazKorisnika
from servis.korisnik.korisnik_servis import KorisnikServis


class IzborKorisnika(PrikazKorisnika):

    def __init__(self, root):
        super().__init__(root)
        potvrdi_dugme = ttk.Button(self._root, text="AZURIRAJ KORISNIKA", command=self.odabir_korisnika)
        potvrdi_dugme.pack(fill='x')

    def odabir_korisnika(self):
        try:
            odabrani = self.treeview.focus()
            odabrani_korisnik = self.treeview.item(odabrani)['values']
            korisnicko_ime_odabranog = odabrani_korisnik[0]
            self.pokretanje_forme_unos_podataka(korisnicko_ime_odabranog)
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali korisnika!")

    def pokretanje_forme_unos_podataka(self, selektovan_korisnik):
        root2 = Tk()
        root2.geometry('330x260')
        application = UnosPodataka(root2, selektovan_korisnik, self._root)
        root2.mainloop()


class UnosPodataka(IzborKorisnika):

    def __init__(self, root2, selektovan_korisnik, root):
        self._stari_root = root
        self._root2 = root2
        self._selektovano_korisnicko_ime = selektovan_korisnik
        self._korisnicko_ime = None
        self._lozinka = None
        self._ime = None
        self._prezime = None

        self._root2.title("Podaci o korisniku")
        self.pronadji_podrazumevane_vrednosti()
        self.unesi_novo_korisnicko_ime()
        self.unesi_novu_lozinku()
        self.unesi_novo_ime()
        self.unesi_novo_prezime()

        ttk.Button(self._root2, text="POTVRDI",
                   command=self.provera_unetih_podataka).grid(row=6, column=2, pady=10)

    def pronadji_podrazumevane_vrednosti(self):
        korisnik = KorisnikServis().pronadji_korisnika_po_korisnickom_imenu(self._selektovano_korisnicko_ime)
        self._podrazumevano_k_ime = korisnik.get_korisnicko_ime()
        self._podrazumevana_lozinka = korisnik.get_lozinka()
        self._podrazumevano_ime = korisnik.get_ime()
        self._podrazumevano_prezime = korisnik.get_prezime()

    def unesi_novo_korisnicko_ime(self):

        Label(self._root2, justify=LEFT, text="Korisnicko ime:", font="Times 15").grid(row=2, column=1, pady=10)
        self._korisnicko_ime = ttk.Entry(self._root2)
        self._korisnicko_ime.insert(0, self._podrazumevano_k_ime)
        self._korisnicko_ime.grid(row=2, column=2, columnspan=10)

    def unesi_novu_lozinku(self):

        Label(self._root2, justify=LEFT, text="Lozinka:", font="Times 15").grid(row=3, column=1, pady=10)
        self._lozinka = ttk.Entry(self._root2)
        self._lozinka.insert(0, self._podrazumevana_lozinka)
        self._lozinka.grid(row=3, column=2, columnspan=10)

    def unesi_novo_ime(self):

        Label(self._root2, justify=LEFT, text="Ime:", font="Times 15").grid(row=4, column=1, pady=10)
        self._ime = ttk.Entry(self._root2)
        self._ime.insert(0, self._podrazumevano_ime)
        self._ime.grid(row=4, column=2, columnspan=10)

    def unesi_novo_prezime(self):

        Label(self._root2, justify=LEFT, text="Prezime:", font="Times 15").grid(row=5, column=1, pady=10)
        self._prezime = ttk.Entry(self._root2)
        self._prezime.insert(0, self._podrazumevano_prezime)
        self._prezime.grid(row=5, column=2, columnspan=10)

    def provera_unetih_podataka(self):

        if not self._korisnicko_ime.get() or not self._lozinka.get() or not self._ime.get() or not self._prezime.get():
            messagebox.showerror("GRESKA", "Neispravan unos.")
            self._root2.destroy()

        elif KorisnikServis().pronadji_korisnika_po_korisnickom_imenu(self._korisnicko_ime.get()):
            if self._selektovano_korisnicko_ime != self._korisnicko_ime.get():
                messagebox.showerror("GRESKA", "Korisnik sa unetim korisnickim imenom vec postoji")
                self._root2.destroy()

            else:
                self.azuriraj_korisnika()
        else:
            self.azuriraj_korisnika()

    def azuriraj_korisnika(self):
        KorisnikServis().azuriraj_korisnika(self._selektovano_korisnicko_ime, self._korisnicko_ime.get(),
                                            self._lozinka.get(), self._ime.get(), self._prezime.get())
        messagebox.showinfo("USPESNO", "Uspesno ste azurirali korisnika")
        self._root2.destroy()
        self._stari_root.destroy()


def poziv_forme_azuriranje_korisnika(root):
    a = IzborKorisnika(root)
    root.mainloop()






if __name__ == '__main__':
    root = Tk()
    poziv_forme_azuriranje_korisnika(root)

