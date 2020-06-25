from model.dto.dogadjaji_dto.zakazivanje_operacija_pregled_dto import ZakazivanjeOperacijaPregledDTO
from model.enum.namena_prostorije import NamenaProstorije
from model.enum.tip_zahvata import TipZahvata
from model.enum.uloga import Uloga
from servis.korisnik.korisnik_servis import KorisnikServis
from model.enum.tip_lekara import TipLekara
from tkinter import ttk, messagebox
from tkinter import *
import datetime
from model.konstante.konstante import *
from model.dto.dogadjaji_dto.zakazivanje_dto import *
from servis.prostorije.prostorije_servis import ProstorijeServis


class ZakazivanjePregleda(object):

    def __init__(self, root, korisnik):
        self._root = root
        self._ulogovani_pacijent = korisnik
        self._lekar_opste_prakse = StringVar(self._root)
        self._lista_lekara_opste_prakse = KorisnikServis().vrati_lekare_specijaliste_ili_lop(TipLekara.LOP)
        self._lekar_opste_prakse.set(self._lista_lekara_opste_prakse[0])
        self._najkasniji_datum = ttk.Entry(self._root)
        self._radio_parametar = IntVar()

        self.izaberi_lop()
        self.izaberi_najkasniji_datum()
        self.preferirani_slotovi()
        self.izbor_najveceg_prioriteta()
        ttk.Button(self._root, text="POTVRDI", command=self.potvrda, width=20).grid(row=7, column=3, sticky=E,
                                                                                    padx=10, pady=20)

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
        self.pref_slot_pocetni = ttk.Entry(self._root)
        self.pref_slot_pocetni.grid(row=2, column=1, sticky=E, padx=10, pady=20)
        self.pref_slot_krajnji = ttk.Entry(self._root)
        self.pref_slot_krajnji.grid(row=2, column=2, sticky=E, padx=10, pady=20)

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

    def potvrda(self):
        if self.provera_unosa():
            paket_za_prenos = ZakazivanjeDTO(self._lekar_opste_prakse.get(), self._najkasniji_datum.get(),
                                             self.pref_slot_pocetni.get(), self.pref_slot_krajnji.get(),
                                             self._radio_parametar.get())
            self._datum, self._vreme = KorisnikServis().zakazivanje_pregleda_pacijent(paket_za_prenos)
            if self._datum:
                self._napravi_dogadjaj()
                messagebox.showinfo("Zakazano", "Zakazan je pregled dana: " + self._datum + ", u: " + self._vreme)
            else:
                messagebox.showerror("Greska", "Doslo je do greske u sistemu pokusajte kasnije")

    def _napravi_dogadjaj(self):
        d, m, g = self._datum.split('/')
        datum = datetime.date(int(g), int(m), int(d))
        s, m = self._vreme.split(':')
        vreme = datetime.datetime(100, 1, 1, int(s), int(m))
        vreme_zavrsetka = vreme + datetime.timedelta(minutes=30)
        lekar, lop = str(self._lekar_opste_prakse.get()).split('|')

        for prostorija in ProstorijeServis().pronadji_prostorije_po_nameni(NamenaProstorije.SALA_ZA_PREGLEDE.value):
            zakazivanjeDTO = ZakazivanjeOperacijaPregledDTO(datum, str(vreme.time())[:5],
                                                            str(vreme_zavrsetka.time())[:5],
                                                            lekar.strip(),
                                                            self._ulogovani_pacijent.get_korisnicko_ime(),
                                                            prostorija, TipZahvata.PREGLED.value)
            if ProstorijeServis.zakazivanje_operacije_i_pregleda(zakazivanjeDTO):
                return

    def provera_unosa(self):
        if not self.provera_datuma():
            messagebox.showerror("GRESKA", "Los format datuma! (DD/MM/GGGG)")
            return False
        elif not REGEX_VREME.match(self.pref_slot_pocetni.get()) or not REGEX_VREME.match(self.pref_slot_krajnji.get()):
            messagebox.showerror("GRESKA", "Neispravan unos vremena.Oblik unos treba biti ss:mm")
            return False
        return True

    def provera_datuma(self):
        try:
            d, m, g = self._najkasniji_datum.get().split("/")
            self._krajnji_datum = datetime.date(int(g), int(m), int(d))

            if self._krajnji_datum <= datetime.date.today():
                return False
        except ValueError:
            return False
        return True


def poziv_forme_zakazivanje_pregleda(root, korisnik):
    ZakazivanjePregleda(root, korisnik)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    korisnik = KorisnikServis().vrati_sve_korisnike_po_ulozi(Uloga.PACIJENT.name)[0]
    poziv_forme_zakazivanje_pregleda(root, korisnik)
