from repository.korisnik.korisnikRepo1 import KorisnikRepository
from repository.oprema.oprema_repository import OpremaRepository
from repository.prostorije.prostorije_repository import ProstorijeRepository
from repository.unos_anamneze.unos_anamneze_repository import UnosAnamnezeRepository

INDEX_ULOGE_KORISNIKA = 2


class KreiranjeObjekata:

    @staticmethod
    def ucitaj_entitete():
        KorisnikRepository.ucitavanje_korisnika()
        OpremaRepository.ucitavanje_bolnicke_opreme()
        UnosAnamnezeRepository.ucitavanje_unosa_anamneze()
        # KreiranjeObjekata.ucitavanje_anamneze()
        ProstorijeRepository.ucitavanje_prostorije()

    @staticmethod
    def sacuvaj_entitete():
        KorisnikRepository.sacuvaj_korisnike()
        # KreiranjeObjekata.__sacuvaj_anamnezu()
        OpremaRepository.sacuvaj_bolnicku_opremu()
        ProstorijeRepository.sacuvaj_prostorije()
        UnosAnamnezeRepository.sacuvaj_unos_anamneze()


    # @staticmethod
    # def __sacuvaj_anamnezu():
    #     path = Path(PATH_TO_ANAMNEZA)
    #     with path.open('w', newline='') as file:
    #         writer = csv.writer(file, delimiter=',')
    #         for anamneza in lista_ucitanih_anamneza:
    #             unosi_anamneza = '|'.join(anamneza.get_spisak_pojedinacnih_unosa())  # spisak u string
    #             writer.writerow([anamneza.get_pacijent(), unosi_anamneza])


# zbog testiranja se ovde poziva, posle treba obrisati jer se poziva u login.py
KreiranjeObjekata.ucitaj_entitete()
