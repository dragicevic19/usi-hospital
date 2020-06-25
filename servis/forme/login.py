


class LoginServis():
    def __init__(self,korisnik_servis):
        self._korisnik_servis =korisnik_servis


    def provera_unosa(self,k_ime, lozinka):
        lista_korisnika = self._korisnik_servis.dobavi_sve_korisnike_u_sistemu()
        for korisnik in lista_korisnika:
            if (
                    korisnik.get_korisnicko_ime() == k_ime and korisnik.get_lozinka() == lozinka):
                return korisnik  # sledecoj formi moraju se proslediti informacije
        return None
