from enum import Enum


class TipRenoviranja(Enum):
    IZMENA_NAMENE = 1
    PREMESTANJE_OPREME = 2
    DELJENJE_PROSTORIJE = 3
    SPAJANJE_PROSTORIJA = 4
    OSTALE_RENOVACIJE = 5


class TipPremestanjaOpreme(Enum):
    DODAVANJE_OPREME = 1
    IZBACIVANJE_OPREME = 2
