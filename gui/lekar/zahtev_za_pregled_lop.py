from model.dto.dogadjaji_dto.zakazivanje_pregleda_kod_spec_dto import ZakazivanjePregledaKodSpecijalisteDTO
from servis.kalendar.kalendar_servis import KalendarServis
from servis.korisnik.korisnik_servis import KorisnikServis
from model.enum.tip_lekara import TipLekara
from tkinter import ttk, messagebox
from tkinter import *
import datetime


class ZahtevZaPregledKodSpecijaliste:

    def __init__(self, root, pacijent):
        self._root = root
        self._root.title('Zakazivanje pregleda za ' + pacijent)
        self._pacijent = pacijent

        self._specijalista = StringVar(self._root)
        self._lista_specijalista = KorisnikServis().vrati_lekare_specijaliste_ili_lop(TipLekara.SPECIJALISTA)
        self._specijalista.set(self._lista_specijalista[0])
        self._pocetni_datum = ttk.Entry(self._root)
        self._krajnji_datum = ttk.Entry(self._root)

        self._vreme_pocetka = ttk.Entry(self._root)
        self._vreme_zavrsetka = ttk.Entry(self._root)

        self.izaberi_pocetni_krajnji_datum()
        self.izaberi_specijalistu()
        ttk.Button(self._root, text="Potvrdi", command=self.provera_unosa).grid(row=5, column=1, sticky=E, padx=10,
                                                                                pady=20)

    def izaberi_pocetni_krajnji_datum(self):
        Label(self._root, text='Pregled treba da se odrzi\nu sledecem vremenskom periodu:', font='Console 11').grid(
            row=0, column=0, sticky=W, pady=10, padx=10)
        Label(self._root, text='OD (dd/mm/gggg): ').grid(row=1, column=0, sticky=E, pady=5)
        self._pocetni_datum.grid(row=1, column=1, sticky=W)

        Label(self._root, text='DO (dd/mm/gggg): ').grid(row=2, column=0, sticky=E)
        self._krajnji_datum.grid(row=2, column=1, sticky=W)

    def izaberi_specijalistu(self):
        Label(self._root, justify=LEFT, text="Specijalista:", font="Console 11").grid(row=3, sticky=W, column=0,
                                                                                      pady=10, padx=10)
        default = self._specijalista.get()
        specijalista_OptionMenu = ttk.OptionMenu(self._root, self._specijalista, default, *self._lista_specijalista)
        specijalista_OptionMenu.grid(row=3, column=1, pady=10)

    def provera_unosa(self):
        if not self.provera_datuma():
            messagebox.showerror("GRESKA", "Los format datuma! (DD/MM/GGGG")
        else:
            self.salji_notifikaciju_sekretaru()

    def provera_datuma(self):
        try:
            d, m, g = self._pocetni_datum.get().split("/")
            self._datum_pocetka = datetime.date(int(g), int(m), int(d))
            d, m, g = self._krajnji_datum.get().split("/")
            self._datum_zavrsetka = datetime.date(int(g), int(m), int(d))
            if self._datum_pocetka < datetime.date.today() or self._datum_zavrsetka < self._datum_pocetka:
                return False
        except ValueError:
            return False
        return True

    def salji_notifikaciju_sekretaru(self):
        zakazivanjeDTO = ZakazivanjePregledaKodSpecijalisteDTO(self._datum_pocetka, self._datum_zavrsetka,
                                                               self._specijalista.get(), self._pacijent)
        KalendarServis().posalji_zahtev_za_pregled_kod_specijaliste(zakazivanjeDTO)
        messagebox.showinfo('USPESNO', 'Uspesno ste zakazali operaciju')
        self._root.destroy()


def poziv_forme_zahtev_za_pregled_lop(korisnicko_ime_pacijenta):
    root = Tk()
    root.geometry('550x240')
    application = ZahtevZaPregledKodSpecijaliste(root, korisnicko_ime_pacijenta)
    root.mainloop()
