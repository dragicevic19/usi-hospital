from tkinter import *
from gui.model_pocetne import ModelPocetne


class PocetnaFormaLekar(ModelPocetne):

    def __init__(self, root, korisnik):
        super().__init__(root, korisnik)


def poziv_forme_lekar(korisnik):
    root = Tk()
    PocetnaFormaLekar(root, korisnik)

    root.mainloop()


if __name__ == '__main__':
    poziv_forme_lekar()
