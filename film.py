from dataclasses import dataclass, asdict, replace
import json

from livre import Livre
   
@dataclass(frozen=True, slots=True)
class film:
     titre: str
     realisateur: str
     annee: int
     note: float

def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

def est_classique(self):
        return self.annee < 2000

def __lt__(self, autre):
        return self.note < autre.note

    # Chargement depuis JSON
@staticmethod
def from_json(texte):
        data = json.loads(texte)
        return film(**data)


film1 = film("Inception", "Christopher Nolan", 2010, 8.8)
film2 = film("Le Parrain", "Francis Ford Coppola", 1972, 9.2)
film3 = film("Matrix", "Lana Wachowski, Lilly Wachowski", 1999, 8.7)

with open("films.json", "w", encoding="utf-8") as fichier:
    json.dump(
        [asdict(film) for film in [film1, film2, film3]],
        fichier,
        ensure_ascii=False,
        indent=4
    )