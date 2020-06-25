from tkinter import *
from tkinter import ttk
from gui.model_pocetne import ModelPocetne
from gui.lekar.azuriranje_anamneze import poziv_forme_za_dodavanje_anamneze_odredjenom_pacijentu
from gui.lekar.pregled_zauzeca import poziv_forme_detaljni_prikaz_pacijenta
from model.enum.tip_lekara import *
from gui.lekar.biranje_pacijenta import poziv_forme_biranje_pacijenata_za_operaciju
from gui.lekar.generisanje_izvestaja import poziv_forme_za_izvestaj_lekara_sopstveni


class PocetnaFormaLekar(ModelPocetne):

    def __init__(self, root, korisnik):
        super().__init__(root, korisnik)
        self.postavljanje_dugmica()


    def postavljanje_dugmica(self):
        b1 = ttk.Button(self._frejm_dugmici, text="Azuriranje anameze", command=self.pokretanje_azuriranja_anamneze)
        b1.place(x=10, y=10, height=60, width=200)

        b2 = ttk.Button(self._frejm_dugmici, text="Pregled zauzeca i pacijenata", command=self.pokretanje_pregleda_zauzeca)
        b2.place(x=270, y=10, height=60, width=200)

        b3 = ttk.Button(self._frejm_dugmici, text="Zakazivanje", command=self.pokretanje_zakazivanja)
        b3.place(x=530, y=10, height=60, width=200)

        b4 = ttk.Button(self._frejm_dugmici, text="Generisanje izvestaja", command=self.pokretanje_forme_za_izvestaje)
        b4.place(x=790, y=10, height=60, width=200)

    def priprema_akcije(self):
        self._okvir_izvrsavanja.destroy()
        super().kreiranje_frejma_za_izvrsavanje()


    def pokretanje_azuriranja_anamneze(self):
        self.priprema_akcije()
        poziv_forme_za_dodavanje_anamneze_odredjenom_pacijentu(self._okvir_izvrsavanja,self._korisnik)


    def pokretanje_pregleda_zauzeca(self):
        self.priprema_akcije()
        poziv_forme_detaljni_prikaz_pacijenta(self._okvir_izvrsavanja,self._korisnik)

    def pokretanje_zakazivanja(self):
        self.priprema_akcije()
        if self._korisnik.get_spisak_specijalizacija() and self._korisnik.get_spisak_specijalizacija()[0] != TipLekara.LOP.value:
            poziv_forme_biranje_pacijenata_za_operaciju(self._okvir_izvrsavanja,self._korisnik)
        else:
            poziv_forme_biranje_pacijenata_za_operaciju(self._okvir_izvrsavanja)

    def pokretanje_forme_za_izvestaje(self):
        self.priprema_akcije()
        poziv_forme_za_izvestaj_lekara_sopstveni(self._okvir_izvrsavanja,self._korisnik)






def poziv_forme_lekar(korisnik):
    root = Tk()
    PocetnaFormaLekar(root, korisnik)

    root.mainloop()


if __name__ == '__main__':
    poziv_forme_lekar()
