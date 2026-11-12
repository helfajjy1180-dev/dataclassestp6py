
from dataclasses import dataclass, asdict, replace
import json


@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    # Conversion en JSON
    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    # Promotion
    def promo(self, prix_reduit):
        return replace(self, prix=prix_reduit)

    # Chargement depuis JSON
    @staticmethod
    def from_json(texte):
        data = json.loads(texte)
        return Livre(**data)

    # Comparaison selon le prix
    def __lt__(self, autre):
        return self.prix < autre.prix
