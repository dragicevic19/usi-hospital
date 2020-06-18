import datetime
from tkinter import *
from tkinter import ttk, messagebox

from model.DTO.dogadjajiDTO.zakazivanje_operacija_DTO import ZakazivanjeOperacijeDTO
from model.enum.namena_prostorije import NamenaProstorije
from model.enum.tip_zahvata import TipZahvata
from model.konstante.konstante import REGEX_VREME
from repozitorijum.korisnik.korisnik_repozitorijum import lista_ucitanih_korisnika
from servisi.prostorije.prostorije_servis import ProstorijeServis


class ZakazivanjeOperacije:

    def __init__(self, root, ulogovani_lekar, pacijent):
        self._hitna_operacija = StringVar()
        self._root = root
        self._lekar = ulogovani_lekar
        self._pacijent = pacijent
        self._lista_operacionih_sala = ProstorijeServis.pronadji_prostorije_po_nameni(
            NamenaProstorije.OPERACIONA_SALA.value)
        self._datum_pocetka_operacije = ttk.Entry(self._root)
        self._vreme_pocetka = ttk.Entry(self._root)
        self._vreme_zavrsetka = ttk.Entry(self._root)

        self._opearciona_sala = StringVar(self._root)
        self._opearciona_sala.set(self._lista_operacionih_sala[0])
        self.izaberi_datum_i_vreme()
        self.izaberi_operacionu_salu()
        self.hitna_operacija()
        ttk.Button(self._root, text="Potvrdi", command=self.provera_unosa).grid(row=5, column=0, sticky=E, padx=60,
                                                                                pady=20)

    def izaberi_datum_i_vreme(self):
        pocetak_Label = Label(self._root, justify=LEFT, text="Datum operacije (dd/mm/gggg):", font="Times 15")
        pocetak_Label.grid(row=0, sticky=W, column=0, pady=10)
        self._datum_pocetka_operacije.grid(row=0, column=1, sticky=W, padx=10)

        pocetak_vreme_Label = Label(self._root, justify=LEFT, text="Vreme pocetka operacije (hh:mm):", font="Times 15")
        pocetak_vreme_Label.grid(row=1, sticky=W, column=0, pady=10)
        self._vreme_pocetka.grid(row=1, column=1, sticky=W, padx=10)

        kraj_vreme_Label = Label(self._root, justify=LEFT, text="Ocekivano vreme zavrsetka operacije (hh:mm):",
                                 font="Times 15")
        kraj_vreme_Label.grid(row=2, sticky=W, column=0, pady=10)
        self._vreme_zavrsetka.grid(row=2, column=1, sticky=W, padx=10)

    def izaberi_operacionu_salu(self):
        op_sala_Label = Label(self._root, justify=LEFT, text="Operaciona sala:", font="Times 15")
        op_sala_Label.grid(row=3, sticky=W, column=0, pady=10)
        default = self._opearciona_sala.get()
        op_sala_OptionMenu = ttk.OptionMenu(self._root, self._opearciona_sala, default, *self._lista_operacionih_sala)
        op_sala_OptionMenu.grid(row=3, column=1, pady=5, padx=10)

    def hitna_operacija(self):
        self._hitno_check = ttk.Checkbutton(self._root, text="HITNA OPERACIJA",
                                            variable=self._hitna_operacija, offvalue='', onvalue='hitno')
        self._hitno_check.grid(row=4, column=1, padx=10)

    def provera_unosa(self):
        if not self.provera_datuma():
            messagebox.showerror("GRESKA", "Los format datuma!")
        elif not REGEX_VREME.match(self._vreme_pocetka.get()) or not REGEX_VREME.match(self._vreme_zavrsetka.get()):
            messagebox.showerror("GRESKA", "Neispravan unos vremena.")
        else:
            self.provera_zauzeca()

    def provera_datuma(self):
        try:
            d, m, g = self._datum_pocetka_operacije.get().split("/")
            self._datum_pocetka = datetime.date(int(g), int(m), int(d))  # regex
            if self._datum_pocetka < datetime.date.today():
                return False
        except ValueError:
            return False
        return True

    def provera_zauzeca(self):
        operacijaDTO = ZakazivanjeOperacijeDTO(self._datum_pocetka, self._vreme_pocetka.get(),
                                               self._vreme_zavrsetka.get(), self._lekar.get_korisnicko_ime(),
                                               self._pacijent,
                                               self._opearciona_sala.get(), self._hitna_operacija.get(),
                                               TipZahvata.OPERACIJA.value)
        print(self._hitna_operacija.get())
        if ProstorijeServis.zakazivanje_operacije(operacijaDTO):
            messagebox.showinfo('USPESNO', 'Uspesno ste zakazali operaciju')
            self._root.destroy()
        else:
            messagebox.showerror('GRESKA', 'Prostorija je zauzeta u tom periodu')


def poziv_forme_zakazivanje_operacije(ulogovani_lekar, pacijent):
    root = Tk()
    root.geometry('700x300')
    application = ZakazivanjeOperacije(root, ulogovani_lekar, pacijent)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    korisnik = lista_ucitanih_korisnika[0]
    poziv_forme_zakazivanje_operacije(root, korisnik)
