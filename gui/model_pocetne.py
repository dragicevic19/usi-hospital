from tkinter import *
from tkinter import ttk

# KONSTANTE
SIRINA_BIO = 550
VISINA_ZA_DUGMICE = 120
ODVAJANJE_RADNOG = 100
SLIKA_DIMENZIJE = 400
BOJA = "#282828"

class ModelPocetne:

    def __init__(self, root, korisnik):
        self._root = root
        self._korisnik = korisnik
        self._root.title(self._korisnik.get_uloga())

        self.sirina = self._root.winfo_screenwidth()
        self.visina = self._root.winfo_screenheight()

        self.__promena_punog_ekrana()

        self.__pozovi_sve_za_init()

    def __pozovi_sve_za_init(self):
        self.__kreiraj_frejm_za_bio()
        self.__kreiranje_frejma_za_dugmice()
        self.kreiranje_frejma_za_izvrsavanje()
        self.__postavljanje_log_out_dugmeta()
        self.__postava_slike()
        self.__postava_bio()

       # self.__oboj_frejmove_sareno(True)

    def __oboj_frejmove_sareno(self, jednobojno=True):
        if jednobojno == False:
            self._root.configure(bg="blue")
            self._frejm_bio.configure(bg="purple")
            self._frejm_dugmici.configure(bg="yellow")
            self._okvir_izvrsavanja.configure(bg="green")
        else:
            self._root.configure(bg=BOJA)
            self._frejm_bio.configure(bg=BOJA)
            self._frejm_dugmici.configure(bg=BOJA)
            self._okvir_izvrsavanja.configure(bg=BOJA)

    def __kreiraj_frejm_za_bio(self):  # kreiraj skroz levi frejm za licne podatke
        self._frejm_bio = Frame(self._root)
        self._frejm_bio.place(x=0, y=0, width=SIRINA_BIO, height=self.visina)

    def __kreiranje_frejma_za_dugmice(self):
        self._frejm_dugmici = Frame(self._root)
        self._frejm_dugmici.place(x=SIRINA_BIO, y=self.visina - VISINA_ZA_DUGMICE, width=self.sirina - SIRINA_BIO,
                                  height=VISINA_ZA_DUGMICE)

    def kreiranje_frejma_za_izvrsavanje(self):
        self._okvir_izvrsavanja = Frame(self._root)
        self._okvir_izvrsavanja.place(x=SIRINA_BIO + ODVAJANJE_RADNOG, y=ODVAJANJE_RADNOG,
                                      height=self.visina - (ODVAJANJE_RADNOG + VISINA_ZA_DUGMICE),
                                      width=self.sirina - (SIRINA_BIO + ODVAJANJE_RADNOG))


    def __postavljanje_log_out_dugmeta(self):
        print(self._frejm_dugmici.winfo_screenwidth())
        log_out = ttk.Button(self._frejm_dugmici, text="LOG OUT", command=self.__akcija_log_out)
        log_out.place(x=self.sirina - SIRINA_BIO - 170, y=20, height=80, width=150)

    def __akcija_log_out(self):
        self._root.destroy()

    def __postava_bio(self):
        l_kor_ime = ttk.Label(self._frejm_bio, text="KORISNICKO IME:", font='Helvetica 14 bold')
        l_kor_ime.grid(row=1, column=0, pady=15, padx=15, sticky=W)

        l_uloga = ttk.Label(self._frejm_bio, text="ULOGA:", font='Helvetica 14 bold')
        l_uloga.grid(row=2, column=0, pady=15, padx=15, sticky=W)

        l_ime = ttk.Label(self._frejm_bio, text="IME:", font='Helvetica 14 bold')
        l_ime.grid(row=3, column=0, pady=15, padx=15, sticky=W)

        l_prezime = ttk.Label(self._frejm_bio, text="PREZIME:", font='Helvetica 14 bold')
        l_prezime.grid(row=4, column=0, pady=15, padx=15, sticky=W)

        self.__popuni_bio()

    def __popuni_bio(self):
        d_kor_ime = ttk.Label(self._frejm_bio, text=self._korisnik.get_korisnicko_ime(), font='Helvetica 12 bold')
        d_kor_ime.grid(row=1, column=0, pady=15, padx=15, sticky=E)

        d_uloga = ttk.Label(self._frejm_bio, text=self._korisnik.get_uloga(), font='Helvetica 12 bold')
        d_uloga.grid(row=2, column=0, pady=15, padx=15, sticky=E)

        d_ime = ttk.Label(self._frejm_bio, text=self._korisnik.get_ime(), font='Helvetica 12 bold')
        d_ime.grid(row=3, column=0, pady=15, padx=15, sticky=E)

        d_prezime = ttk.Label(self._frejm_bio, text=self._korisnik.get_prezime(), font='Helvetica 12 bold')
        d_prezime.grid(row=4, column=0, pady=15, padx=15, sticky=E)

    def __postava_slike(self):
        platno = Frame(self._frejm_bio, width=SLIKA_DIMENZIJE, height=SLIKA_DIMENZIJE, background='red')

        platno.grid(row=0, column=0, padx=75, pady=75)
        # Label(platno,text = "PROSTOR ZA SLIKU",font = "Helvetica 20 bold").grid(row=0, column=0, padx=100, pady=200)

    def __promena_punog_ekrana(self):
        self._root.attributes('-fullscreen', True)
        self._root.bind("<Escape>", self.__izlaz_iz_full_screena)
        self._root.bind("<F1>", self.__ulaz_u_full_screena)

    def __izlaz_iz_full_screena(self, event):
        self.__izlaz_iz_full_screena = False
        self._root.attributes("-fullscreen", self.__izlaz_iz_full_screena)

    def __ulaz_u_full_screena(self, event):
        self.__izlaz_iz_full_screena = True
        self._root.attributes("-fullscreen", self.__izlaz_iz_full_screena)


# if __name__ == '__main__':
#     root = Tk()
#     root.geometry('400x190')
#
#     nes = ModelPocetne(root, lista_ucitanih_korisnika[0])
#     root.mainloop()
