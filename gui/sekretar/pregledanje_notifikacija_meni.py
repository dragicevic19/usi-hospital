from tkinter import ttk
from tkinter import *

from gui.sekretar.prikaz_resavanje_notifikacija import prikaz_notifikacija
from model.enum.tip_notifikacije import TipNotifikacije


class PregledanjeNotifikacijaMeni(object):

    def __init__(self, root):
        self._root = root
        self.postavi_meni()

    def postavi_meni(self):
        ttk.Button(self._root, text="RENOVIRANJE",
                   command=lambda: prikaz_notifikacija(TipNotifikacije.RENOVIRANJE)).pack(ipady=20, ipadx=150, pady=15)

        ttk.Button(self._root, text="ZAHTEVI ZA PREGLED",
                   command=lambda: prikaz_notifikacija(TipNotifikacije.ZAHTEV_ZA_PREGLED)).pack(ipady=20, ipadx=125,
                                                                                                pady=15)
        ttk.Button(self._root, text="HITNE OPERACIJE",
                   command=lambda: prikaz_notifikacija(TipNotifikacije.HITNA_OPERACIJA)).pack(ipady=20, ipadx=140,
                                                                                              pady=15)


def poziv_forme_pregledanje_notifikacija_meni(root):
    application = PregledanjeNotifikacijaMeni(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('425x315')
    poziv_forme_pregledanje_notifikacija_meni(root)
