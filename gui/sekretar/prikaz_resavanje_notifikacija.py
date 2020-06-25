from tkinter import ttk, messagebox
from tkinter import *
from gui.prikaz_entiteta.prikaz_notifikacija import PrikazNotifikacija



class PrikazIResavanjeNotifikacija(PrikazNotifikacija):

    def __init__(self, root, tip_notifikacije,kalendar_servis):
        self._root = root
        self._tip_notifikacije = tip_notifikacije
        self._kalendar_servis = kalendar_servis

        super().__init__(self._root, tip_notifikacije,self._kalendar_servis)
        messagebox.showinfo('Uputstvo',
                            'Kada zelite da selektujete obavljenu notifikaciju - dvoklik\n na kolonu \'Zavrseno\'')
        ttk.Button(self._root, text='OBRISI OZNACENE NOTIFIKACIJE', command=self.brisi_notifikacije).pack(fill='x')

    def brisi_notifikacije(self):
        self._kalendar_servis.brisi_selektovane_notifikacije(self._lista_selektovanih_notifikacija, self._tip_notifikacije)
        messagebox.showinfo('USPESNO', 'Uspesno ste obrisali oznacene notifikacije!')
        self._root.destroy()


def prikaz_notifikacija(tip_notifikacije,kalendar_servis):
    root = Tk()
    app = PrikazIResavanjeNotifikacija(root, tip_notifikacije,kalendar_servis)
    root.mainloop()
