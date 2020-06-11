from tkinter import ttk, Tk, messagebox

from gui.lekar.dodavanje_anamneze_pacijentu import DodavanjeAnamnezePacijentu
from gui.prikaz_entiteta.prikazKorisnika import PrikazKorisnika
from repository.korisnik.korisnik_repozitorijum import KorisnikRepository

""" 
 na dvoklik na pacijenta, izlazi nova forma
 formi se prosledjuje objekat pacijenta tako sto ce se iz kolone kor. ime
 pozvati fun. pronadji po kor. imenu

 u novom root-u
 imam objekat pacijenta, na novoj formi prikazujem sve njegove anamneze
 ispod toga textbox(veci) i dugme za unos anamneze

"""


class AzuriranjeAnamneze(PrikazKorisnika):

    def __init__(self, root):
        super().__init__(root, "PACIJENT")
        self.treeview.bind('<Double-1>', self._selektuj_korisnika)

    def _selektuj_korisnika(self, event):
        try:
            pacijent = self.selektovani_pacijent()
            DodavanjeAnamnezePacijentu(pacijent)
        except IndexError:
            pass

    def selektovani_pacijent(self):
        odabrana = self.treeview.focus()
        odabrani_pacijent = self.treeview.item(odabrana)['values']
        korisnicko_ime = str(odabrani_pacijent[0])
        pacijent = KorisnikRepository.nadji_po_korisnickom_imenu(korisnicko_ime)
        return pacijent


if __name__ == '__main__':
    root = Tk()
    AzuriranjeAnamneze(root)
    root.mainloop()
