from gui.prikaz_entiteta.prikaz_opreme import PrikazOpreme
from servis.oprema.oprema_servis import OpremaServis
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from servis.prostorije.prostorije_servis import ProstorijeServis


class BrisanjeOpreme(PrikazOpreme):

    def __init__(self, root):
        super().__init__(root)
        potvrdi_dugme = ttk.Button(self._root, text="OBRISI", command=self.obrisi_opremu)
        potvrdi_dugme.pack(fill='x')

    def obrisi_opremu(self):
        try:
            odabrana = self.treeview.focus()
            odabrana_oprema = self.treeview.item(odabrana)['values']
            naziv_opreme_odabrane = odabrana_oprema[0]
            OpremaServis().obrisi_opremu(naziv_opreme_odabrane)
            ProstorijeServis().obrisi_opremu_iz_prostorija(naziv_opreme_odabrane)
            messagebox.showinfo("USPESNO", "Uspesno ste obrisali opremu!")
            self._root.destroy()
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali opremu!")


def poziv_forme_brisanje_opreme(root):
    # root = Tk()
    application = BrisanjeOpreme(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_forme_brisanje_opreme(root)
