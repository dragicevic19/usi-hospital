from tkinter import *
from repository.kalendar.kalendar_repozitorijum import vremenski_slotovi
from services.kalendar.kalendar_servis import KalendarServis


class Tabela_vremenskih_slotova():

    def __init__(self, root, lista_zauzeca):
        self._root = root
        self._lista_zauzeca = lista_zauzeca
        self._root.title("Vremenski slotovi zauzeca")
        self.prikaz_slotova()


    def prikaz_slotova(self):
        height = 7
        width = 7
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                pozadina = "green"
                trenutno_vreme = vremenski_slotovi[i * 7 + j]
                if trenutno_vreme in self._lista_zauzeca:
                    pozadina = "red"
                b = Label(self._root, text=trenutno_vreme, bg=pozadina, font="Italic 19", borderwidth=2, relief="groove")
                b.grid(row=i, column=j)

        Tk.mainloop(self._root)


if __name__ == '__main__':
    root = Tk()
    lista = KalendarServis.vrati_zauzeca_datum_soba("6/1/2020", "3", "301")
    Tabela_vremenskih_slotova(root, lista)

