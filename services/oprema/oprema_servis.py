from services.file.file_servis import FileService
from model.bolnickaOprema import BolnickaOprema
from repository.prostorije.prostorije_repozitorijum import lista_ucitanih_prostorija
from repository.oprema.oprema_repozitorijum import OpremaRepository, lista_ucitane_bolnicke_opreme


class OpremaService(object):

    @staticmethod
    def dodaj_postojecu_opremu(oprema, kolicina, opis):
        oprema._ukupan_broj_opreme += int(kolicina)
        oprema._slobodna_oprema += int(kolicina)
        oprema._opis += ' ' + opis
        OpremaRepository.sacuvaj_bolnicku_opremu()

    @staticmethod
    def dodaj_opremu_nova(naziv, opis, kolicina):
        oprema = BolnickaOprema(naziv, int(kolicina), int(kolicina), opis)
        OpremaRepository.dodaj_opremu(oprema)

    @staticmethod
    def azuriraj_opremu(selektovan_naziv, naziv, opis, kolicina):
        oprema = OpremaRepository.nadji_po_nazivu_opreme(selektovan_naziv)
        oprema._naziv_opreme = naziv
        oprema._opis = opis
        zauzeta_oprema = int(oprema._ukupan_broj_opreme) - int(oprema._slobodna_oprema)
        oprema._slobodna_oprema = kolicina
        oprema._ukupan_broj_opreme = int(zauzeta_oprema) + int(kolicina)
        OpremaRepository.sacuvaj_bolnicku_opremu()

    @staticmethod
    def obrisi_opremu(naziv_opreme):
        oprema = OpremaRepository.nadji_po_nazivu_opreme(naziv_opreme)
        OpremaRepository.brisanje_opreme(oprema)

    @staticmethod
    def obrisi_opremu_iz_prostorija(naziv_opreme):
         OpremaRepository.brisanje_opreme_iz_prostorija(naziv_opreme)