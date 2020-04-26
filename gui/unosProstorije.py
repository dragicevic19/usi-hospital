import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model.kreiranje_objekata_entiteta import KreiranjeObjekataEntiteta as KreiranjeObjekata


class NovaProstorija:
    spratovi = ('1', '2', '3', '4')
    moguce_namene_prostorija = ('operaciona sala', 'sala za preglede', 'soba za lezanje')

    def __init__(self, root):
        self._root = root
        self._sprat = StringVar(self._root)
        self._sprat.set(self.spratovi[0])
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
        default = 'Operaciona sala'
        ttk.OptionMenu(self._root, self._namena_prostorije, default, *self.moguce_namene_prostorija).grid(row=3,
                                                                                                          column=2)

    def sacuvaj_prostoriju(self):
        if not self._prostorija.get() or not self._namena_prostorije.get():
            messagebox.showerror("GRESKA", "Neispravan unos.")
        elif KreiranjeObjekata.postoji_prostorija(self._sprat.get(), self._prostorija.get()):
            messagebox.showerror("GRESKA", "Soba vec postoji")
        else:

            messagebox.showinfo("USPESNO", "Uspesno ste dodali prostoriju")


if __name__ == '__main__':
    root = Tk()
    root.geometry('425x425')
    application = NovaProstorija(root)
    root.mainloop()

    # e = Entry(root, width=50, borderwidth=5)
    #
    #
    # def onClick():
    #     hello = "Hello " + e.get()
    #     myLabel = Label(root, text=hello).pack()
    #
    #
    # # e.pack()
    #
    # dugme = Button(root, text="Ime:", command=onClick, bg="black", fg="red").pack()
    #
    # button_quit = Button(root, text="Exit Program", command=root.quit).pack()
