from model.enum.uloga import Uloga
from model.korisnik import Korisnik
from model.lekar import Lekar
from model.sekretar import Sekretar
from model.upravnik import Upravnik
from services.userService import UserService
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from repository.korisnik.korisnikRepo1 import KorisnikRepository


class NoviKorisnik:
    uloge = ('LEKAR', 'UPRAVNIK', 'SEKRETAR')
    recnik = {'UPRAVNIK': Uloga.UPRAVNIK.value, 'SEKRETAR': Uloga.SEKRETAR.value, 'LEKAR': Uloga.LEKAR.value}
    recKonstruktora = {'UPRAVNIK': Upravnik, 'SEKRETAR': Sekretar, 'LEKAR': Lekar}

    def __init__(self, root):
        self._root = root
        self._uloga = StringVar(self._root)
        self._uloga.set(self.uloge[0])
        self._korisnicko_ime = None
        self._lozinka = None
        self._ime = None
        self._prezime = None

        self.izaberi_ulogu()
        self.unesi_korisnicko_ime()
        self.unesi_lozinku()
        self.unesi_ime()
        self.unesi_prezime()

        ttk.Button(self._root, text="POTVRDI", command=self.sacuvaj_korisnika).grid(row=6, column=2)

    def izaberi_ulogu(self):
        Label(self._root, text="Uloga:", font="Times 14").grid(row=1, column=1, pady=10)
        default = 'LEKAR'
        ttk.OptionMenu(self._root, self._uloga, default, *self.uloge).grid(row=1, column=2)

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

    def sacuvaj_korisnika(self):
        if not self._korisnicko_ime.get() or not self._lozinka.get() or not self._ime.get() or not self._prezime.get():
            messagebox.showerror("GRESKA", "Neispravan unos.")

        elif KorisnikRepository.nadji_po_korisnickom_imenu(self._korisnicko_ime.get()):  # serivs
            messagebox.showerror("GRESKA", "Korisnik sa unetim korisnickim imenom vec postoji")

        else:
            uloga = self._uloga.get()
            korisnik = self.recKonstruktora[uloga](self._korisnicko_ime.get(), self._lozinka.get(), self.recnik[uloga],
                                                   self._ime.get(), self._prezime.get())

            #
            # if self._uloga.get() == 'LEKAR':
            #     korisnik = Lekar(self._korisnicko_ime.get(), self._lozinka.get(), self.recnik[uloga], self._ime.get(),
            #                      self._prezime.get())
            #
            # else:
            #     korisnik = Korisnik(self._korisnicko_ime.get(), self._lozinka.get(), self._ime.get(),
            #                         self._prezime.get(), '', self.recnik[uloga])

            UserService.dodaj_korisnika(korisnik)

            messagebox.showinfo("USPESNO", "Uspesno ste dodali korisnika")
            self._root.destroy()


def poziv_forme_unos_korisnika(root):
    application = NoviKorisnik(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('425x425')
    poziv_forme_unos_korisnika(root)
