from repozitorijum.korisnik.korisnik_repozitorijum import lista_ucitanih_korisnika


class LoginServis:

    @staticmethod
    def provera_unosa(k_ime, lozinka):
        for korisnik in lista_ucitanih_korisnika:
            if (
                    korisnik.get_korisnicko_ime() == k_ime and korisnik.get_lozinka() == lozinka):
                return korisnik  # sledecoj formi moraju se proslediti informacije
        return None
