import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

selected_date = None


def print_sel(cal):
    global selected_date
    selected_date = (cal.get_date())
    print(selected_date)


def pick_date_dialog(ROOT):
    top = tk.Toplevel(ROOT)

    # defaults to today's date
    cal = Calendar(top,
                   font="Arial 10", background='darkblue',
                   foreground='white', selectmode='day')

    cal.grid()
    ttk.Button(top, text="OK", command=lambda: print_sel(cal)).grid()
    return selected_date


def poziv():
    ROOT = tk.Tk()
    ROOT.withdraw()  # hide naff extra window
    ROOT.title('Please choose a date')
    pick_date_dialog(ROOT)
    ROOT.mainloop()


if __name__ == '__main__':
    poziv()
#
# class PrikazKalendara:
#
#     def __init__(self):
#         self._datum = None
#         self.napiravi_kalendar()
#         self.pick_date_dialog()
#
#     def napiravi_kalendar(self):
#         self.root = tk.Tk()
#         self.root.withdraw()  # hide naff extra window
#         self.root.title('Izaberite datum')
#         self.root.mainloop()
#
#     def get_datum(self):
#         return self._datum
#
#     def pick_date_dialog(self):
#         top = tk.Toplevel(self.root)
#
#         self.cal = Calendar(top,
#                             font="Arial 10", background='darkblue',
#                             foreground='white', selectmode='day')
#
#         self.cal.grid()
#         ttk.Button(top, text="OK", command=lambda: self.print_sel(self.cal)).grid()
#
#     def print_sel(self, cal):
#         self._datum = (cal.get_date())


a = PrikazKalendara()
print(a.get_datum())
#
# class PrikazKalendara:
#
#     @staticmethod
#     def print_sel(cal):
#         selected_date = (cal.get_date())
#         print(selected_date)
#
#     @staticmethod
#     def pick_date_dialog():
#         top = tk.Toplevel(ROOT)
#
#         cal = Calendar(top,
#                        font="Arial 10", background='darkblue',
#                        foreground='white', selectmode='day')
#
#         cal.grid()
#         cal.bind('<Double-1>', print_sel(cal))
#
#         ttk.Button(top, text="OK", command=lambda: print_sel(cal)).grid()
#
#
# pick_date_dialog()
#
# ROOT.mainloop()
