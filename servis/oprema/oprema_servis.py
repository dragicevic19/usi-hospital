from repozitorijum.oprema.oprema_repozitorijum_impl import OpremaRepozitorijumImpl
from model.bolnicka_oprema import BolnickaOprema
from repozitorijum.prostorije.prostorije_repozitorijum import ProstorijeRepozitorijumImpl


class OpremaServis(object):

    def __init__(self, repo_oprema=OpremaRepozitorijumImpl(), repo_prostorije=ProstorijeRepozitorijumImpl()):
        self.repo_oprema = repo_oprema
        self.repo_prostorije = repo_prostorije

    def dodaj_postojecu_opremu(self, oprema, kolicina, opis):
        oprema._ukupan_broj_opreme += int(kolicina)
        oprema._slobodna_oprema += int(kolicina)
        oprema._opis += ' ' + opis
        self.repo_oprema.sacuvaj_bolnicku_opremu()

    def dodaj_opremu_nova(self, naziv, opis, kolicina):
        oprema = BolnickaOprema(naziv, int(kolicina), int(kolicina), opis)
        self.repo_oprema.dodaj_opremu(oprema)

    def azuriraj_opremu(self, selektovan_naziv, naziv, opis, kolicina):
        oprema = self.repo_oprema.nadji_po_nazivu_opreme(selektovan_naziv)
        oprema._naziv_opreme = naziv
        oprema._opis = opis
        zauzeta_oprema = int(oprema._ukupan_broj_opreme) - int(oprema._slobodna_oprema)
        oprema._slobodna_oprema = kolicina
        oprema._ukupan_broj_opreme = int(zauzeta_oprema) + int(kolicina)
        self.repo_oprema.sacuvaj_bolnicku_opremu()

    def obrisi_opremu(self, naziv_opreme):
        oprema = self.repo_oprema.nadji_po_nazivu_opreme(naziv_opreme)
        self.repo_oprema.brisanje_opreme(oprema)

    def pronadji_opremu_po_nazivu(self, naziv_opreme):
        return self.repo_oprema.nadji_po_nazivu_opreme(naziv_opreme)

    def vrati_svu_opremu_u_sistemu(self):
        return self.repo_oprema.vrati_svu_opremu_u_sistemu()