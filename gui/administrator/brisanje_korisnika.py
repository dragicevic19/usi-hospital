from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.prikaz_entiteta.prikaz_korisnika import PrikazKorisnika
from servis.korisnik.korisnik_servis import KorisnikServis


class BrisanjeKorisnika(PrikazKorisnika):

    def __init__(self, root):
        super().__init__(root)
        potvrdi_dugme = ttk.Button(self._root, text="OBRISI", command=self.obrisi_korisnika)
        potvrdi_dugme.pack(fill='x')

    def obrisi_korisnika(self):
        try:
            odabrani = self.treeview.focus()
            odabrani_korisnik = self.treeview.item(odabrani)['values']
            korisnicko_ime_odabranog = odabrani_korisnik[0]
            KorisnikServis().obrisi_korisnika(korisnicko_ime_odabranog)
            messagebox.showinfo("USPESNO", "Uspesno ste obrisali korisnika!")
            self._root.destroy()
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali korisnika!")


def poziv_forme_brisanje_korisnika(root):
    BrisanjeKorisnika(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_forme_brisanje_korisnika(root)
