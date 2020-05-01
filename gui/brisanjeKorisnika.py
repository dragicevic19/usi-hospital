from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model.kreiranje_objekata_entiteta import lista_ucitanih_korisnika, KreiranjeObjekata, lista_obrisanih_korisnika


class BrisanjeKorisnika:

    def __init__(self, root):
        self._root = root
       # self._root.title('Brisanje korisnika')

        self.treeview = ttk.Treeview(self._root)
        self.scroll = ttk.Scrollbar(self._root, orient='vertical', command=self.treeview.yview)
        self.scroll.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scroll.set)

        self.izlistaj_korisnike()

    def izlistaj_korisnike(self):
        self.napravi_treeview()
        potvrdi_dugme = ttk.Button(self._root, text="OBRISI", command=self.obrisi_korisnika)
        potvrdi_dugme.pack(fill='x')

    def napravi_treeview(self):
        self.treeview["columns"] = ["korisnicko_ime", "uloga", "ime", "prezime"]
        self.treeview["show"] = "headings"
        self.treeview.heading("korisnicko_ime", text="Korisnicko ime")
        self.treeview.heading("uloga", text="Uloga")
        self.treeview.heading("ime", text="Ime")
        self.treeview.heading("prezime", text="Prezime")
        self.treeview.pack()
        self.treeview.config(height=13)
        self.__popuni_treeview()

    def __popuni_treeview(self):
        index = iid = 0
        for korisnik in lista_ucitanih_korisnika:
            k = (korisnik.get_korisnicko_ime(), korisnik.get_uloga(), korisnik.get_ime(), korisnik.get_prezime())
            self.treeview.insert("", index, iid, values=k)
            index = iid = index + 1

    def obrisi_korisnika(self):
        try:
            odabrani = self.treeview.focus()
            odabrani_korisnik = self.treeview.item(odabrani)['values']
            korisnicko_ime_odabranog = odabrani_korisnik[0]

            korisnik = KreiranjeObjekata.postoji_korisnik(korisnicko_ime_odabranog)
            korisnik.set_obrisan('True')
            lista_ucitanih_korisnika.remove(korisnik)
            lista_obrisanih_korisnika.append(korisnik)
            messagebox.showinfo("USPESNO", "Uspesno ste obrisali korisnika!")
            KreiranjeObjekata.sacuvaj_entitete()
            self._root.destroy()


        except IndexError:
            messagebox.showerror("GRESKA", "Niste odabrali korisnika!")


def poziv_forme_brisanje_korisnika(root):
    #root = Tk()
    application = BrisanjeKorisnika(root)
    root.mainloop()

if __name__ == '__main__':
    root = Tk()
    poziv_forme_brisanje_korisnika(root)
