from gui.lekar.dodavanje_anamneze_pacijentu import DodavanjeAnamnezePacijentu
from gui.prikaz_entiteta.prikaz_korisnika import PrikazKorisnika
from tkinter import Tk


""" 
 na dvoklik na pacijenta, izlazi nova forma
 formi se prosledjuje objekat pacijenta tako sto ce se iz kolone kor. ime
 pozvati fun. pronadji po kor. imenu

 u novom root-u
 imam objekat pacijenta, na novoj formi prikazujem sve njegove anamneze
 ispod toga textbox(veci) i dugme za unos anamneze

"""


class AzuriranjeAnamneze(PrikazKorisnika):

    def __init__(self, root, lekar,korisnik_servis,unos_anamneze_servis):

        self._lekar = lekar
        self._korisnik_servis = korisnik_servis
        self._unos_anamneze_servis = unos_anamneze_servis
        super().__init__(root,self._korisnik_servis, "PACIJENT")
        self.treeview.bind('<Double-1>', self._selektuj_korisnika)

    def _selektuj_korisnika(self, event):
        try:
            pacijent = self.selektovani_pacijent()
            DodavanjeAnamnezePacijentu(pacijent, self._lekar,self._unos_anamneze_servis)
        except IndexError:
            pass

    def selektovani_pacijent(self):
        odabrani = self.treeview.focus()
        odabrani_pacijent = self.treeview.item(odabrani)['values']
        korisnicko_ime = str(odabrani_pacijent[0])
        pacijent = self._korisnik_servis.pronadji_korisnika_po_korisnickom_imenu(korisnicko_ime)
        return pacijent


def poziv_forme_za_dodavanje_anamneze_odredjenom_pacijentu(root, ulogovani_lekar,korisnik_servis,unos_anamneze_servis):
    AzuriranjeAnamneze(root, ulogovani_lekar,korisnik_servis,unos_anamneze_servis)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_forme_za_dodavanje_anamneze_odredjenom_pacijentu(root, "horacije442")
