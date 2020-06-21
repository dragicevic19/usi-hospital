from servis.prostorije.prostorije_servis import ProstorijeServis
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model.prostorija import Prostorija


class NovaProstorija:
    moguce_namene_prostorija = ('operaciona sala', 'sala za preglede', 'soba za lezanje')
    spratovi = ('1', '2', '3', '4')

    def __init__(self, root):
        self._root = root
        self._sprat = StringVar(self._root)
        self._broj_prostorije = None
        self._namena_prostorije = StringVar(self._root)

        self.izaberi_sprat()
        self.izaberi_prostoriju()
        self.izaberi_namenu_prostorije()
        ttk.Button(self._root, text="POTVRDI", command=self.proveri_validnost).grid(row=4, column=2)

    def izaberi_sprat(self):
        Label(self._root, text="Sprat:", font="Times 14").grid(row=1, column=1, pady=10)
        podrazumevana_vrednost = '1'
        ttk.OptionMenu(self._root, self._sprat, podrazumevana_vrednost, *self.spratovi).grid(row=1, column=2)

    def izaberi_prostoriju(self):
        Label(self._root, justify=LEFT, text="Broj prostorije:", font="Times 15").grid(row=2, column=1, pady=10)
        self._broj_prostorije = ttk.Entry(self._root)
        self._broj_prostorije.grid(row=2, column=2, columnspan=10)

    def izaberi_namenu_prostorije(self):
        Label(self._root, text="Namena prostorije:", font="Times 15", justify=LEFT).grid(row=3, column=1, pady=10)
        podrazumevana_vrednost = 'operaciona sala'
        ttk.OptionMenu(self._root, self._namena_prostorije, podrazumevana_vrednost, *self.moguce_namene_prostorija) \
            .grid(row=3, column=2)

    def proveri_validnost(self):
        if not self._broj_prostorije.get() or not self._namena_prostorije.get():
            messagebox.showerror("GRESKA", "Neispravan unos.")
        elif ProstorijeServis().pronadji_prostoriju(self._sprat.get(), self._broj_prostorije.get()):
            messagebox.showerror("GRESKA", "Soba vec postoji")
        else:
            self.__sacuvaj_prostoriju()

    def __sacuvaj_prostoriju(self):
        prostorija = Prostorija(self._sprat.get(), self._broj_prostorije.get(), {}, self._namena_prostorije.get())
        ProstorijeServis().dodavanje_prostorije(prostorija)
        messagebox.showinfo("USPESNO", "Uspesno ste dodali prostoriju")
        self._root.destroy()


def poziv_forme_unos_prostorije(root):
    application = NovaProstorija(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('425x200')
    poziv_forme_unos_prostorije(root)
