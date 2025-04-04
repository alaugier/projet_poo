from abc import ABC, abstractmethod
import pymongo
from pymongo import MongoClient

class Media(ABC):
    """
    Classe abstraite servant de base pour tous les types de médias.
    
    Définit les attributs et méthodes communs à tous les médias.
    
    Attributes:
        title (str): Titre du média
        release_year (str): Année de sortie/publication
        author (str): Auteur/Créateur du média
    """
    def __init__(self, _title, _release_year, _author):
        """
        Initialise un objet média avec les attributs de base.
        
        Args:
            _title (str): Titre du média
            _release_year (str): Année de sortie/publication
            _author (str): Auteur/Créateur du média
        """
        self.title = _title
        self.release_year = _release_year
        self.author = _author
    
    @abstractmethod
    def display_info():
        """
        Méthode abstraite qui doit être implémentée par chaque sous-classe.
        
        Returns:
            dict: Dictionnaire contenant les informations du média
        """
        pass

    def to_dict(self):
        """
        Convertit les attributs de base en dictionnaire.
        
        Returns:
            dict: Dictionnaire avec les attributs de base du média
        """
        return {"title":self.title, "release year":self.release_year, "author":self.author}

class Book(Media):
    """
    Classe représentant un livre dans la bibliothèque.
    
    Hérite de la classe Media et ajoute des attributs spécifiques aux livres.
    
    Attributes:
        title (str): Titre du livre
        release_year (str): Année de publication
        author (str): Auteur du livre
        publisher (str): Éditeur du livre
        nb_of_pages (str): Nombre de pages
        dict_book (dict): Dictionnaire stockant les informations du livre
        num (int): Compteur pour l'itération
    """
    def __init__(self, _title, _release_year, _author, _publisher, _nb_of_pages):
        """
        Initialise un objet livre avec tous ses attributs.
        
        Args:
            _title (str): Titre du livre
            _release_year (str): Année de publication
            _author (str): Auteur du livre
            _publisher (str): Éditeur du livre
            _nb_of_pages (str): Nombre de pages
        """
        Media.__init__(self, _title, _release_year, _author)
        self.publisher = _publisher
        self.nb_of_pages = _nb_of_pages
        self.dict_book = {"title":_title,"release year":_release_year, "author":_author}
        self.num = 0
        
    def dict_update(self, d):
        """
        Met à jour le dictionnaire du livre avec de nouvelles données.
        
        Args:
            d (dict): Dictionnaire contenant les nouvelles données
        """
        self.dict_book.update(d)
        
    def __len__(self):
        """
        Renvoie la longueur du dictionnaire du livre.
        
        Returns:
            int: Nombre d'éléments dans le dictionnaire
        """
        return len(self.dict_book)
        
    def display_info(self):
        """
        Renvoie toutes les informations du livre sous forme de dictionnaire.
        
        Ajoute les attributs spécifiques au dictionnaire de base.
        
        Returns:
            dict: Dictionnaire avec toutes les informations du livre
        """
        self.dict_update({"publisher":self.publisher, "number of pages":self.nb_of_pages})
        return self.dict_book
        
    def __iter__(self):
        """
        Prépare l'itération sur les attributs du livre.
        
        Returns:
            Book: Instance de l'objet livre
        """
        return self
        
    def __next__(self):
        """
        Retourne le prochain élément lors de l'itération.
        
        Returns:
            dict: Paire clé-valeur du dictionnaire
            
        Raises:
            StopIteration: Quand il n'y a plus d'éléments à parcourir
        """
        if self.num < len(self.dict_book):
            print({list(self.display_info().keys())[self.num]:list(self.display_info().values())[self.num]})
            self.num += 1
        else:
            raise StopIteration

