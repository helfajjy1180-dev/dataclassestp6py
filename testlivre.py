import json
from dataclasses import asdict
from livre import Livre

# Création des livres
livre1 = Livre("1984", "George Orwell", 1949, 9.90)
livre2 = Livre("L'Étranger", "Albert Camus", 1942, 7.50)

# Affichage JSON
print("JSON du livre :")
print(livre1.to_json())


# Promotion
livre3 = livre1.promo(5.90)

print("\nLivre après promotion :")
print(livre3)

# Chargement JSON
texte = livre1.to_json()
livre4 = Livre.from_json(texte)

print("\nLivre chargé depuis JSON :")
print(livre4)


# Comparaison
print("\nComparaison :")
print(livre1 < livre2)


# Tri
livres = [livre1, livre2, livre3]
livres_tries = sorted(livres)

print("\nLivres triés par prix :")
for livre in livres_tries:
    print(livre.titre, livre.prix)


# Enregistrement dans un fichier JSON
with open("livres.json", "w", encoding="utf-8") as fichier:
    json.dump(
        [asdict(livre) for livre in livres],
        fichier,
        ensure_ascii=False,
        indent=4
    )

print("\nLivres enregistrés avec succès !")
