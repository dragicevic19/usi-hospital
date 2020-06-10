import datetime
from tkinter import *
from tkinter import ttk, messagebox

from model.DTO.slobodna_oprema_DTO import SlobodnaOpremaDTO
from repository.oprema.oprema_repozitorijum import lista_ucitane_bolnicke_opreme
from repository.prostorije.prostorije_repozitorijum import ProstorijeRepository, lista_ucitanih_prostorija
from services.prostorije.prostorije_servis import ProstorijeService


class DodavanjeOpremeUProstoriju:

    def __init__(self, root, selektovana_prostorija):
        self._root = root
        self._prostorija = selektovana_prostorija
        self._datum_pocetka_radova = None
        self._datum_zavrsetka_radova = None
        self._oprema_za_dodavanje = []
        self.pronadji_opremu_za_dodavanje()
        self._oprema = StringVar(self._root)
        self._oprema.set(self._oprema_za_dodavanje[0])

        self.izaberi_datum()
        self.izaberi_opremu()
        ttk.Button(self._root, text="Potvrdi", command=self.dodaj_opremu)

    def pronadji_opremu_za_dodavanje(self):
        for oprema in lista_ucitane_bolnicke_opreme:
            if int(oprema.get_slobodna_oprema()) > 0:
                slobodna_opremaDTO = SlobodnaOpremaDTO(oprema.get_naziv_opreme(), int(oprema.get_slobodna_oprema()))
                self._oprema_za_dodavanje.append(slobodna_opremaDTO)
        if not self._oprema_za_dodavanje:
            messagebox.showinfo("UPOZORENJE", "Trenutno nema slobodne opreme!")
            self._root.destroy()

    def izaberi_datum(self):
        Label(self._root, justify=LEFT, text="Datum pocetka radova (dd/mm/gggg):", font="Times 15").grid(row=0,
                                                                                                         column=0,
                                                                                                         pady=10)
        self._datum_pocetka_radova = ttk.Entry(self._root)
        self._datum_pocetka_radova.grid(row=0, column=1)

        Label(self._root, justify=LEFT, text="Datum pocetka radova (dd/mm/gggg)", font="Times 15").grid(row=1, column=0,
                                                                                                        pady=10)
        self._datum_zavrsetka_radova = ttk.Entry(self._root)
        self._datum_zavrsetka_radova.grid(row=1, column=1)

    def izaberi_opremu(self):
        Label(self._root, text="Izaberite opremu", font="Console 15").grid(row=3, column=0, pady=10)
        red = 4
        self.recnik_za_entry = {}
        for oprema in self._oprema_za_dodavanje:
            Label(self._root, text=oprema.naziv_opreme, font="Times 12").grid(row=red, column=0, pady=2)

            unet_broj_opreme = ttk.Entry(self._root, width=10)
            unet_broj_opreme.insert(INSERT, "0")
            unet_broj_opreme.grid(row=red, column=1, pady=2, padx=1)

            max_tekst = "max: " + str(oprema.broj_slobodne_opreme)
            Label(self._root, text=max_tekst, font="Times 10").grid(row=red, column=2, pady=2, padx=1)
            self.recnik_za_entry[oprema.naziv_opreme] = [unet_broj_opreme, oprema.broj_slobodne_opreme]
            red += 1

    def dodaj_opremu(self):
        if self.proveri_unos():
            '''
            TODO: Servisu treba da se prosledi datum pocetka i zavrsetka radova, u kojoj prostoriji se radi,
                  naziv opreme, i broj opreme koji se dodaje.
            '''
            ProstorijeService.dodavanje_slobodne_opreme_u_prostoriju(self.recnik_za_entry)

    def proveri_unos(self):
        if not self.provera_datuma():
            return False

        for kljuc in self.recnik_za_entry:
            if self.recnik_za_entry[kljuc][0] > self.recnik_za_entry[kljuc][1]:
                return False
        return True

    def provera_datuma(self):
        try:
            d, m, g = self._datum_pocetka_radova.get().split("/")
            self._datum_pocetka = datetime.date(int(g), int(m), int(d))
            d, m, g = self._datum_zavrsetka_radova.get().split("/")
            self._datum_zavrsetka = datetime.date(int(g), int(m), int(d))
            if self._datum_pocetka < datetime.date.today() or self._datum_zavrsetka < self._datum_pocetka:
                # TODO: ako je prostorija zauzeta u tom terminu isto false
                return False
        except ValueError:
            return False
        return True


def dodavanje_opreme(selektovana_prostorija):
    root = Tk()
    root.geometry('800x600')
    application = DodavanjeOpremeUProstoriju(root, selektovana_prostorija)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    ProstorijeRepository.ucitavanje_prostorije()
    prostorija = lista_ucitanih_prostorija[0]
    application = DodavanjeOpremeUProstoriju(root, prostorija)
    root.mainloop()