class Album(Media):
    """
    Classe représentant un album musical dans la bibliothèque.
    
    Hérite de la classe Media et ajoute des attributs spécifiques aux albums.
    
    Attributes:
        title (str): Titre de l'album
        release_year (str): Année de sortie
        author (str): Artiste/Groupe
        genre (str): Genre musical
        label (str): Label de l'album
        tracks (dict): Dictionnaire des pistes de l'album
        dict_album (dict): Dictionnaire stockant les informations de l'album
        num (int): Compteur pour l'itération
    """
    def __init__(self, _title, _release_year, _author, _genre, _label, _tracks):
        """
        Initialise un objet album avec tous ses attributs.
        
        Args:
            _title (str): Titre de l'album
            _release_year (str): Année de sortie
            _author (str): Artiste/Groupe
            _genre (str): Genre musical
            _label (str): Label de l'album
            _tracks (dict): Dictionnaire des pistes
        """
        Media.__init__(self, _title, _release_year, _author)
        self.genre = _genre
        self.label = _label
        self.tracks = _tracks
        self.dict_album = {"title":_title,"release year":_release_year, "author":_author}
        self.num = 0
        
    def dict_update(self, d):
        """
        Met à jour le dictionnaire de l'album avec de nouvelles données.
        
        Args:
            d (dict): Dictionnaire contenant les nouvelles données
        """
        self.dict_album.update(d)
        
    def tracks_to_dict(self):
        """
        Renvoie le dictionnaire des pistes de l'album.
        
        Returns:
            dict: Dictionnaire des pistes
        """
        return self.tracks
        
    def __len__(self):
        """
        Renvoie le nombre de pistes dans l'album.
        
        Returns:
            int: Nombre de pistes
        """
        return len(self.tracks)
        
    def display_info(self):
        """
        Renvoie toutes les informations de l'album sous forme de dictionnaire.
        
        Ajoute les attributs spécifiques au dictionnaire de base.
        
        Returns:
            dict: Dictionnaire avec toutes les informations de l'album
        """
        self.dict_update({"genre":self.genre, "label":self.label})
        self.dict_update({"tracks":self.tracks})
        return self.dict_album
        
    def __iter__(self):
        """
        Prépare l'itération sur les attributs de l'album.
        
        Returns:
            Album: Instance de l'objet album
        """
        return self
        
    def __next__(self):
        """
        Retourne le prochain élément lors de l'itération.
        
        Returns:
            dict: Paire clé-valeur du dictionnaire
            
        Raises:
            StopIteration: Quand il n'y a plus d'éléments à parcourir
        """
        if self.num < len(self.dict_album):
            print({list(self.display_info().keys())[self.num]:list(self.display_info().values())[self.num]})
            self.num += 1
        else:
            raise StopIteration

class Track(Album):
    """
    Classe représentant une piste individuelle d'un album.
    
    Hérite de la classe Album et ajoute des attributs spécifiques aux pistes.
    
    Attributes:
        track_number (int): Numéro de la piste dans l'album
    """
    def __init__(self, _title, _release_year, _author, _genre, _label, _tracks, _track_number):
        """
        Initialise un objet piste avec tous ses attributs.
        
        Args:
            _title (str): Titre de l'album parent
            _release_year (str): Année de sortie
            _author (str): Artiste/Groupe
            _genre (str): Genre musical
            _label (str): Label de l'album
            _tracks (dict): Dictionnaire des pistes
            _track_number (int): Numéro de la piste
        """
        Album.__init__(self, _title, _release_year, _author, _genre, _label, _tracks)
        self.track_number = _track_number
        
    def track_from_dict(self):
        """
        Extrait les informations d'une piste spécifique.
        
        Returns:
            dict: Dictionnaire avec les informations de la piste
        """
        return {list(self.tracks.values())[self.track_number-1]:list(self.tracks.keys())[self.track_number-1]}

