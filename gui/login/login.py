from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.lekar.lekar import poziv_forme_lekar
from gui.sekretar.sektretar import poziv_forme_sekretar
from gui.pacijent.pacijent import poziv_forme_pacijent
from gui.administrator.administrator import poziv_forme_administrator
from gui.upravnik.upravnik import poziv_forme_upravnik
from gui.neregistrovan import poziv_forme_neregistrovan
from repository.korisnik.korisnik_repozitorijum import lista_ucitanih_korisnika as lista_korisnika
from services.forme.login import LoginService


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
        if self._obelezeno.get() == True:
            poziv_forme_neregistrovan()
        else:

            korisnik = LoginService.provera_unosa(self._korisnicko_ime.get(),self._lozinka.get())
            if (korisnik != None):
                self.__poziv_forme_za(korisnik)
            else:
                messagebox.showerror("GRESKA", "Neispravan unos.")


    def __poziv_forme_za(self, korisnik):
        # self._korisnicko_ime.delete(0,"end")
        # self._lozinka.delete(0, "end")
        self._root.destroy()

        uloga = korisnik.get_uloga()
        recnik_funkcija = {'UPRAVNIK': poziv_forme_upravnik, 'SEKRETAR': poziv_forme_sekretar,
                           'LEKAR': poziv_forme_lekar, 'ADMINISTRATOR': poziv_forme_administrator,
                           'PACIJENT': poziv_forme_pacijent}
        recnik_funkcija[uloga](korisnik)



def kreni_login():
    root = Tk()
    root.geometry('370x150')
    application = LogIn(root)
    root.mainloop()


if __name__ == '__main__':
    kreni_login()
