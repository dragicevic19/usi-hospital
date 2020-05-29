import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

ROOT = tk.Tk()
ROOT.withdraw()  # hide naff extra window
ROOT.title('Please choose a date')


def print_sel(cal):
    selected_date = (cal.get_date())
    print(selected_date)


def pick_date_dialog():
    top = tk.Toplevel(ROOT)

    # defaults to today's date
    cal = Calendar(top,
                   font="Arial 10", background='darkblue',
                   foreground='white', selectmode='day')

    cal.grid()
    ttk.Button(top, text="OK", command=lambda: print_sel(cal)).grid()


pick_date_dialog()

ROOT.mainloop()


class PrikazKalendara:

    @staticmethod
    def print_sel(cal):
        selected_date = (cal.get_date())
        print(selected_date)

    @staticmethod
    def pick_date_dialog():
        top = tk.Toplevel(ROOT)

        cal = Calendar(top,
                       font="Arial 10", background='darkblue',
                       foreground='white', selectmode='day')

        cal.grid()
        cal.bind('<Double-1>', print_sel(cal))

        ttk.Button(top, text="OK", command=lambda: print_sel(cal)).grid()


pick_date_dialog()

ROOT.mainloop()
