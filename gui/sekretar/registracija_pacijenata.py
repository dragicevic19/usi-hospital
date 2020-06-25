from model.dto.registracija_pacijenta_dto import RegistracijaPacijentaDTO
from model.konstante.konstante import DUZINA_BR_KNJIZICE
from servis.korisnik.korisnik_servis import KorisnikServis
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class RegistracijaPacijenta:
    pol = ('muski', 'zenski')

    def __init__(self, root):
        self._root = root
        self._pol = StringVar(self._root)
        self._pol.set(self.pol[0])
        self._korisnicko_ime = None
        self._lozinka = None
        self._ime = None
        self._prezime = None
        self._br_zdravstvene = None

        self.izaberi_pol()
        self.unesi_korisnicko_ime()
        self.unesi_lozinku()
        self.unesi_ime()
        self.unesi_prezime()
        self.unesi_broj_zdravstvene_knjizice()

        ttk.Button(self._root, text="POTVRDI", command=self.registruj_pacijenta).grid(row=7, column=2)

    def izaberi_pol(self):
        Label(self._root, text="Pol:", font="Times 14").grid(row=1, column=1, pady=10)
        podrazumevana_vrednost = 'muski'
        ttk.OptionMenu(self._root, self._pol, podrazumevana_vrednost, *self.pol).grid(row=1, column=2)

    def unesi_korisnicko_ime(self):
        Label(self._root, justify=LEFT, text="Korisnicko ime:", font="Times 15").grid(row=2, column=1, pady=10)
        self._korisnicko_ime = ttk.Entry(self._root)
        self._korisnicko_ime.grid(row=2, column=2, columnspan=10)

    def unesi_lozinku(self):
        Label(self._root, justify=LEFT, text="Lozinka:", font="Times 15").grid(row=3, column=1, pady=10)
        self._lozinka = ttk.Entry(self._root, show='*')
        self._lozinka.grid(row=3, column=2, columnspan=10)

    def unesi_ime(self):
        Label(self._root, justify=LEFT, text="Ime:", font="Times 15").grid(row=4, column=1, pady=10)
        self._ime = ttk.Entry(self._root)
        self._ime.grid(row=4, column=2, columnspan=10)

    def unesi_prezime(self):
        Label(self._root, justify=LEFT, text="Prezime:", font="Times 15").grid(row=5, column=1, pady=10)
        self._prezime = ttk.Entry(self._root)
        self._prezime.grid(row=5, column=2, columnspan=10)

    def unesi_broj_zdravstvene_knjizice(self):
        Label(self._root, justify=LEFT, text="Broj knjizice:", font="Times 15").grid(row=6, column=1, pady=10)
        self._br_zdravstvene = ttk.Entry(self._root)
        self._br_zdravstvene.grid(row=6, column=2, columnspan=10)

    def registruj_pacijenta(self):
        if not self._korisnicko_ime.get() or not self._lozinka.get() or not self._ime.get() or not self._prezime.get() \
                or not self._br_zdravstvene.get():
            messagebox.showerror("GRESKA", "Neispravan unos.")
        elif len(self._br_zdravstvene.get()) != DUZINA_BR_KNJIZICE or not str(self._br_zdravstvene.get()).isnumeric():
            messagebox.showerror("GRESKA!", "Pogresan unos broja zdravstvene knjizice (8 brojeva)!")
        else:
            self.registruj()

    def registruj(self):
        if not KorisnikServis().pronadji_korisnika_po_korisnickom_imenu(self._korisnicko_ime.get()):
            pacijent = RegistracijaPacijentaDTO(self._korisnicko_ime.get(), self._lozinka.get(), self._ime.get(),
                                                self._prezime.get(), self._br_zdravstvene.get(),
                                                self._pol.get())
            KorisnikServis().registracija_pacijenta(pacijent)
            messagebox.showinfo("USPESNO", "Uspesno ste registrovali pacijenta")
            self._root.destroy()
        else:
            messagebox.showerror("GRESKA", "Korisnik sa unetim korisnickim imenom vec postoji")


def poziv_forme_unos_korisnika(root):
    RegistracijaPacijenta(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('425x425')
    poziv_forme_unos_korisnika(root)
