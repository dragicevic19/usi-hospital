import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model.kreiranje_objekata_entiteta import KreiranjeObjekata
from model.kreiranje_objekata_entiteta import lista_ucitanih_korisnika
from model.korisnik import Korisnik


class AzuriraniKorisnik:

    korisnicka_imena = [i.get_korisnicko_ime() for i in lista_ucitanih_korisnika]

    def __init__(self, root2, selektovan_korisnik):

        self._root2 = root2
        self._selektovan_korisnik = selektovan_korisnik
        self._korisnicko_ime = None
        self._lozinka = None
        self._ime = None
        self._prezime = None

        self._root2.title("Podaci o korisniku")
        self.unesi_novo_korisnicko_ime()
        self.unesi_novu_lozinku()
        self.unesi_novo_ime()
        self.unesi_novo_prezime()

        ttk.Button(self._root2, text="POTVRDI",
                   command=self.provera_unetih_podataka).grid(row=6, column=2, pady=10)

    def insert_korisnicko_ime(self):

        for korisnik in lista_ucitanih_korisnika:
            if korisnik.get_korisnicko_ime() == self._selektovan_korisnik:
                return korisnik.get_korisnicko_ime()

    def insert_lozinka(self):

        for korisnik in lista_ucitanih_korisnika:
            if korisnik.get_korisnicko_ime() == self._selektovan_korisnik:
                return korisnik.get_lozinka()

    def insert_ime(self):

        for korisnik in lista_ucitanih_korisnika:
            if korisnik.get_korisnicko_ime() == self._selektovan_korisnik:
                return korisnik.get_ime()

    def insert_prezime(self):

        for korisnik in lista_ucitanih_korisnika:
            if korisnik.get_korisnicko_ime() == self._selektovan_korisnik:
                return korisnik.get_prezime()

    def unesi_novo_korisnicko_ime(self):

        Label(self._root2, justify=LEFT, text="Korisnicko ime:", font="Times 15").grid(row=2, column=1, pady=10)
        self._korisnicko_ime = ttk.Entry(self._root2)
        self._korisnicko_ime.insert(0, self.insert_korisnicko_ime())
        self._korisnicko_ime.grid(row=2, column=2, columnspan=10)

    def unesi_novu_lozinku(self):

        Label(self._root2, justify=LEFT, text="Lozinka:", font="Times 15").grid(row=3, column=1, pady=10)
        self._lozinka = ttk.Entry(self._root2)
        self._lozinka.insert(0, self.insert_lozinka())
        self._lozinka.grid(row=3, column=2, columnspan=10)

    def unesi_novo_ime(self):

        Label(self._root2, justify=LEFT, text="Ime:", font="Times 15").grid(row=4, column=1, pady=10)
        self._ime = ttk.Entry(self._root2)
        self._ime.insert(0, self.insert_ime())
        self._ime.grid(row=4, column=2, columnspan=10)

    def unesi_novo_prezime(self):

        Label(self._root2, justify=LEFT, text="Prezime:", font="Times 15").grid(row=5, column=1, pady=10)
        self._prezime = ttk.Entry(self._root2)
        self._prezime.insert(0, self.insert_prezime())
        self._prezime.grid(row=5, column=2, columnspan=10)

    def provera_unetih_podataka(self):

        if not self._korisnicko_ime.get() or not self._lozinka.get() or not self._ime.get()\
                or not self._prezime.get():

            messagebox.showerror("GRESKA", "Neispravan unos.")

        if KreiranjeObjekata.postoji_korisnik(self._korisnicko_ime.get()):

            if self._selektovan_korisnik != self._korisnicko_ime.get():

                messagebox.showerror("GRESKA", "Korisnik sa unetim korisnickim imenom vec postoji")

            else:
                self.azuriraj_korisnika()

        else:
            self.azuriraj_korisnika()

    def azuriraj_korisnika(self):

        for korisnik in lista_ucitanih_korisnika:

            if korisnik.get_korisnicko_ime() == self._selektovan_korisnik:

                korisnik.set_korisnicko_ime(self._korisnicko_ime.get())
                korisnik.set_lozinka(self._lozinka.get())
                korisnik.set_ime(self._ime.get())
                korisnik.set_prezime(self._prezime.get())

                messagebox.showinfo("USPESNO", "Uspesno ste azurirali korisnika")
                self._root2.destroy()
                global root1
                root1.destroy()



def double_click(event):

    item_id = event.widget.focus()
    item = event.widget.item(item_id)
    values = item['values']
    selektovan_korisnik = values[0]
    pokretanje_unosa_podataka(selektovan_korisnik)


def pokretanje_tabele(root1):

    #root1 = Tk()
    #root1.title("Azuriranje korisnika")

    tabela = ttk.Treeview(root1,columns=(1, 2, 3, 4), show="headings", height=15)
    tabela["columns"] = ("korisnicko ime", "uloga", "ime", "prezime")
    return tabela


def kreiranje_kolona(tabela):

    tabela.column("korisnicko ime", width=200)
    tabela.column("uloga", width=200)
    tabela.column("ime", width=200)
    tabela.column("prezime", width=200)


def kreiranje_headinga(tabela):

    tabela.heading("korisnicko ime", text="Korisnicko ime")
    tabela.heading("uloga", text="Uloga")
    tabela.heading("ime", text="Ime")
    tabela.heading("prezime", text="Prezime")
    selektovan_korisnik = tabela.bind("<Double-Button-1>", double_click)
    return selektovan_korisnik


def popunjavanje_tabele(root1, tabela):

    for korisnik in lista_ucitanih_korisnika:
        tabela.insert("", "end", text="Korisnik", values=(korisnik.get_korisnicko_ime(), korisnik.get_uloga(),
                                                          korisnik.get_ime(), korisnik.get_prezime()))
    tabela.grid()
    root1.mainloop()


def pokretanje_unosa_podataka(selektovan_korisnik):

    root2 = Tk()
    root2.geometry('330x250')
    application = AzuriraniKorisnik(root2, selektovan_korisnik)
    root2.mainloop()


global root1
def poziv_forme_azuriranje_korisnika(root2):
    global root1
    root1 = root2
    tabela = pokretanje_tabele(root1)
    kreiranje_kolona(tabela)
    kreiranje_headinga(tabela)
    popunjavanje_tabele(root1, tabela)


if __name__ == '__main__':
    root1 = Tk()
    poziv_forme_azuriranje_korisnika(root1)