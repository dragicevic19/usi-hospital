# from servis.file.file_servis import FileService
from model.bolnicka_oprema import BolnickaOprema
from repozitorijum.oprema.oprema_repozitorijum import OpremaRepozitorijum, lista_ucitane_bolnicke_opreme


class OpremaServis(object):

    @staticmethod
    def dodaj_postojecu_opremu(oprema, kolicina, opis):
        oprema._ukupan_broj_opreme += int(kolicina)
        oprema._slobodna_oprema += int(kolicina)
        oprema._opis += ' ' + opis
        OpremaRepozitorijum.sacuvaj_bolnicku_opremu()

    @staticmethod
    def dodaj_opremu_nova(naziv, opis, kolicina):
        oprema = BolnickaOprema(naziv, int(kolicina), int(kolicina), opis)
        OpremaRepozitorijum.dodaj_opremu(oprema)

    @staticmethod
    def azuriraj_opremu(selektovan_naziv, naziv, opis, kolicina):
        oprema = OpremaRepozitorijum.nadji_po_nazivu_opreme(selektovan_naziv)
        oprema._naziv_opreme = naziv
        oprema._opis = opis
        zauzeta_oprema = int(oprema._ukupan_broj_opreme) - int(oprema._slobodna_oprema)
        oprema._slobodna_oprema = kolicina
        oprema._ukupan_broj_opreme = int(zauzeta_oprema) + int(kolicina)
        OpremaRepozitorijum.sacuvaj_bolnicku_opremu()

    @staticmethod
    def obrisi_opremu(naziv_opreme):
        oprema = OpremaRepozitorijum.nadji_po_nazivu_opreme(naziv_opreme)
        OpremaRepozitorijum.brisanje_opreme(oprema)

    @staticmethod
    def obrisi_opremu_iz_prostorija(naziv_opreme):
        OpremaRepozitorijum.brisanje_opreme_iz_prostorija(naziv_opreme)

    @staticmethod
    def smanji_broj_slobodne_opreme(prostorija_za_izmenu):
        for oprema in lista_ucitane_bolnicke_opreme:
            if oprema._naziv_opreme == prostorija_za_izmenu.naziv_opreme:
                oprema._slobodna_oprema -= prostorija_za_izmenu.broj_opreme
        OpremaRepozitorijum.sacuvaj_bolnicku_opremu()

    @staticmethod
    def povecaj_broj_slobodne_opreme(naziv, broj_opreme):
        for oprema in lista_ucitane_bolnicke_opreme:
            if oprema._naziv_opreme == naziv:
                oprema._slobodna_oprema += broj_opreme
        OpremaRepozitorijum.sacuvaj_bolnicku_opremu()
