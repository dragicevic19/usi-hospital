from tkinter import *
from repozitorijum.kalendar.kalendar_repozitorijum import vremenski_slotovi
from servis.kalendar.kalendar_servis import KalendarServis


class Tabela_vremenskih_slotova():

    def __init__(self, root, lista_zauzeca):
        self._root = root
        self._lista_zauzeca = lista_zauzeca
        self._root.title("Vremenski slotovi zauzeca")
        self.prikaz_slotova()

    def prikaz_slotova(self):
        VISINA = 7
        SIRINA = 7
        for i in range(VISINA):  # REDOVI
            for j in range(SIRINA):  # KOLONE
                pozadina = "green"
                trenutno_vreme = vremenski_slotovi[i * 7 + j]
                if trenutno_vreme in self._lista_zauzeca:
                    pozadina = "red"
                b = Label(self._root, text=trenutno_vreme, bg=pozadina, font="Italic 19", borderwidth=2,
                          relief="groove")
                b.grid(row=i, column=j)

        Tk.mainloop(self._root)


if __name__ == '__main__':
    root = Tk()
    lista = KalendarServis.vrati_zauzeca_datum_soba("4/6/2020", "1", "109")
    Tabela_vremenskih_slotova(root, lista)
