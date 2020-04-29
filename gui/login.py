from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.lekar import poziv_forme_lekar
from gui.sektretar import poziv_forme_sekretar
from gui.pacijent import poziv_forme_pacijent
from gui.administrator import poziv_forme_administrator
from gui.upravnik import poziv_forme_upravnik
from gui.neregistrovan import poziv_forme_neregistrovan
from model.kreiranje_objekata_entiteta import lista_ucitanih_korisnika as lista_korisnika


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
            i = self.__provera_unosa()
            if (i != None):
                self.__poziv_forme_za(i)
            else:
                messagebox.showerror("GRESKA", "Neispravan unos.")

    def __provera_unosa(self):
        for i in lista_korisnika:
            if (i.get_korisnicko_ime() == self._korisnicko_ime.get() and i.get_lozinka() == self._lozinka.get()):
                return i.get_uloga()
        return None

    def __poziv_forme_za(self, uloga):
        if (uloga == "upravnik"):
            poziv_forme_upravnik()
        elif (uloga == "sekretar"):
            poziv_forme_sekretar()
        elif (uloga == "pacijent"):
            poziv_forme_pacijent()
        elif (uloga == "lekar"):
            poziv_forme_lekar()
        elif (uloga == "administrator"):
            poziv_forme_administrator()


def kreni_login():
    root = Tk()
    root.geometry('370x130')
    application = LogIn(root)
    root.mainloop()


if __name__ == '__main__':
    kreni_login()
