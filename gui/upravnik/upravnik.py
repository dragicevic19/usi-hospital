from tkinter import *
from tkinter import ttk
from gui.ModelPocetne import ModelPocetne


class PocetnaFormaUpravnik(ModelPocetne):

    def __init__(self, root, korisnik):
        super().__init__(root, korisnik)


def poziv_forme_upravnik(korisnik):
    root = Tk()
    kreni = PocetnaFormaUpravnik(root, korisnik)
    root.mainloop()


if __name__ == '__main__':
    poziv_forme_upravnik()
