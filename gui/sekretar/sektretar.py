from tkinter import *
from gui.model_pocetne import ModelPocetne
from tkinter import ttk
from gui.sekretar.registracija_pacijenata import poziv_forme_unos_korisnika


class PocetnaFormaSekretar(ModelPocetne):

    def __init__(self, root, korisnik):
        super().__init__(root, korisnik)
        self.postavljanje_dugmica()

    def postavljanje_dugmica(self):
        b1 = ttk.Button(self._frejm_dugmici, text="Pregledanje notifikacija", command=self.pokretanje_azuriranja_anamneze)
        b1.place(x=10, y=10, height=60, width=200)

        b2 = ttk.Button(self._frejm_dugmici, text="Registracija pacijenata",
                        command=self.pokretanje_pregleda_zauzeca)
        b2.place(x=270, y=10, height=60, width=200)

        b3 = ttk.Button(self._frejm_dugmici, text="Zakazivanje operacija \n i pregleda", command=self.akcija3)
        b3.place(x=530, y=10, height=60, width=200)

        b4 = ttk.Button(self._frejm_dugmici, text="Otkazivanje termina", command=self.akcija4)
        b4.place(x=790, y=10, height=60, width=200)

    def priprema_akcije(self):
        self._okvir_izvrsavanja.destroy()
        super().kreiranje_frejma_za_izvrsavanje()

    def pokretanje_azuriranja_anamneze(self):
        self.priprema_akcije()


    def pokretanje_pregleda_zauzeca(self):
        self.priprema_akcije()
        poziv_forme_unos_korisnika(self._okvir_izvrsavanja)


    def akcija3(self):
        self.priprema_akcije()

    def akcija4(self):
        self.priprema_akcije()



def poziv_forme_sekretar(korisnik):
    root = Tk()
    PocetnaFormaSekretar(root, korisnik)
    root.mainloop()


if __name__ == '__main__':
    poziv_forme_sekretar()