class Movie(Media):
    """
    Classe représentant un film dans la bibliothèque.
    
    Hérite de la classe Media et ajoute des attributs spécifiques aux films.
    
    Attributes:
        title (str): Titre du film
        release_year (str): Année de sortie
        author (str): Réalisateur/Auteur
        publisher (str): Producteur
        genre (str): Genre du film
        time (str): Durée du film
        dict_movie (dict): Dictionnaire stockant les informations du film
    """
    def __init__(self, _title, _release_year, _author,  _publisher, _genre, _time):
        """
        Initialise un objet film avec tous ses attributs.
        
        Args:
            _title (str): Titre du film
            _release_year (str): Année de sortie
            _author (str): Réalisateur/Auteur
            _publisher (str): Producteur
            _genre (str): Genre du film
            _time (str): Durée du film
        """
        Media.__init__(self, _title, _release_year, _author)
        self.publisher = _publisher
        self.genre = _genre
        self.time = _time
        self.dict_movie = {"title":_title,"release year":_release_year, "author":_author}
        
    def dict_update(self, d):
        """
        Met à jour le dictionnaire du film avec de nouvelles données.
        
        Args:
            d (dict): Dictionnaire contenant les nouvelles données
        """
        self.dict_movie.update(d)
        
    def display_info(self):
        """
        Renvoie toutes les informations du film sous forme de dictionnaire.
        
        Ajoute les attributs spécifiques au dictionnaire de base.
        
        Returns:
            dict: Dictionnaire avec toutes les informations du film
        """
        self.dict_update({"publisher":self.publisher, "genre":self.genre, "time":self.time})
        return self.dict_movie

class Library:
    """
    Classe gérant une collection de médias avec persistance MongoDB.
    
    Fournit des méthodes pour ajouter, supprimer, rechercher et afficher des médias,
    ainsi que pour sauvegarder et charger la bibliothèque depuis MongoDB.
    
    Attributes:
        medias (list): Liste des objets média dans la bibliothèque
    """
    def __init__(self, *args):
        """
        Initialise une bibliothèque avec une liste optionnelle de médias.
        
        Args:
            *args: Liste variable d'objets média à ajouter à la bibliothèque
        """
        #super().__init__(*args)
        self.medias = list(args)
        
    def display_all(self):
        """
        Affiche les informations de tous les médias dans la bibliothèque.
        
        Returns:
            list: Liste des dictionnaires d'information pour tous les médias
        """
        return [media.display_info() for media in self.medias]
        
    def add_media(self, media):
        """
        Ajoute un média à la bibliothèque.
        
        Args:
            media (Media): Objet média à ajouter
        """
        self.medias.append(media)
        
    def remove_media(self, title):
        """
        Supprime un média de la bibliothèque par son titre.
        
        Args:
            title (str): Titre du média à supprimer
        """
        for media in self.medias:
            if title==media.display_info()['title']:
                self.medias.remove(media)
                
    def search(self, keyword):
        """
        Recherche un média par mot-clé.
        
        Pour les albums, recherche également dans les titres des pistes.
        
        Args:
            keyword (str): Mot-clé à rechercher
            
        Returns:
            tuple or str: Pour les albums avec piste correspondante, retourne
                          (titre_album, titre_piste). Pour les autres médias,
                          retourne le titre du média.
        """
        for media in self.medias:
            if media.__class__.__name__ == 'Album':
                for track in media.tracks_to_dict():
                    if keyword.lower() in track.lower():
                        return media.display_info()['title'], track
            else:
                if keyword.lower() in media.display_info()['title'].lower():
                    return media.display_info()['title']
                    
    def list_medias(self, order_by):
        """
        Liste les médias triés selon un critère spécifié.
        
        Args:
            order_by (str): Critère de tri ('title' ou 'release year')
            
        Returns:
            list: Liste des médias triée selon le critère spécifié
        """
        if order_by=='title':
            return sorted(self.display_all(), key=lambda x: x['title'])
        if order_by=='release year':
            return sorted(self.display_all(), key=lambda x: x['release year'])
            
    def mongo_connect(self):
        """
        Établit une connexion à la base de données MongoDB.
        
        Configure les attributs client, db et media pour l'interaction avec MongoDB.
        """
        self.client = MongoClient("localhost", 27017)
        self.db = self.client["projet_POO"]
        self.media = self.db["media"]
        
    def save_to_mongo(self):
        """
        Sauvegarde tous les médias de la bibliothèque dans MongoDB.
        
        Convertit chaque média en dictionnaire avant de l'insérer dans la collection.
        """
        self.mongo_connect()
        self.media.insert_many(self.display_all())
        
    def load_from_mongo(self):
        """
        Charge tous les médias depuis MongoDB.
        
        Returns:
            list: Liste des documents (dictionnaires) chargés depuis MongoDB
        """
        self.mongo_connect()
        self.lst_docs = []
        for doc in self.media.find({}):
            self.lst_docs.append(doc)
        return self.lst_docs
        
    def reload_library(self, _lst):
        """
        Reconstitue la bibliothèque à partir d'une liste de dictionnaires.
        
        Crée les objets appropriés (Book, Album, Movie) en fonction des attributs.
        
        Args:
            _lst (list): Liste de dictionnaires représentant des médias
            
        Returns:
            Library: Nouvelle instance de bibliothèque avec les médias reconstitués
        """
        self.lib = Library()
        for d in _lst:
            del d['_id']
            if 'number of pages' in list(d.keys()):
                book = Book(*list(d.values()))
                self.lib.add_media(book)
            if 'tracks' in list(d.keys()):
                album = Album(*list(d.values()))
                self.lib.add_media(album)
            if 'time' in list(d.keys()):
                movie = Movie(*list(d.values()))
                self.lib.add_media(movie)
        return self.lib

