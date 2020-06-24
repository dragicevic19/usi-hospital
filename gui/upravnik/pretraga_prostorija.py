from tkinter import *
from gui.prikaz_entiteta.prikaz_prostorija import PrikazProstorija
from model.dto.prenos_prostorija_dto import PretragaProstorijaDTO
from tkinter.ttk import Combobox
from tkinter import messagebox
from model.konstante.konstante import REGEX_VREME, REGEX_DATUM
from servis.prostorije.zauzeca_prostorija_servis import ZauzecaProstorijaServis
from servis.oprema.oprema_servis import OpremaServis


class PretragaProstorija:

    def __init__(self, root):
        self._root = root
        self.lista_zahtevane_opreme = []
        self.napravi_frejmove()

        self.grupisi_vreme_od()
        self.grupisi_vreme_do()
        self.postava()

    def napravi_frejmove(self):
        self.frejm_za_vremena = Frame(self._root)
        self.frejm_za_vremena.place(x=0, y=0, width=450, height=250)

        self.drugi_frejm = Frame(self._root)
        self.drugi_frejm.place(x=0, y=250, width=200, height=500)

        self.treci_frejm = Frame(self._root)
        self.treci_frejm.place(x=200, y=250, width=200, height=500)

        self.cetvrti_frejm = Frame(self._root)
        self.cetvrti_frejm.place(x=100, y=500, width=200, height=500)

    def postava(self):
        v = OpremaServis().vrati_svu_opremu_u_sistemu()
        self.combo = Combobox(self.drugi_frejm, state='readonly', values=v, width=14)
        self.combo.grid(row=2, column=2, padx=20, pady=20)

        dugme = Button(self.drugi_frejm, text="DODAJ OPREMU", command=self.print_vrednost_comba)
        dugme.grid(row=1, column=2, padx=20, pady=20)

        self.label = Label(self.treci_frejm, text="Izabrana oprema \n za pretragu").grid(row=0, column=0, padx=20)
        self.prikaz = Listbox(self.treci_frejm)

        dugme = Button(self.cetvrti_frejm, text="PRETRAZI", command=self.pretraga)
        dugme.grid(row=0, column=2, padx=20, pady=20)

    def grupisi_vreme_od(self):
        self.grupa1 = LabelFrame(self.frejm_za_vremena, text="Vreme od", padx=10, pady=20)
        self.grupa1.grid(row=2, column=1)

        Label(self.grupa1, text="Datum").grid(row=0, column=1)
        Label(self.grupa1, text="Vreme").grid(row=0, column=2)
        self.datumOd = Entry(self.grupa1)
        self.datumOd.grid(row=1, column=1, padx=20)
        self.vremeOd = Entry(self.grupa1)
        self.vremeOd.grid(row=1, column=2, padx=20)

    def grupisi_vreme_do(self):
        self.grupa2 = LabelFrame(self.frejm_za_vremena, text="Vreme do", padx=10, pady=20)
        self.grupa2.grid(row=3, column=1)

        Label(self.grupa2, text="Datum").grid(row=0, column=1)
        Label(self.grupa2, text="Vreme").grid(row=0, column=2)
        self.datumDo = Entry(self.grupa2)
        self.datumDo.grid(row=1, column=1, padx=20)
        self.vremeDo = Entry(self.grupa2)
        self.vremeDo.grid(row=1, column=2, padx=20)

    def provera_unosa_vremena(self):
        if not REGEX_VREME.match(self.vremeOd.get()):
            messagebox.showerror("GRESKA", "Neispravan unos vremena.Oblik unos treba biti ss:mm")
            return False
        if not REGEX_VREME.match(self.vremeDo.get()):
            messagebox.showerror("GRESKA", "Neispravan unos vremena.Oblik unos treba biti ss:mm")
            return False
        if not REGEX_DATUM.match(self.datumOd.get()):
            messagebox.showerror("GRESKA", "Neispravan unos datuma.Oblik unosa treba biti dd/mm/gggg")
            return False
        if not REGEX_DATUM.match(self.datumDo.get()):
            messagebox.showerror("GRESKA", "Neispravan unos datuma.Obrlk unosa treba biti dd/mm/gggg")
            return False
        return True

    def pretraga(self):
        if self.provera_unosa_vremena():
            paket_za_prenos = PretragaProstorijaDTO(self.lista_zahtevane_opreme, self.datumOd.get(), self.vremeOd.get(),
                                                    self.datumDo.get(), self.vremeDo.get(), True)
            lista = ZauzecaProstorijaServis().zauzece_prostorije_od_do(paket_za_prenos)
            novi_root = Tk()
            PrikazProstorija(novi_root, lista)

    def print_vrednost_comba(self):
        vrednost = self.combo.get()

        if vrednost == "":
            messagebox.showinfo("Prazno", "Izaberite opremu.")
        else:
            if vrednost not in self.lista_zahtevane_opreme:
                self.lista_zahtevane_opreme.append(vrednost)
                self.prikaz.insert(1, vrednost)
                self.prikaz.grid(row=1, column=0, padx=2)
            else:
                messagebox.showinfo("Unos", "Parametar koji ste uneli vec je dodat u listu zahtevanih")


def poziv_forma_za_pretragu_prostorija(root):
    a = PretragaProstorija(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x570")
    poziv_forma_za_pretragu_prostorija(root)
