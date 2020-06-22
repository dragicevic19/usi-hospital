import datetime
import tkinter as tk
from tkinter import ttk, messagebox, Label, LEFT, W, INSERT
from model.dto.dogadjaji_dto.premestanje_opreme_dto import PremestanjeOpremeDTO
from model.enum.renoviranje import TipPremestanjaOpreme
from servis.prostorije.prostorije_servis import ProstorijeServis

"""
    IZMENITI NAZIVE NA ENGLESKOM

"""


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


funkcija_za_premestanje = {
    TipPremestanjaOpreme.DODAVANJE_OPREME: ProstorijeServis().dodavanje_slobodne_opreme_u_prostoriju,
    TipPremestanjaOpreme.IZBACIVANJE_OPREME: ProstorijeServis().izbacivanje_opreme_iz_prostorije
}


class PremestanjeOpreme:
    def __init__(self, root, selektovana_prostorija, oprema_za_prikaz, tip_premestanja):
        self._root = root
        self._prostorija = selektovana_prostorija
        self._oprema_za_prikaz = oprema_za_prikaz
        self.proveri_opremu_za_prikaz()
        self._tip_premestanja = tip_premestanja
        self._datum_pocetka_radova = None
        self._datum_zavrsetka_radova = None
        self._naziv_broj_odabrane_opreme = {}
        self._frame = ScrollableFrame(root)

        self.izaberi_datum()
        self.izaberi_opremu()

    def proveri_opremu_za_prikaz(self):
        if not self._oprema_za_prikaz:
            messagebox.showinfo("UPOZORENJE", "Trenutno nema slobodne opreme!")
            self._root.destroy()

    def izaberi_datum(self):
        pocetak_Label = Label(self._root, justify=LEFT, text="Datum pocetka radova (dd/mm/gggg):", font="Times 15")
        pocetak_Label.grid(row=0, sticky=W, column=0, pady=10)

        self._datum_pocetka_radova = ttk.Entry(self._root)
        self._datum_pocetka_radova.grid(row=0, column=1, sticky=W)

        kraj_Label = Label(self._root, justify=LEFT, text="Datum zavrsetka radova (dd/mm/gggg)", font="Times 15")
        kraj_Label.grid(row=1, column=0, sticky=W, pady=10)

        self._datum_zavrsetka_radova = ttk.Entry(self._root)
        self._datum_zavrsetka_radova.grid(row=1, column=1)

    def izaberi_opremu(self):
        Label(self._frame.scrollable_frame, text="Izaberite opremu", font="Console 15").grid(row=3, column=0, pady=10)
        self.ispisi_mogucu_opremu_i_kolicinu()
        self._frame.grid(row=3, column=0)
        ttk.Button(self._root, text="Potvrdi", command=self.dodaj_opremu).grid(row=1, column=2, padx=10)

    def ispisi_mogucu_opremu_i_kolicinu(self):
        red = 4
        for oprema in self._oprema_za_prikaz:
            Label(self._frame.scrollable_frame, text=oprema.naziv_opreme, font="Times 12").grid(row=red, column=0,
                                                                                                sticky=W, pady=2)
            unet_broj_opreme = ttk.Entry(self._frame.scrollable_frame, width=10)
            unet_broj_opreme.insert(INSERT, "0")
            unet_broj_opreme.grid(row=red, column=1, sticky=W, pady=2)

            max_tekst = "max: " + str(oprema.broj_slobodne_opreme)
            Label(self._frame.scrollable_frame, text=max_tekst, font="Times 10").grid(row=red, column=2, sticky=W,
                                                                                      pady=2)
            self._naziv_broj_odabrane_opreme[oprema.naziv_opreme] = [unet_broj_opreme, oprema.broj_slobodne_opreme]
            red += 1

    def dodaj_opremu(self):
        if self.proveri_unos():
            lista_opreme = []
            for naziv, broj_opreme in self._naziv_broj_odabrane_opreme.items():
                if int(broj_opreme[0].get()) == 0:
                    continue

                prostorijaDTO = PremestanjeOpremeDTO(self._datum_pocetka, self._datum_zavrsetka, self._prostorija,
                                                     naziv, broj_opreme[0].get())
                lista_opreme.append(prostorijaDTO)
            self.provera_zauzeca(lista_opreme)

    def provera_zauzeca(self, lista_opreme):
        if not lista_opreme:
            messagebox.showerror('GRESKA', 'Niste odabrali opremu za premestanje!')
        elif not funkcija_za_premestanje[self._tip_premestanja](lista_opreme):
            messagebox.showerror("GRESKA", "Prostorija je zauzeta u tom periodu")
        else:
            messagebox.showinfo("USPESNO", "Podneli ste zahtev za renoviranje prostorije")
            self._root.destroy()

    def proveri_unos(self):
        if not self.provera_datuma():
            messagebox.showerror("GRESKA", "Los format datuma!")
            return False
        if not self.provera_unosa_opreme():
            return False
        return True

    def provera_unosa_opreme(self):
        for naziv, broj_opreme in self._naziv_broj_odabrane_opreme.items():
            if not broj_opreme[0].get():
                messagebox.showerror("GRESKA", "Popunite sva polja!")
                return False
            unet_broj_opreme, max_broj_opreme = int(broj_opreme[0].get()), broj_opreme[1]
            if unet_broj_opreme > max_broj_opreme or unet_broj_opreme < 0:
                messagebox.showerror("GRESKA", "Lose unet broj opreme!")
                return False
        return True

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
