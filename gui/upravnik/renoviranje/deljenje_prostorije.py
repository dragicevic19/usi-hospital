from tkinter import *


class DeljenjeProstorije:
    def __init__(self, root, prostorija):
        self._root = root
        self._root.title("Deljenje prostorije")
        self._prostorija = prostorija
        


def deljenje_prostorije(selektovana_prostorija):
    root = Tk()
    root.geometry('800x600')
    application = DeljenjeProstorije(root, selektovana_prostorija)
    root.mainloop()
