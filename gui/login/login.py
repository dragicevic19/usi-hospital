from tkinter import *  # UBACITI TRY CATCH ZA NESTANDARDNE BIBLIOTEKE!!!!!!!!!!!
from tkinter import ttk
from tkinter import messagebox
from gui.administrator.administrator import poziv_forme_administrator
from gui.upravnik.upravnik import poziv_forme_upravnik
from gui.neregistrovan import poziv_forme_neregistrovan
from model.enum.uloga import Uloga
from servis.forme.login import LoginServis
from gui.sekretar.sektretar import poziv_forme_sekretar
from gui.pacijent.pacijent import poziv_forme_pacijent


class LogIn:

    def __init__(self, root):
        self._root = root
        self._root.title("PRIJAVA KORISNIKA")
        self.__postava_oko_korisnickog_imena()
        self.__postava_oko_lozinke()
        self.__postavka_check_dugmeta()
        self.__postava_oko_dugmeta()

    def __postava_oko_korisnickog_imena(self):
        Label(self._root, text="Korisnicko ime:", font="Times 15").grid(row=1, column=1, pady=10)
        self._korisnicko_ime = ttk.Entry()
        self._korisnicko_ime.grid(row=1, column=2, columnspan=10)

    def __postava_oko_lozinke(self):
        Label(self._root, text="Lozinka:", font="Times 15").grid(row=2, column=1, pady=10)
        self._lozinka = ttk.Entry(show="*")
        self._lozinka.grid(row=2, column=2, columnspan=10)

    def __postavka_check_dugmeta(self):
        self._obelezeno = BooleanVar()
        self._neregistrovan = ttk.Checkbutton(self._root, text="zelite biti neregistrovani", variable=self._obelezeno,
                                              offvalue=False, onvalue=True)
        self._neregistrovan.grid(row=3, column=1)

    def __postava_oko_dugmeta(self):
        ttk.Button(self._root, text="PRIJAVA", command=self.__prijava).grid(row=3, column=2)

    def __prijava(self):
        if self._obelezeno.get():
            poziv_forme_neregistrovan()
        else:

            korisnik = LoginServis().provera_unosa(self._korisnicko_ime.get(), self._lozinka.get())
            if korisnik is not None:
                self.__poziv_forme_za(korisnik)
            else:
                messagebox.showerror("GRESKA", "Neispravan unos.")

    def __poziv_forme_za(self, korisnik):
        from gui.lekar.lekar import poziv_forme_lekar
        self._root.destroy()
        uloga = korisnik.get_uloga()
        recnik_funkcija = {Uloga.UPRAVNIK.name: poziv_forme_upravnik, Uloga.SEKRETAR.name: poziv_forme_sekretar,
                           Uloga.LEKAR.name: poziv_forme_lekar, Uloga.ADMINISTRATOR.name: poziv_forme_administrator,
                           Uloga.PACIJENT.name: poziv_forme_pacijent}
        recnik_funkcija[uloga](korisnik)


def kreni_login():
    root = Tk()
    root.geometry('370x150')
    LogIn(root)
    root.mainloop()


if __name__ == '__main__':
    kreni_login()
