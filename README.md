Clean watch api
# Statut
⚠️ L'API est actuellement en cours de construction. Pour l'instant, elle propose uniquement des films.

L'api a été conçue pour répertorier des films et des séries sans contenu explicite, permettant ainsi une expérience de visionnage adaptée à tous.

## Tag `explicit_flag`
Le tag `explicit_flag` indique le type de contenu dans les films et séries :

`None` : Pas de contenu explicite.

`Moderate` : Pas de contenu explicite, mais peut avoir des images ou paroles suggestives.

### Exemples d'utilisation

**Récupérer les détails d'un film spécifique**

**Requête :**
```http request
GET {{base_url}}/api/v1/film/1
```
**Réponse :**

```json
{
  "id": "1",
  "title": "Hugo Cabret",
  "description": "Dans la gare...",
  "duration": "2h 6m",
  "release_year": "14/12/2011",
  "explicit_flag": "None",
  "poster": "https://res.cloudinary...",
  "trailer_id": "RWK_LMPljDhoN-Ui",
  "budget": "$170,000,000.00",
  "revenue": "$185,770,160.00",
  "original_language": "anglais",
  "categories": [
    {
      "id": "1",
      "name": "Drame"
    },
    {
      "id": "2",
      "name": "Aventure"
    },
    {
      "id": "3",
      "name": "Familial"
    }
  ],
  "directors": [
    {
      "id": "1",
      "name": "Martin Scorsese",
      "image": "https://res.cloudinary..."
    }
  ],
  "streaming": [
    {
      "id": "1",
      "name": "FilmBox+",
      "link": "https://filmbox...",
    },
    {
      "id": "2",
      "name": "https://tv.apple..."
    }
  ]
}
```
**Lister tous les films**

**Requête :**
```http request
GET {{base_url}}/api/v1/films
```
**Réponse :**

```js
[
  {
    "id": "1",
    "title": "Hugo Cabret",
    "explicit_flag": "None",
    "poster": "https://res.cloudinary..."
  },
  // {...}
]
```