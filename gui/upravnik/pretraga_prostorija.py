from tkinter import *
from model.dto.prenos_prostorija_dto import PretragaProstorijaDTO
from repozitorijum.oprema.oprema_repozitorijum_impl import *
import datetime
from tkinter.ttk import Combobox
# from repozitorijum.oprema.oprema_repozitorijum_impl import lista_ucitane_bolnicke_opreme
from tkinter import messagebox

from servis.oprema.oprema_servis import OpremaServis


class PretragaProstorija:
    lista_zahtevane_opreme = []

    def __init__(self, root):
        self._root = root
        self.postava()

    def postava(self):
        lista_opreme = OpremaServis().vrati_svu_opremu_u_sistemu()
        self.combo = Combobox(root, state='readonly', values=lista_opreme, width=14)
        self.combo.grid(row=1, column=1, padx=20, pady=20)
        dugme = Button(self._root, text="DODAJ OPREMU", command=self.print_vrednost_comba)
        dugme.grid(row=1, column=2, padx=20, pady=20)
        self.label = Label(self._root, text="Izabrana oprema \n za pretragu").grid(row=1, column=3, padx=20, pady=20)
        self.prikaz = Listbox(self._root)

    def grupisi(self):
        self.grupa1 = LabelFrame(self._root, text="nestoe")
        self.grupa1.grid(row=2, column=1)

        Entry(self.grupa1, text="nesto").grid(row=1)

    def print_vrednost_comba(self):
        vrednost = self.combo.get()
        if vrednost not in self.lista_zahtevane_opreme and vrednost != "":
            self.lista_zahtevane_opreme.append(vrednost)
            self.prikaz.insert(1, vrednost)
            self.prikaz.grid(row=2, column=3, padx=2, pady=20)
        else:
            if vrednost == "":
                messagebox.showinfo("Prazno", "Izaberite opremu.")
            else:
                messagebox.showinfo("Unos", "Parametar koji ste uneli vec je dodat u listu zahtevanih")


def poziv_forma_za_pretragu_prostorija(root):
    a = PretragaProstorija(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x570")
    poziv_forma_za_pretragu_prostorija(root)