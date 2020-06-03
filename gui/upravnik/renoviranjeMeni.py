import tkinter as tk
import tkinter.ttk as ttk
from gui.upravnik.renoviranje.renoviranjeProstorije import poziv_forme_odabir_prostorije
from model.enum.renoviranje import TipRenoviranja

""" 



REFAKTORISATI NA KRAJU INIT I VP START GUI





"""


def init(top, gui):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = RenoviranjeMeni(root)
    init(root, top)
    root.mainloop()


w = None


def poziv_forme_za_renovaciju_prostorije(rt):
    '''Starting point when module is imported by another module.
       Correct form of call: 'napravi_meni(root)'.'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    meni = RenoviranjeMeni(w)
    init(w, meni)
    return w, meni


class RenoviranjeMeni:
    def __init__(self, top=None):
        font = "-family {Segoe UI} -size 12 -weight bold"
        self.style = ttk.Style()

        top.geometry("600x450+718+234")
        top.resizable(0, 0)
        top.title("Renoviranje prostorije")
        top.configure(background="#d9d9d9", highlightcolor="#646464646464")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.083, rely=0.044, height=35, width=498)
        self.Label1.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font, foreground="#000000")
        self.Label1.configure(text='''RENOVIRANJE PROSTORIJE''')

        self.TButton0 = ttk.Button(top)
        self.TButton0.place(relx=0.083, rely=0.133, height=59, width=498)
        self.TButton0.configure(text='''Izmena namena prostorije''',
                                command=lambda: poziv_forme_odabir_prostorije(TipRenoviranja.IZMENA_NAMENE))

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.083, rely=0.311, height=59, width=498)
        self.TButton1.configure(text='''Premestanje opreme kojom prostorija raspolaze''',
                                command=lambda: poziv_forme_odabir_prostorije(TipRenoviranja.PREMESTANJE_OPREME))

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.083, rely=0.489, height=59, width=498)
        self.TButton2.configure(text='''Deljenje prostorija''',
                                command=lambda: poziv_forme_odabir_prostorije(TipRenoviranja.DELJENJE_PROSTORIJE))

        self.TButton3 = ttk.Button(top)
        self.TButton3.place(relx=0.083, rely=0.667, height=59, width=498)
        self.TButton3.configure(text='''Spajanje prostorija''',
                                command=lambda: poziv_forme_odabir_prostorije(TipRenoviranja.SPAJANJE_PROSTORIJA))

        self.TButton4 = ttk.Button(top)
        self.TButton4.place(relx=0.083, rely=0.844, height=59, width=498)
        self.TButton4.configure(text='''Ostale renovacije''',
                                command=lambda: poziv_forme_odabir_prostorije(TipRenoviranja.OSTALE_RENOVACIJE))


if __name__ == '__main__':
    vp_start_gui()
