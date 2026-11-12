import json
from dataclasses import asdict

from film import Film

# Création des films
film1 = Film("Inception", "Christopher Nolan", 2010, 8.8)
film2 = Film("Le Parrain", "Francis Ford Coppola", 1972, 9.2)
film3 = Film("Matrix", "Lana Wachowski, Lilly Wachowski", 1999, 8.7)


# Affichage JSON
print("JSON du film :")
print(film1.to_json())


# Vérifier si le film est classique
print("\nFilm classique ?")
print(film3.est_classique())


# Comparaison des films
print("\nComparaison des notes :")
print(film1 < film2)


# Chargement depuis JSON
texte = film1.to_json()
film4 = Film.from_json(texte)

print("\nFilm chargé :")
print(film4)


# Enregistrement dans un fichier JSON
films = [film1, film2, film3]

with open("films.json", "w", encoding="utf-8") as fichier:
    json.dump(
        [asdict(f) for f in films],
        fichier,
        ensure_ascii=False,
        indent=4
    )

print("\nFilms enregistrés avec succès !")


# Tri selon les notes
films_tries = sorted(films)

print("\nFilms triés par note :")
for f in films_tries:
    print(f.titre, f.note)
