# Système de Gestion de Bibliothèque Multimédia

Ce projet est une application Python permettant de gérer une collection de médias (livres, albums, films) avec persistance des données via MongoDB.

## Fonctionnalités

- Ajout, suppression et recherche de différents types de médias
- Prise en charge de trois types de médias : livres, albums et films
- Persistance des données dans une base de données MongoDB
- Interface en ligne de commande pour interagir avec la bibliothèque

## Structure du Projet

Le projet est organisé autour d'un système de classes hiérarchique :

- `Media` : Classe abstraite de base pour tous les types de médias
- `Book` : Classe pour représenter les livres
- `Album` : Classe pour représenter les albums de musique
- `Track` : Classe pour représenter les pistes d'un album
- `Movie` : Classe pour représenter les films
- `Library` : Classe pour gérer la collection de médias

## Prérequis

- Python 3.x
- PyMongo (`pip install pymongo`)
- MongoDB (installé et exécuté localement sur le port 27017)

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/votre-utilisateur/bibliotheque-multimedia.git
   cd bibliotheque-multimedia
   ```

2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

3. Assurez-vous que MongoDB est en cours d'exécution sur votre machine locale (port 27017).

## Utilisation

Pour lancer l'application :

```
python app.py
```

L'interface vous guidera ensuite avec plusieurs options :
1. Ajouter un média (livre, album ou film)
2. Supprimer un média 
3. Rechercher un média par mot-clé
4. Afficher tous les médias

## Exemples d'utilisation

### Ajouter un livre
```
Taper 1 pour ajouter un media
Taper 1 pour un livre
Titre : Les Misérables
Année de publication : 1862
Auteur : Victor Hugo
Éditeur : Albert Lacroix et Cie
Nombre de pages : 1900
```

### Rechercher un média
```
Taper 3 pour rechercher un media
Entrer un mot clé : Misérables
```

## Fonctionnalités Principales

### Persistance des données
Les données sont stockées dans MongoDB dans la base `projet_POO` et la collection `media`.

### Recherche
La recherche peut se faire par titre pour les livres et films, et également dans les titres des pistes pour les albums.

### Organisation
Les médias peuvent être triés par titre ou année de publication.

## Contribuer

1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez vos changements (`git commit -am 'Ajout d'une nouvelle fonctionnalité'`)
4. Pushez vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Créez une Pull Request

## Structure des Classes

### Classe Media (ABC)
Classe abstraite qui définit les attributs communs à tous les médias (titre, année de sortie, auteur).

### Classe Book
Représente un livre avec des attributs spécifiques comme l'éditeur et le nombre de pages.

### Classe Album
Représente un album de musique avec des attributs comme le genre, le label et les pistes.

### Classe Movie
Représente un film avec des attributs comme le producteur, le genre et la durée.

### Classe Library
Gère la collection de médias avec des méthodes pour ajouter, supprimer, rechercher et afficher les médias.

## Améliorations Futures

- Interface graphique
- Support pour d'autres types de médias (séries TV, podcasts, etc.)
- Système d'authentification des utilisateurs
- Fonctionnalités de notation et de critique des médias
- API RESTful pour accéder à la bibliothèque