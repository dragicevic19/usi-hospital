from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from services.oprema.oprema_servis import OpremaService
from gui.prikaz_entiteta.prikazOpreme import PrikazOpreme


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
            OpremaService.obrisi_opremu(naziv_opreme_odabrane)
            OpremaService.obrisi_opremu_iz_prostorija(naziv_opreme_odabrane)
            messagebox.showinfo("USPESNO", "Uspesno ste obrisali opremu!")
            self._root.destroy()
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali opremu!")


def poziv_forme_brisanje_opreme(root):
    #root = Tk()
    application = BrisanjeOpreme(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_forme_brisanje_opreme(root)


