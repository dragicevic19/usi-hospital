from repozitorijum.korisnik.korisnik_repozitorijum import KorisnikRepozitorijum
from repozitorijum.unos_anamneze.unos_anamneze_repozitorijum import UnosAnamnezeRepozitorijum
from servis.unos_anamneze.unos_anamneze_servis import UnosAnamnezeService
from gui.pacijent.pregled_anamneze import PregledAnamneze
from tkinter import messagebox
from tkinter import *


class DodavanjeAnamnezePacijentu(PregledAnamneze):

    def __init__(self, pacijent, lekar):
        self._root2 = Tk()
        self._root2.title("Anamneze pacijenta " + pacijent.get_ime() + " " + pacijent.get_prezime())
        self._lekar = lekar
        self._pacijent = pacijent
        super().__init__(self._root2, pacijent)
        self.polje_za_unos_anamneze = None
        naslov = Label(self._root2, text="DODAJ ANAMNEZU PACIJENTU", font="Arial 12 bold").pack(pady=5)
        self.polje_za_unos_anamneze = Text(self._root2, height=8, width=50)
        self.polje_za_unos_anamneze.pack(padx=20, pady=20)
        dugme_unos = Button(self._root2, text="UNESI", width=50, command=self._unesi_anamnezu).pack(pady=20)

    """
        izmeniti metodu dodaj anamnezu svuda / ne bismo trebali da koristimo ovde repozitorijum,
        vec da sve odradimo u metodi servisa tj. da u metodi dodaj anamnezu svuda odradimo i cuvanje korisnika
        
        vazi za sva mesta gde se ponavlja slican kod kao ovaj
    """

    def _unesi_anamnezu(self):
        UnosAnamnezeService.dodaj_anamnezu_svuda(self._lekar, self.polje_za_unos_anamneze.get(), self._pacijent)
        UnosAnamnezeRepozitorijum.sacuvaj_unos_anamneze()
        KorisnikRepozitorijum.sacuvaj_korisnike()
        messagebox.showinfo("USPESNO", "Uspesno ste dodali novu anamnezu.")
        self._root2.destroy()
