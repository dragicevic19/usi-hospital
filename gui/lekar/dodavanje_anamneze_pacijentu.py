from gui.pacijent.pregled_anamneze import PregledAnamneze
from tkinter import *


class DodavanjeAnamnezePacijentu(PregledAnamneze):

    def __init__(self, ulogovani_pacijent):
        self._root2 = Tk()
        super().__init__(self._root2, ulogovani_pacijent)
        naslov = Label(self._root2, text="DODAJ ANAMNEZU PACIJENTU", font="Arial 12 bold").pack(pady=5)
        text = Text(self._root2, height=5).pack(padx=20, pady=20)
        dugme = Button(self._root2, text="UNESI", width=50, command=self._unesi_anamnezu).pack(pady=20)

    def _unesi_anamnezu(self):
        pass
