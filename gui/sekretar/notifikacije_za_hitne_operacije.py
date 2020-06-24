from tkinter import ttk

from gui.prikaz_entiteta.prikaz_notifikacija import PrikazNotifikacija
from model.enum.tip_notifikacije import TipNotifikacije


class NotifikacijeZaHitneOperacije(PrikazNotifikacija):

    def __init__(self, root):
        self._root = root
        super().__init__(self._root, TipNotifikacije.HITNA_OPERACIJA)
        ttk.Button(self._root)


def notifikacije_za_hitne_operacije():
    pass
