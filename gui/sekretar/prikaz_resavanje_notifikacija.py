from tkinter import ttk, messagebox
from tkinter import *
from gui.prikaz_entiteta.prikaz_notifikacija import PrikazNotifikacija
from servis.kalendar.kalendar_servis import KalendarServis


class PrikazIResavanjeNotifikacija(PrikazNotifikacija):

    def __init__(self, root, tip_notifikacije):
        self._root = root
        self._tip_notifikacije = tip_notifikacije
        super().__init__(self._root, tip_notifikacije)
        messagebox.showinfo('Uputstvo',
                            'Kada zelite da selektujete obavljenu notifikaciju - dvoklik\n na kolonu \'Zavrseno\'')
        ttk.Button(self._root, text='OBRISI OZNACENE NOTIFIKACIJE', command=self.brisi_notifikacije).pack(fill='x')

    def brisi_notifikacije(self):
        KalendarServis().brisi_selektovane_notifikacije(self._lista_selektovanih_notifikacija, self._tip_notifikacije)
        messagebox.showinfo('USPESNO', 'Uspesno ste obrisali oznacene notifikacije!')
        self._root.destroy()


def prikaz_notifikacija(tip_notifikacije):
    root = Tk()
    app = PrikazIResavanjeNotifikacija(root, tip_notifikacije)
    root.mainloop()
