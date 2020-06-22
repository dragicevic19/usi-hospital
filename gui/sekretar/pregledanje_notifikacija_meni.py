from tkinter import ttk
from tkinter import *

from gui.sekretar.notifikacije_za_hitne_operacije import notifikacije_za_hitne_operacije
from gui.sekretar.notifikacije_za_renoviranje import notifikacije_za_renoviranje
from gui.sekretar.notifikacije_za_zahteve_za_pregled import notifikacije_za_zahteve_za_pregled

tip_notifikacije = {0: notifikacije_za_renoviranje,
                    1: notifikacije_za_zahteve_za_pregled,
                    2: notifikacije_za_hitne_operacije
                    }


class PregledanjeNotifikacijaMeni(object):

    def __init__(self, root):
        self._root = root
        self._root.title('Pregledanje notifikacija - MENI')
        self.postavi_meni()

    def postavi_meni(self):
        ttk.Button(self._root, text="RENOVIRANJE", command=tip_notifikacije[0]()).pack(ipady=20, ipadx=150, pady=15)
        ttk.Button(self._root, text="ZAHTEVI ZA PREGLED", command=tip_notifikacije[1]()).pack(ipady=20, ipadx=125,
                                                                                              pady=15)
        ttk.Button(self._root, text="HITNE OPERACIJE", command=tip_notifikacije[2]()).pack(ipady=20, ipadx=140, pady=15)


def poziv_forme_pregledanje_notifikacija_meni(root):
    application = PregledanjeNotifikacijaMeni(root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('425x315')
    poziv_forme_pregledanje_notifikacija_meni(root)
