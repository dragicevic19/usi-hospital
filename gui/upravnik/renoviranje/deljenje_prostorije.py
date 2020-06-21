import datetime
from tkinter import *
from tkinter import ttk, messagebox
from gui.upravnik.renoviranje.premestanje_opreme import ScrollableFrame
from model.dto.broj_i_naziv_opreme_dto import BrojINazivOpremeDTO
from model.dto.dogadjaji_dto.deljenje_prostorije_dto import DeljenjeProstorijeDTO
from servis.prostorije.prostorije_servis import ProstorijeServis


class DeljenjeProstorije:
    namene_prostorija = ('sala za preglede', 'operaciona sala', 'soba za lezanje')

    def __init__(self, root, prostorija):
        self._root = root
        self._root.title("Deljenje prostorije")
        self._prostorija = prostorija
        self._frame = ScrollableFrame(root)
        self._dostupna_oprema = []
        self._namena_prve = StringVar(self._root)
        self._namena_prve.set(self.namene_prostorija[0])
        self._namena_druge = StringVar(self._root)
        self._namena_druge.set(self.namene_prostorija[0])
        self._datum_zavrsetka_radova = ttk.Entry(self._root)
        self._datum_pocetka_radova = ttk.Entry(self._root)
        self._novi_br_prostorije2 = ttk.Entry(self._root)
        self._novi_br_prostorije1 = ttk.Entry(self._root)
        self._naziv_broj_odabrane_opreme = {}

        self.izaberi_datum()
        self.izaberi_brojeve_prostorija()
        self.izaberi_namenu_prostorija()
        self.rasporedi_opremu()

    def izaberi_datum(self):
        pocetak_Label = Label(self._root, justify=LEFT, text="Datum pocetka radova (dd/mm/gggg):", font="Times 15")
        pocetak_Label.grid(row=0, sticky=W, column=0, pady=10)

        self._datum_pocetka_radova.grid(row=0, column=1, sticky=W, padx=10)

        kraj_Label = Label(self._root, justify=LEFT, text="Datum zavrsetka radova (dd/mm/gggg):", font="Times 15")
        kraj_Label.grid(row=1, column=0, sticky=W, pady=10)

        self._datum_zavrsetka_radova.grid(row=1, column=1, sticky=W, padx=9)

    def izaberi_brojeve_prostorija(self):
        soba1_Label = Label(self._root, justify=LEFT, text="Broj prve prostorije: ", font="Times 14")
        soba1_Label.grid(row=2, column=0, sticky=W, pady=10)

        self._novi_br_prostorije1.grid(row=3, column=0, sticky=W, pady=5, padx=10)

        soba2_Label = Label(self._root, justify=LEFT, text="Broj druge prostorije: ", font="Times 14")
        soba2_Label.grid(row=2, column=1, sticky=W, pady=10)

        self._novi_br_prostorije2.grid(row=3, column=1, sticky=W, pady=5, padx=10)

    def izaberi_namenu_prostorija(self):
        namena1_Label = Label(self._root, justify=LEFT, text='Namena prve prostorije: ', font="Times 14")
        namena1_Label.grid(row=4, column=0, pady=10, sticky=W)
        default = self._namena_prve.get()
        ttk.OptionMenu(self._root, self._namena_prve, default, *self.namene_prostorija).grid(row=5, column=0, sticky=W,
                                                                                             pady=5, padx=10)
        namena2_Label = Label(self._root, justify=LEFT, text='Namena druge prostorije: ', font="Times 14")
        namena2_Label.grid(row=4, column=1, pady=10, sticky=W)
        default = self._namena_druge.get()
        ttk.OptionMenu(self._root, self._namena_druge, default, *self.namene_prostorija).grid(row=5, column=1, sticky=W,
                                                                                              pady=5, padx=10)

    def rasporedi_opremu(self):
        self.pronadji_dostupnu_opremu()
        self.ispisi_labele_za_opremu()
        self.ispisi_mogucu_opremu_i_kolicinu()
        self._frame.grid(row=7, column=0)
        ttk.Button(self._root, text="Potvrdi", command=self.provera_unosa).grid(row=8, column=1, sticky=E)

    def ispisi_labele_za_opremu(self):
        Label(self._frame.scrollable_frame, justify=LEFT, text="Izaberi opremu", font="Times 12").grid(row=6, column=0,
                                                                                                       sticky=W,
                                                                                                       pady=15)
        oprema1_Label = Label(self._frame.scrollable_frame, justify=LEFT, text="Prva soba:", font="Times 12")
        oprema1_Label.grid(row=6, column=1, sticky=W, pady=15, padx=15)
        oprema2_Label = Label(self._frame.scrollable_frame, justify=LEFT, text="Druga soba:",
                              font="Times 12")
        oprema2_Label.grid(row=6, column=2, sticky=W, pady=15, padx=15)

    def ispisi_mogucu_opremu_i_kolicinu(self):
        red = 7
        for oprema in self._dostupna_oprema:
            Label(self._frame.scrollable_frame, text=oprema.naziv_opreme, font="Times 12").grid(row=red, column=0,
                                                                                                sticky=W, pady=2)
            broj_opreme_prostorija1 = ttk.Entry(self._frame.scrollable_frame, width=10)
            broj_opreme_prostorija1.insert(INSERT, "0")
            broj_opreme_prostorija1.grid(row=red, column=1, sticky=W, pady=2, padx=10)

            broj_opreme_prostorija2 = ttk.Entry(self._frame.scrollable_frame, width=10)
            broj_opreme_prostorija2.insert(INSERT, "0")
            broj_opreme_prostorija2.grid(row=red, column=2, sticky=W, pady=2, padx=10)

            max_tekst = "max: " + str(oprema.broj_slobodne_opreme)
            Label(self._frame.scrollable_frame, text=max_tekst, font="Times 10").grid(row=red, column=3, sticky=W,
                                                                                      pady=2)
            self._naziv_broj_odabrane_opreme[oprema.naziv_opreme] = [broj_opreme_prostorija1, broj_opreme_prostorija2,
                                                                     oprema.broj_slobodne_opreme]
            red += 1

    def pronadji_dostupnu_opremu(self):
        for naziv, broj_opreme in self._prostorija.get_spisak_opreme().items():
            if broj_opreme > 0:
                opremaDTO = BrojINazivOpremeDTO(naziv, int(broj_opreme))
                self._dostupna_oprema.append(opremaDTO)

    def provera_unosa(self):
        if not self.provera_datuma():
            messagebox.showerror("GRESKA", "Los format datuma!")
        if self.provera_broja_prostorija():
            if self.provera_unosa_opreme():
                lista_opreme = self.napravi_objekteDTO()
                self.provera_zauzeca(lista_opreme)

    def napravi_objekteDTO(self):
        lista_opreme = []
        for naziv, broj_opreme in self._naziv_broj_odabrane_opreme.items():
            visak_opreme = broj_opreme[2] - (int(broj_opreme[0].get()) + int(broj_opreme[1].get()))
            renoviranjeDTO = DeljenjeProstorijeDTO(self._datum_pocetka, self._datum_zavrsetka, self._prostorija,
                                                   naziv, broj_opreme[0].get(), broj_opreme[1].get(),
                                                   visak_opreme, self._namena_prve.get(),
                                                   self._namena_druge.get(), self._novi_br_prostorije1.get(),
                                                   self._novi_br_prostorije2.get())
            lista_opreme.append(renoviranjeDTO)
        return lista_opreme

    def provera_zauzeca(self, lista_opreme):
        if not lista_opreme:
            messagebox.showerror()
        if ProstorijeServis().deljenje_prostorije(lista_opreme):
            messagebox.showinfo('USPESNO', 'Uspesno ste zakazali renoviranje prostorije!')
            self._root.destroy()
        else:
            messagebox.showerror('GRESKA', 'Prostorija je zauzeta u tom periodu!')

    def provera_datuma(self):
        try:
            d, m, g = self._datum_pocetka_radova.get().split("/")
            self._datum_pocetka = datetime.date(int(g), int(m), int(d))
            d, m, g = self._datum_zavrsetka_radova.get().split("/")
            self._datum_zavrsetka = datetime.date(int(g), int(m), int(d))
            if self._datum_pocetka < datetime.date.today() or self._datum_zavrsetka < self._datum_pocetka:
                return False

        except ValueError:
            return False
        return True

    def provera_broja_prostorija(self):
        ProstorijeServis().obrisi_sobe(self._prostorija)
        sprat = self._prostorija.get_sprat()
        if ProstorijeServis().slobodan_broj_prostorije(sprat, self._novi_br_prostorije1):
            if ProstorijeServis().slobodan_broj_prostorije(sprat, self._novi_br_prostorije2):
                return True
            else:
                messagebox.showerror("GRESKA", "Broj druge prostorije je zauzet!")
        else:
            messagebox.showerror('GRESKA', 'Broj prve prostorije je zauzet!')
        return False

    def provera_unosa_opreme(self):
        for naziv, broj_opreme in self._naziv_broj_odabrane_opreme.items():
            if not broj_opreme[0].get():
                messagebox.showerror("GRESKA", "Popunite sva polja!")
                return False
            br_opreme1, br_opreme2 = int(broj_opreme[0].get()), int(broj_opreme[1].get())
            max_br_opreme = broj_opreme[2]
            if br_opreme1 < 0 or br_opreme2 < 0 or br_opreme1 + br_opreme2 > max_br_opreme:
                messagebox.showerror("GRESKA", "Lose unet broj opreme!")
                return False
        return True


def deljenje_prostorije(selektovana_prostorija):
    root = Tk()
    root.geometry('750x650')
    DeljenjeProstorije(root, selektovana_prostorija)
    root.mainloop()

# if __name__ == '__main__':
#     root = Tk()
#     root.geometry('800x650')
#     selektovana_prostorija = lista_ucitanih_prostorija[2]
#     application = DeljenjeProstorije(root, selektovana_prostorija)
#     root.mainloop()
