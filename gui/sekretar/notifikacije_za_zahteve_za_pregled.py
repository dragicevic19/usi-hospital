import datetime
from tkinter import *
from tkinter import ttk, messagebox

from gui.prikaz_entiteta.tabela_vremenskih_slotova import poziv_tabele_vremenskih_slotova
from model.dto.dogadjaji_dto.zakazivanje_operacija_pregled_dto import ZakazivanjeOperacijaPregledDTO
from model.enum.namena_prostorije import NamenaProstorije
from model.enum.tip_lekara import TipLekara
from model.enum.tip_notifikacije import TipNotifikacije
from model.enum.tip_zahvata import TipZahvata
from model.konstante.konstante import REGEX_VREME
from servis.kalendar.kalendar_servis import KalendarServis
from servis.korisnik.korisnik_servis import KorisnikServis
from servis.prostorije.prostorije_servis import ProstorijeServis


class ZakazivanjePregleda(object):
    def __init__(self, root, selektovana_notifikacija):
        self._root = root
        self._selektovan = selektovana_notifikacija
        self._lista_dostupnih_prostorija = ProstorijeServis().pronadji_prostorije_po_nameni(
            NamenaProstorije.SALA_ZA_PREGLEDE.value)
        self._prostorija = StringVar()
        self._prostorija.set(self._lista_dostupnih_prostorija[0])
        self._datum_pocetka_pregleda = ttk.Entry(self._root)
        self._vreme_pocetka = ttk.Entry(self._root)
        self._vreme_zavrsetka = ttk.Entry(self._root)
        self._specijalista = StringVar(self._root)
        self._lista_specijalista = KorisnikServis().vrati_lekare_specijaliste_ili_lop(TipLekara.SPECIJALISTA)
        self._specijalista.set(self._lista_specijalista[0])
        self.izaberi_prostoriju()
        self.postavi_datum()
        ttk.Button(self._root, text="Potvrdi", command=self.provera_unosa).grid(row=4, column=2, sticky=E, padx=10,
                                                                                pady=20)

    def izaberi_prostoriju(self):
        sala_label = Label(self._root, justify=LEFT, text="Sala za preglede:", font="Times 14")
        sala_label.grid(row=1, sticky=W, column=0, pady=10)
        default = self._prostorija.get()
        sala_option_menu = ttk.OptionMenu(self._root, self._prostorija, default, *self._lista_dostupnih_prostorija)
        sala_option_menu.grid(row=1, column=1, pady=5, padx=10)

    def postavi_datum(self):
        frejm = Frame(self._root)
        labela = Label(frejm,
                       text='Pregled bi trebalo da se odrzi od: ' + self._selektovan.datum_pocetka + ' do: ' + self._selektovan.datum_zavrsetka,
                       font='Console 15')
        labela.grid(row=0, column=0, pady=10, padx=5)
        frejm.grid(row=0, column=0)
        self.datum_vreme_pocetka()
        self.datum_vreme_kraj()

    def datum_vreme_pocetka(self):
        pocetak_Label = Label(self._root, justify=LEFT, text="Datum operacije (dd/mm/gggg):", font="Times 14")
        pocetak_Label.grid(row=2, sticky=W, column=0, pady=10)
        self._datum_pocetka_pregleda.grid(row=2, column=1, sticky=W, padx=10)
        pocetak_vreme_Label = Label(self._root, justify=LEFT, text="Vreme pocetka operacije (hh:mm):",
                                    font="Times 14")
        pocetak_vreme_Label.grid(row=3, sticky=W, column=0, pady=10)
        self._vreme_pocetka.grid(row=3, column=1, sticky=W, padx=10)

    def datum_vreme_kraj(self):
        kraj_vreme_Label = Label(self._root, justify=LEFT, text="Ocekivano vreme zavrsetka pregleda (hh:mm):",
                                 font="Times 14")
        kraj_vreme_Label.grid(row=4, sticky=W, column=0, pady=10)
        self._vreme_zavrsetka.grid(row=4, column=1, sticky=W, padx=10)
        ttk.Button(self._root, text="Pregledaj\nzauzeca", command=self.tabela_vremenskih_zauzeca).grid(row=2, column=2,
                                                                                                       sticky=E,
                                                                                                       padx=10)

    def tabela_vremenskih_zauzeca(self):
        if not self.provera_datuma():
            messagebox.showerror('GRESKA', 'Los format datuma!')
        else:
            poziv_tabele_vremenskih_slotova(self._datum_pocetka_pregleda.get(),
                                            *(self._prostorija.get().split('|')))

    def provera_unosa(self):
        if not self.provera_datuma():
            messagebox.showerror("GRESKA", "Los format datuma!")
        elif not REGEX_VREME.match(self._vreme_pocetka.get()) or not REGEX_VREME.match(self._vreme_zavrsetka.get()):
            messagebox.showerror("GRESKA", "Neispravan unos vremena.")
        else:
            self.provera_zauzeca()

    def provera_datuma(self):
        try:
            d, m, g = self._datum_pocetka_pregleda.get().split("/")
            self._datum_pocetka = datetime.date(int(g), int(m), int(d))  # regex
            if self._datum_pocetka < datetime.date.today():
                return False
        except ValueError:
            return False
        return True

    def provera_zauzeca(self):
        pregledDTO = ZakazivanjeOperacijaPregledDTO(self._datum_pocetka, self._vreme_pocetka.get(),
                                                    self._vreme_zavrsetka.get(), self._selektovan.lekar,
                                                    self._selektovan.pacijent, self._prostorija.get(),
                                                    TipZahvata.PREGLED.value)

        if ProstorijeServis().zakazivanje_operacije_i_pregleda(pregledDTO):
            messagebox.showinfo('USPESNO', 'Uspesno ste zakazali operaciju')
            KalendarServis().brisi_selektovane_notifikacije([self._selektovan],
                                                            TipNotifikacije.ZAHTEV_ZA_PREGLED)
            self._root.destroy()
        else:
            messagebox.showerror('GRESKA', 'Prostorija je zauzeta u tom periodu')


def poziv_forme_za_zakazivanje_pregleda(selektovana_notifikacija):
    root = Tk()
    app = ZakazivanjePregleda(root, selektovana_notifikacija)
    root.mainloop()
