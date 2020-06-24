from tkinter import *
from gui.model_pocetne import ModelPocetne
from tkinter import ttk
from gui.pacijent.pregled_anamneze import poziv_forme_pregled_anamneze
from gui.pacijent.pregled_rasporeda_pregleda import poziv_prikaza_pregleda
from gui.pacijent.zakazivanje_pregleda import poziv_forme_zakazivanje_pregleda


class PocetnaFormaPacijent(ModelPocetne):

    def __init__(self, root, korisnik):
        super().__init__(root, korisnik)
        self.postavljanje_dugmica()

    def postavljanje_dugmica(self):
        b1 = ttk.Button(self._frejm_dugmici, text="Zakazivanje pregleda",
                        command=self.pokretanje_zakazivanja_pregleda)
        b1.place(x=10, y=10, height=60, width=200)

        b2 = ttk.Button(self._frejm_dugmici, text="Menjanje termina",
                        command=self.pokretanje_menjanje_termina)
        b2.place(x=270, y=10, height=60, width=200)

        b3 = ttk.Button(self._frejm_dugmici, text="Pregled anamneze", command=self.pokretanje_pregleda_anamneze)
        b3.place(x=530, y=10, height=60, width=200)

        b4 = ttk.Button(self._frejm_dugmici, text="Pregled rasporeda pregleda", command=self.pokretanje_rasporeda_pregleda)
        b4.place(x=790, y=10, height=60, width=200)

    def priprema_akcije(self):
        self._okvir_izvrsavanja.destroy()
        super().kreiranje_frejma_za_izvrsavanje()

    def pokretanje_zakazivanja_pregleda(self):
        self.priprema_akcije()
        poziv_forme_zakazivanje_pregleda(self._okvir_izvrsavanja)


    def pokretanje_menjanje_termina(self):
        self.priprema_akcije()
        pass

    def pokretanje_pregleda_anamneze(self):
        self.priprema_akcije()
        poziv_forme_pregled_anamneze(self._okvir_izvrsavanja,self._korisnik)

    def pokretanje_rasporeda_pregleda(self):
        self.priprema_akcije()
        poziv_prikaza_pregleda(self._okvir_izvrsavanja,self._korisnik)



def poziv_forme_pacijent(korisnik):
    root = Tk()
    PocetnaFormaPacijent(root, korisnik)
    root.mainloop()


if __name__ == '__main__':
    poziv_forme_pacijent()
