import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

odabrani_datum = None


class PrikazKalendara:

    def __init__(self, root):
        self.root = root
        self._datum = None
        self.napravi_kalendar()

    def napravi_kalendar(self):
        # self.root.withdraw()  # hide naff extra window
        # self.root.title('Izaberite datum')
        self.odaberi_datum()
        self.root.mainloop()

    def get_datum(self):
        return self._datum

    def odaberi_datum(self):
        # self.top = tk.Toplevel(self.root)

        self._kalendar = Calendar(self.root,
                            font="Arial 10", background='darkblue',
                            foreground='white', selectmode='day')

        self._kalendar.grid()
        ttk.Button(self.root, text="OK", command=self.print_sel).grid()

    def print_sel(self):
        self._datum = self._kalendar.get_date()
        # self.top.destroy()
        # self.root.destroy()


if __name__ == '__main__':
    forma = tk.Tk()
    a = PrikazKalendara(forma)
    print(a._datum)
    forma.mainloop()
