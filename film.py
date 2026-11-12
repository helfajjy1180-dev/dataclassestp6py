
from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    # Conversion en JSON
    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    # Vérifier si le film est classique
    def est_classique(self):
        return self.annee >= 2000

    # Comparaison selon la note
    def __lt__(self, autre):
        return self.note < autre.note

    # Chargement depuis JSON
    @staticmethod
    def from_json(texte):
        data = json.loads(texte)
        return Film(**data)


