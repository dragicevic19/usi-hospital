from model.dto.unos_anamneze_dto import UnosAnamnezeDTO
from servis.unos_anamneze.unos_anamneze_servis import UnosAnamnezeServis
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
        Label(self._root2, text="DODAJ ANAMNEZU PACIJENTU", font="Arial 12 bold").pack(pady=5)
        self.polje_za_unos_anamneze = Text(self._root2, height=8, width=50)
        self.polje_za_unos_anamneze.pack(padx=20, pady=20)
        Button(self._root2, text="UNESI", width=50, command=self._unesi_anamnezu).pack(pady=20)

    def _unesi_anamnezu(self):
        unos_anamneze_dto = UnosAnamnezeDTO(self._lekar, self.polje_za_unos_anamneze.get("1.0", "end-1c")
                                            .replace("\n", " "), self._pacijent)
        UnosAnamnezeServis().dodaj_anamnezu_svuda(unos_anamneze_dto)
        messagebox.showinfo("USPESNO", "Uspesno ste dodali novu anamnezu.")
        self._root2.destroy()