# Initialisation de la bibliothèque
library = Library()

# Boucle principale de l'interface utilisateur
response ='O'

while response=='O':
    print("\n", "Indiquer quelle action vous voulez faire", "\n")

    print('-' * 42)
    print('| {:^38} |'.format('Taper 1 pour ajouter un media'))
    print('-' * 42)
    print('| {:^38} |'.format('Taper 2 pour supprimer un media'))
    print('-' * 42)
    print('| {:^38} |'.format('Taper 3 pour rechercher un media'))
    print('-' * 42)
    print('| {:^38} |'.format('Taper 4 pour afficher tous les medias'))
    print('-' * 42, "\n")

    x = int(input("Votre choix d'action : "))

    if x!=4:

        print("\n", "Sélectionner le type de media","\n")

        print('-' * 24)
        print('| {:^21} |'.format('Taper 1 pour un livre'))
        print('-' * 24)
        print('| {:^21} |'.format('Taper 2 pour un album'))
        print('-' * 24)
        print('| {:^21} |'.format('Taper 3 pour un film'))
        print('-' * 24, "\n")

        y = int(input("Votre choix de media : "))

        if x==1:
            if y==1:
                title = input('Taper le titre du livre :')
                release_year = input("Taper l'année de publication :")
                author = input("Taper le nom de l'auteur :")
                publisher = input("Taper le nom de l'éditeur :")
                nb_of_pages = input("Taper le nombre de pages :")
                book = Book(title, release_year, author, publisher, nb_of_pages)
                library.add_media(book)
                print(book.display_info())
            elif y==2:
                title = input("Taper le titre de l'album :")
                release_year = input("Taper l'année de publication :")
                author = input("Taper le nom de l'artiste :")
                genre = input("Taper le genre musical :")
                label = input("Taper le label :")
                album = Album(title, release_year, author, genre, label)
                library.add_media(album)
                print(album.display_info())
            else:
                title = input("Taper le titre du film :")
                release_year = input("Taper l'année de publication du film :")
                author = input("Taper le nom de l'auteur du film :")
                publisher = input("Taper le nom du producteur du film :")
                genre = input("Taper le genre du film :")
                time = input("Taper la durée du film :")
                movie = Movie(title, release_year, author, publisher, genre, time)
                library.add_media(movie)
                print(movie.display_info())
            library.save_to_mongo()
        elif x==2:
            library_back_to_list_of_dicts = library.load_from_mongo()
            title = input('Taper le titre du media :')
            for d in library_back_to_list_of_dicts:
                if d['title']==title:
                    client = MongoClient("localhost", 27017)
                    db = client["projet_POO"]
                    media = db["media"]
                    media.delete_one({'title':title})
        else:
            library_back_to_list_of_dicts = library.load_from_mongo()
            library = library.reload_library(library_back_to_list_of_dicts)
            user_keyword = input("Entrer un mot clé :")
            print(library.search(user_keyword))
    else:
        library_back_to_list_of_dicts = library.load_from_mongo()
        library = library.reload_library(library_back_to_list_of_dicts)
        print(library.display_all())
  
    response = input("Voulez-vous effectuer une autre action (O/N) :")