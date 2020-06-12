from tkinter import messagebox

from gui.pacijent.pregled_anamneze import PregledAnamneze
from tkinter import *

from repository.korisnik.korisnik_repozitorijum import KorisnikRepository
from repository.unos_anamneze.unos_anamneze_repozitorijum import UnosAnamnezeRepository
from services.unos_anamneze.unos_anamneze_servis import UnosAnamnezeService


class DodavanjeAnamnezePacijentu(PregledAnamneze):

    def __init__(self, pacijent,lekar):
        self._root2 = Tk()
        self._root2.title("Anamneze pacijenta "+ pacijent.get_ime()+ " " + pacijent.get_prezime())
        self._lekar = lekar
        self._pacijent = pacijent
        super().__init__(self._root2, pacijent)
        self.textic = None
        naslov = Label(self._root2, text="DODAJ ANAMNEZU PACIJENTU", font="Arial 12 bold").pack(pady=5)
        self.textic = Text(self._root2, height=8 , width = 50)
        self.textic.pack(padx=20, pady=20)
        dugme = Button(self._root2, text="UNESI", width=50, command=self._unesi_anamnezu).pack(pady=20)


    def _unesi_anamnezu(self):
        UnosAnamnezeService.dodaj_anamnezu_svuda(self._lekar, self.textic.get(),self._pacijent)
        UnosAnamnezeRepository.sacuvaj_unos_anamneze()
        KorisnikRepository.sacuvaj_korisnike()
        messagebox.showinfo("USPESNO","Uspesno ste dodali novu anamnezu.")
        self._root2.destroy()
