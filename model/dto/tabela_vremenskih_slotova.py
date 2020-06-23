from tkinter import *
from servis.kalendar.kalendar_servis import KalendarServis


class TabelaVremenskihSlotovaDTO(object):

    def __init__(self, root):
        self._root = root
        self._root.title("Vremenski slotovi zauzeca")
        self.prikaz_slotova()

    def prikaz_slotova(self):
        VISINA = 7
        SIRINA = 7
        for i in range(VISINA):  # REDOVI
            for j in range(SIRINA):  # KOLONE
                vremenski_slotovi = KalendarServis().dobavi_vremenske_slotove()
                trenutno_vreme = vremenski_slotovi[i * 7 + j]
                pozadina = "green"

                b = Label(self._root, text=trenutno_vreme, bg=pozadina, font="Italic 19", borderwidth=2,
                          relief="groove")

                b.grid(row=i, column=j)
                b.bind("<Button-1>", self.promena_boje_kvadratica)

        Tk.mainloop(self._root)

    def promena_boje_kvadratica(self, kvadratic):
        kvadratic.widget.config(bg="yellow")


def poziv_tabele_vremenskih_slotova():
    root = Tk()
    TabelaVremenskihSlotovaDTO(root)
