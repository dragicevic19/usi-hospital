from gui.prikaz_entiteta.prikaz_anamneze import PrikazAnamneze
from tkinter import *
from tkinter import messagebox


class PregledAnamneze(PrikazAnamneze):

    def __init__(self, root, ulogovan_pacijent):
        super().__init__(root, ulogovan_pacijent)
        self.treeview.bind('<Double-1>', self._odabir_pacijenta)

    def _odabir_pacijenta(self, event):
        try:
            odabrani = self.treeview.focus()
            odabrani_unos_anamneze = self.treeview.item(odabrani)['values']
            odabrani_opis = odabrani_unos_anamneze[1]
            self.ispis_opisa(odabrani_opis)
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali unos anamneze!")

    def ispis_opisa(self, selektovan_unos_anamneze):
        root2 = Tk()
        root2.geometry('600x200')
        application = DetaljnijiOpis(root2, selektovan_unos_anamneze, self._root)
        root2.mainloop()


class DetaljnijiOpis(PregledAnamneze):

    def __init__(self, root2, selektovan_unos_anamneze, root):
        self._stari_root = root
        self._root2 = root2
        self._selektovan_unos_anamneze = selektovan_unos_anamneze
        self._root2.title("Detaljan opis")
        self.detaljniji_opis()

    def detaljniji_opis(self):
        text = Text(self._root2)
        text.insert(INSERT, self._selektovan_unos_anamneze)
        text.config(state=DISABLED)
        text.pack()


def poziv_forme_pregled_anamneze(root, ulogovan_pacijent):
    # root = Tk()
    PregledAnamneze(root, ulogovan_pacijent)
    root.mainloop()

#
# if __name__ == '__main__':
#     root = Tk()
#     ulogovan_pacijent = lista_ucitanih_korisnika[23]
#     poziv_forme_pregled_anamneze(root, ulogovan_pacijent)
