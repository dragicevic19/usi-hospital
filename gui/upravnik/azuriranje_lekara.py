from gui.prikaz_entiteta.prikaz_korisnika import PrikazKorisnika
from model.enum.uloga import Uloga
from model.konstante.konstante import REGEX_VREME_OD_DO

from servis.korisnik.korisnik_servis import KorisnikServis
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class IzborLekara(PrikazKorisnika):

    def __init__(self, root):
        super().__init__(root, Uloga.LEKAR.name)
        azuriraj_dugme = ttk.Button(self._root, text="AZURIRAJ LEKARA", command=self.otvori_formu_za_azuriranje)
        azuriraj_dugme.pack(fill='x')

    def otvori_formu_za_azuriranje(self):
        try:
            odabrani = self.treeview.focus()
            odabrani_lekar = self.treeview.item(odabrani)['values']
            korisnicko_ime_lekara = odabrani_lekar[0]
            self.pokretanje_unosa_podataka(korisnicko_ime_lekara)
        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali lekara!")

    def pokretanje_unosa_podataka(self, selektovani_lekar):
        root2 = Tk()
        root2.geometry('330x260')
        application = UnosPodataka(root2, selektovani_lekar, self._root)
        root2.mainloop()


class UnosPodataka(IzborLekara):

    def __init__(self, root2, selektovani_lekar, root):
        self._stari_root = root
        self._root2 = root2
        self._korisnicko_ime_lekara = selektovani_lekar
        self._radno_vreme = None
        self._spisak_specijalizacija = None

        self._root2.title("Podaci o lekaru")
        self.pronadji_podrazumevane_vrednosti()
        self.unesi_novo_radno_vreme()
        self.unesi_novi_spisak_specijalizacija()

        ttk.Button(self._root2, text="POTVRDI",
                   command=self.provera_unetih_podataka).grid(row=6, column=2, pady=10)

    def pronadji_podrazumevane_vrednosti(self):
        lekar = KorisnikServis().pronadji_korisnika_po_korisnickom_imenu(self._korisnicko_ime_lekara)
        self._podrazumevano_radno_vreme = lekar.get_radno_vreme()
        self._podrazumevani_spisak_specijalizacija = lekar.get_spisak_specijalizacija()

    def unesi_novo_radno_vreme(self):

        Label(self._root2, justify=LEFT, text="Radno vreme:", font="Times 15").grid(row=2, column=1, pady=10)
        self._radno_vreme = ttk.Entry(self._root2)
        self._radno_vreme.insert(0, self._podrazumevano_radno_vreme)
        self._radno_vreme.grid(row=2, column=2, columnspan=10)

    def unesi_novi_spisak_specijalizacija(self):

        Label(self._root2, justify=LEFT, text="Spisak specijalizacija:", font="Times 15").grid(row=3, column=1, pady=10)
        self._spisak_specijalizacija = ttk.Entry(self._root2)
        self._spisak_specijalizacija.insert(0, self._podrazumevani_spisak_specijalizacija)
        self._spisak_specijalizacija.grid(row=3, column=2, columnspan=10)

    def provera_unetih_podataka(self):

        if not self._radno_vreme.get() or not self._spisak_specijalizacija.get():
            messagebox.showerror("GRESKA", "Neispravan unos.")
            self._root2.destroy()
        elif not REGEX_VREME_OD_DO.match(self._radno_vreme.get()):
            messagebox.showerror("GRESKA", "Neispravan unos radnog vremena.")
        else:
            self.azuriraj_lekara()

    def azuriraj_lekara(self):
        KorisnikServis().azuriraj_lekara(self._korisnicko_ime_lekara, self._radno_vreme.get(),
                                         self._spisak_specijalizacija.get())
        messagebox.showinfo("USPESNO", "Uspesno ste azurirali lekara")
        self._root2.destroy()
        self._stari_root.destroy()


def poziv_forme_azuriranje_lekara(root):
    a = IzborLekara(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    poziv_forme_azuriranje_lekara(root)
