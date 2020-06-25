from gui.prikaz_entiteta.prikaz_opreme import PrikazOpreme
from tkinter import messagebox
from tkinter import ttk
from tkinter import *



class BrisanjeOpreme(PrikazOpreme):

    def __init__(self, root,prostorije_servis,oprema_servis):
        self._prostorije_servis = prostorije_servis
        self._oprema_servis = oprema_servis
        super().__init__(root,self._oprema_servis)
        potvrdi_dugme = ttk.Button(self._root, text="OBRISI", command=self.obrisi_opremu)
        potvrdi_dugme.pack(fill='x')

    def obrisi_opremu(self):
        try:
            odabrana = self.treeview.focus()
            odabrana_oprema = self.treeview.item(odabrana)['values']
            naziv_opreme_odabrane = odabrana_oprema[0]
            self._oprema_servis.obrisi_opremu(naziv_opreme_odabrane)
            self._prostorije_servis.obrisi_opremu_iz_prostorija(naziv_opreme_odabrane)
            messagebox.showinfo("USPESNO", "Uspesno ste obrisali opremu!")
            self._root.destroy()
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali opremu!")


def poziv_forme_brisanje_opreme(root,prostorije_servis,oprema_servis):
    # root = Tk()
    application = BrisanjeOpreme(root,prostorije_servis,oprema_servis)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_forme_brisanje_opreme(root)
