from services.opremaService import OpremaService
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model.kreiranje_objekata_entiteta import KreiranjeObjekata, lista_ucitane_bolnicke_opreme
from services.opremaService import OpremaService


class NovaOprema:

    def __init__(self, root):
        self._root = root

        self._naziv = None
        self._opis = None
        self._kolicina = None

        self.unesi_naziv()
        self.unesi_opis()
        self.unesi_kolicinu()

        ttk.Button(self._root, text="POTVRDI", command=self.sacuvaj_opremu).grid(row=6, column=2)

    def unesi_naziv(self):
        Label(self._root, justify=LEFT, text="Naziv opreme:", font="Times 15").grid(row=2, column=1, pady=10)
        self._naziv = ttk.Entry(self._root)
        self._naziv.grid(row=2, column=2, columnspan=10)

    def unesi_opis(self):
        Label(self._root, justify=LEFT, text="Opis:", font="Times 15").grid(row=3, column=1, pady=10)
        self._opis = ttk.Entry(self._root)
        self._opis.grid(row=3, column=2, columnspan=10)

    def unesi_kolicinu(self):
        Label(self._root, justify=LEFT, text="Kolicina:", font="Times 15").grid(row=4, column=1, pady=10)
        self._kolicina = ttk.Entry(self._root)
        self._kolicina.grid(row=4, column=2, columnspan=10)

    # koristi se za detekciju opreme koja vec postoji u sistemu, kako bi se novododata oprema sabrala sa postojecom
    def sacuvaj_opremu(self):

        pronadjena_oprema = KreiranjeObjekata.postoji_oprema(self._naziv.get())

        if not self._naziv.get() or not self._opis.get() or not self._kolicina.get():
            messagebox.showerror("GRESKA", "Neispravan unos.")
        elif pronadjena_oprema:
            OpremaService.dodaj_postojecu_opremu(pronadjena_oprema, self._kolicina.get())
            messagebox.showinfo("USPESNO", "Uspesno ste dodali opremu")
            self._root.destroy()
        else:
            OpremaService.dodaj_opremu(self._naziv.get(), self._opis.get(), self._kolicina.get())
            messagebox.showinfo("USPESNO", "Uspesno ste dodali opremu")
            self._root.destroy()


def poziv_forme_unos_opreme(root):
    application = NovaOprema(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('325x225')
    poziv_forme_unos_opreme(root)
