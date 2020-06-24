from tkinter import *
from gui.model_pocetne import ModelPocetne
from tkinter import ttk
from gui.sekretar.registracija_pacijenata import poziv_forme_unos_korisnika
from gui.sekretar.pregledanje_notifikacija_meni import poziv_forme_pregledanje_notifikacija_meni
from gui.sekretar.zakazivanje_operacija_i_pregleda import zakazivanje_operacija_i_pregleda


class PocetnaFormaSekretar(ModelPocetne):

    def __init__(self, root, korisnik):
        super().__init__(root, korisnik)
        self.postavljanje_dugmica()

    def postavljanje_dugmica(self):
        b1 = ttk.Button(self._frejm_dugmici, text="Pregledanje notifikacija", command=self.pokretanje_pregledanja_notifikacija)
        b1.place(x=10, y=10, height=60, width=200)

        b2 = ttk.Button(self._frejm_dugmici, text="Registracija pacijenata",
                        command=self.pokretanje_registracije)
        b2.place(x=270, y=10, height=60, width=200)

        b3 = ttk.Button(self._frejm_dugmici, text="Zakazivanje operacija \n i pregleda", command=self.pokretanje_zakazivanja)
        b3.place(x=530, y=10, height=60, width=200)

        b4 = ttk.Button(self._frejm_dugmici, text="Otkazivanje termina", command=self.poziv_otkazivanja_termina)
        b4.place(x=790, y=10, height=60, width=200)

    def priprema_akcije(self):
        self._okvir_izvrsavanja.destroy()
        super().kreiranje_frejma_za_izvrsavanje()

    def pokretanje_pregledanja_notifikacija(self):
        self.priprema_akcije()
        poziv_forme_pregledanje_notifikacija_meni(self._okvir_izvrsavanja)


    def pokretanje_registracije(self):
        self.priprema_akcije()
        poziv_forme_unos_korisnika(self._okvir_izvrsavanja)


    def pokretanje_zakazivanja(self):
        self.priprema_akcije()
        zakazivanje_operacija_i_pregleda(self._okvir_izvrsavanja)

    def poziv_otkazivanja_termina(self):
        self.priprema_akcije()
        pass



def poziv_forme_sekretar(korisnik):
    root = Tk()
    PocetnaFormaSekretar(root, korisnik)
    root.mainloop()


if __name__ == '__main__':
    poziv_forme_sekretar()
