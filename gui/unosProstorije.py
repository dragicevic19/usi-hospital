from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model.kreiranje_objekata_entiteta import lista_ucitanih_prostorija, KreiranjeObjekata
from model.prostorija import Prostorija


class NovaProstorija:
    spratovi = ('1', '2', '3', '4')
    moguce_namene_prostorija = ('operaciona sala', 'sala za preglede', 'soba za lezanje')

    def __init__(self, root):
        self._root = root
        self._sprat = StringVar(self._root)
        # self._sprat.set(self.spratovi[0])
        self._prostorija = None
        self._namena_prostorije = StringVar(self._root)
        self._namena_prostorije.set(self.moguce_namene_prostorija[0])

        self._root.title("Kreiranje nove prostorije")
        self.izaberi_sprat()
        self.izaberi_prostoriju()
        self.izaberi_namenu_prostorije()
        ttk.Button(self._root, text="POTVRDI", command=self.sacuvaj_prostoriju).grid(row=4, column=2)

    def izaberi_sprat(self):
        Label(self._root, text="Sprat:", font="Times 14").grid(row=1, column=1, pady=10)
        default = '1'
        ttk.OptionMenu(self._root, self._sprat, default, *self.spratovi).grid(row=1, column=2)

    def izaberi_prostoriju(self):
        Label(self._root, justify=LEFT, text="Broj prostorije:", font="Times 15").grid(row=2, column=1, pady=10)
        self._prostorija = ttk.Entry()
        self._prostorija.grid(row=2, column=2, columnspan=10)

    def izaberi_namenu_prostorije(self):
        Label(self._root, text="Namena prostorije:", font="Times 15", justify=LEFT).grid(row=3, column=1, pady=10)
        default = 'operaciona sala'
        ttk.OptionMenu(self._root, self._namena_prostorije, default, *self.moguce_namene_prostorija).grid(row=3,
                                                                                                          column=2)

    def sacuvaj_prostoriju(self):
        if not self._prostorija.get() or not self._namena_prostorije.get() or not self._prostorija.get().isnumeric():
            messagebox.showerror("GRESKA", "Neispravan unos.")
        elif KreiranjeObjekata.postoji_prostorija(self._sprat.get(), self._prostorija.get()):
            messagebox.showerror("GRESKA", "Soba vec postoji")
        else:
            prostorija = Prostorija(self._sprat.get(), self._prostorija.get(), [], self._namena_prostorije.get())
            lista_ucitanih_prostorija.append(prostorija)
            messagebox.showinfo("USPESNO", "Uspesno ste dodali prostoriju")
            self._root.destroy()


if __name__ == '__main__':
    root = Tk()
    root.geometry('425x200')
    application = NovaProstorija(root)
    root.mainloop()
