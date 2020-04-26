from tkinter import *
from tkinter import ttk

class LogIn:
    kor_ime = "admin"
    loz = "admin"

    def __init__(self, root):
        self._root = root
        self._root.title("LOGIN SCREEN")

        Label(text="Korisnicko ime:", font="Times 15").grid(row=1, column=1, pady=20)
        self.korisnicko_ime = Entry()
        self.korisnicko_ime.grid(row=1, column=2, columnspan=10)

        Label(text="Lozinka:", font="Times 15").grid(row=2, column=1, pady=20)
        self.lozinka = Entry(show="*")
        self.lozinka.grid(row=2, column=2, columnspan=10)

        ttk.Button(text="LOGIN", command=self.log_korisnik).grid(row=3, column=2)

    def log_korisnik(self):

        self.message = Label(text="               ")
        self.message.grid(row=6, column=2)

        if self.korisnicko_ime.get() == self.kor_ime and self.lozinka.get() == self.loz:

            self.message = Label(text="Uspeo")
            self.message.grid(row=6, column=2)


        else:

            self.message = Label(text="Pogresno")
            self.message.grid(row=6, column=2)


if __name__ == '__main__':
    root = Tk()
    root.geometry('425x425')
    application = LogIn(root)
    root.mainloop()

