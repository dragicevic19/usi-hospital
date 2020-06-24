from repozitorijum.unos_anamneze.interfejs_unos_anamneze_repozitorijum import InterfejsUnosAnamnezeRepo
from repozitorijum.korisnik.korisnik_repozitorijum import KorisnikRepozitorijumImpl
from datetime import datetime
from pathlib import Path
from model.konstante.konstante import *
from model.unos_anamneze import UnosAnamneze
import csv


class UnosAnamnezeRepozitorijumImpl(InterfejsUnosAnamnezeRepo):

    def __init__(self):
        self._mapa_ucitanih_unosa_anamneza = {}
        self._id_sledece_anamneze = 0
        self.ucitavanje_unosa_anamneze()

    def ucitavanje_unosa_anamneze(self):
        path = Path(PUTANJA_FAJL_UNOS_ANAMNEZE)
        with path.open('r') as file:
            reader = csv.reader(file)
            for red in reader:
                unos_anamneze = UnosAnamneze(*red)
                self._mapa_ucitanih_unosa_anamneza[red[0]] = unos_anamneze

    def sacuvaj_unos_anamneze(self):
        path = Path(PUTANJA_FAJL_UNOS_ANAMNEZE)
        with path.open('w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for kljuc in self._mapa_ucitanih_unosa_anamneza:    # for kljuc, vrednost in ... .items():
                unos = self._mapa_ucitanih_unosa_anamneza[kljuc]
                writer.writerow([unos.get_id(), unos.get_lekar(), unos.get_opis(), unos.get_datum_i_vreme()])

    def generisi_id_anamneze(self):
        for kljuc in self._mapa_ucitanih_unosa_anamneza:
            if int(kljuc) > self._id_sledece_anamneze:
                self._id_sledece_anamneze = int(kljuc)
        self._id_sledece_anamneze += 1

    def pronadji_anamnezu_za_pacijenta(self, ulogovan_pacijent):
        lista_anamneza_po_pacijentu = []
        for kljuc in self._mapa_ucitanih_unosa_anamneza:
            unos = self._mapa_ucitanih_unosa_anamneza[kljuc]
            if unos.get_id() in ulogovan_pacijent.get_anamneza():
                lista_anamneza_po_pacijentu.append(unos)
        return lista_anamneza_po_pacijentu

    def sacuvaj_anamnezu(self, unos_anamneze_dto):
        self.generisi_id_anamneze()
        datum = datetime.now().strftime("%d-%m-%Y %H:%M")
        anamneza = UnosAnamneze(self._id_sledece_anamneze, unos_anamneze_dto.lekar, unos_anamneze_dto.anamneza, datum)
        self._mapa_ucitanih_unosa_anamneza[str(id)] = anamneza
        KorisnikRepozitorijumImpl().dodaj_id_anamneze_pacijentu(unos_anamneze_dto.pacijent, str(self._id_sledece_anamneze))
        self.sacuvaj_unos_anamneze()
