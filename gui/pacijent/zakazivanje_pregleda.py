from servis.korisnik.korisnik_servis import KorisnikServis
from model.enum.tip_lekara import TipLekara
from tkinter import ttk, messagebox
from tkinter import *
import datetime
from model.dto.tabela_vremenskih_slotova import poziv_tabele_vremenskih_slotova


class ZakazivanjePregleda():

    def __init__(self, root):
        self._root = root
        self._root.title("Zakazivanje pregleda")
        self._lekar_opste_prakse = StringVar(self._root)
        self._lista_lekara_opste_prakse = KorisnikServis().vrati_lekare_specijaliste_ili_lop(TipLekara.LOP)
        self._lekar_opste_prakse.set(self._lista_lekara_opste_prakse[0])
        self._najkasniji_datum = ttk.Entry(self._root)
        self._radio_parametar = IntVar()

        self.izaberi_lop()
        self.izaberi_najkasniji_datum()
        self.preferirani_slotovi()
        self.izbor_najveceg_prioriteta()
        ttk.Button(self._root, text="POTVRDI", command=self.provera_unosa, width=20).grid(row=7, column=3, sticky=E,
                                                                                          padx=10, pady=20)
        ttk.Button(self._root, text="Izaberite slotove", command=self.prikaz_vremenskih_slotova, width=20).grid(row=2,
                                                                                   column=1, sticky=E, padx=10, pady=20)

    def izaberi_lop(self):
        Label(self._root, justify=LEFT, text="Lekar opste prakse:", font="Console 11").grid(row=0, sticky=W, column=0,
                                                                                            pady=10, padx=10)
        default = self._lekar_opste_prakse.get()
        lekar_opste_prakse_OptionMenu = ttk.OptionMenu(self._root, self._lekar_opste_prakse, default,
                                                       *self._lista_lekara_opste_prakse)
        lekar_opste_prakse_OptionMenu.grid(row=0, column=1, pady=10)

    def preferirani_slotovi(self):
        Label(self._root, text="Preferirani slotovi: ", font='Console 11').grid(row=2, column=0, sticky=W, pady=10,
                                                                                padx=10)

    def izaberi_najkasniji_datum(self):
        Label(self._root, text="Najkasniji datum (dd/mm/gggg): ", font='Console 11').grid(
            row=3, column=0, sticky=W, pady=10, padx=10)
        self._najkasniji_datum.grid(row=3, column=1)

    def izbor_najveceg_prioriteta(self):
        Label(self._root, text="Izaberite najveci prioritet: ", font='Console 11').grid(row=5, column=0, sticky=W,
                                                                                        pady=25, padx=10)
        zeljeni_lekar = Radiobutton(self._root, text="Zeljeni lekar", variable=self._radio_parametar, value=1)
        zeljeni_lekar.grid(row=5, column=1, padx=10, pady=10)
        najkasniji_datum = Radiobutton(self._root, text="Sto raniji pregled", variable=self._radio_parametar, value=2)
        najkasniji_datum.grid(row=5, column=2, padx=10, pady=10)
        preferirani_slotovi = Radiobutton(self._root, text="Zeljeni slotovi", variable=self._radio_parametar, value=3)
        preferirani_slotovi.grid(row=5, column=3, padx=10, pady=10)

    def prikaz_vremenskih_slotova(self):
        poziv_tabele_vremenskih_slotova()

    def provera_unosa(self):
        if not self.provera_datuma():
            messagebox.showerror("GRESKA", "Los format datuma! (DD/MM/GGGG)")
        else:
            print("To be continued...")

    def provera_datuma(self):
        try:
            d, m, g = self._najkasniji_datum.get().split("/")
            self._krajnji_datum = datetime.date(int(g), int(m), int(d))

            if self._krajnji_datum < datetime.date.today():
                return False
        except ValueError:
            return False
        return True


def poziv_forme_zakazivanje_pregleda():
    root = Tk()
    root.geometry('673x280')
    application = ZakazivanjePregleda(root)
    root.mainloop()


if __name__ == '__main__':
    poziv_forme_zakazivanje_pregleda()