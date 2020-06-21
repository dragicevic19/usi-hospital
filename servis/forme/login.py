from servis.korisnik.korisnik_servis import KorisnikServis


class LoginServis():

    @staticmethod
    def provera_unosa(k_ime, lozinka):
        lista_korisnika = KorisnikServis().dobavi_sve_korisnike_u_sistemu()
        for korisnik in lista_korisnika:
            if (
                    korisnik.get_korisnicko_ime() == k_ime and korisnik.get_lozinka() == lozinka):
                return korisnik  # sledecoj formi moraju se proslediti informacije
        return None
