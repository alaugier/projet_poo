from abc import ABC, abstractmethod
import pymongo
from pymongo import MongoClient

class Media(ABC):
    def __init__(self, _title, _release_year, _author):
        self.title = _title
        self.release_year = _release_year
        self.author = _author
    
    @abstractmethod
    def display_info():
        pass

    def to_dict(self):
        return {"title":self.title, "release year":self.release_year, "author":self.author}

class Book(Media):
    def __init__(self, _title, _release_year, _author, _publisher, _nb_of_pages):
        Media.__init__(self, _title, _release_year, _author)
        self.publisher = _publisher
        self.nb_of_pages = _nb_of_pages
        self.dict_book = {"title":_title,"release year":_release_year, "author":_author}
        self.num = 0
    def dict_update(self, d):
        self.dict_book.update(d)
    def __len__(self):
        return len(self.dict_book)
    def display_info(self):
        self.dict_update({"publisher":self.publisher, "number of pages":self.nb_of_pages})
        return self.dict_book
    def __iter__(self):
        return self
    def __next__(self):
        if self.num < len(self.dict_book):
            print({list(self.display_info().keys())[self.num]:list(self.display_info().values())[self.num]})
            self.num += 1
        else:
            raise StopIteration

class Album(Media):
    def __init__(self, _title, _release_year, _author, _genre, _label, _tracks):
        Media.__init__(self, _title, _release_year, _author)
        self.genre = _genre
        self.label = _label
        self.tracks = _tracks
        self.dict_album = {"title":_title,"release year":_release_year, "author":_author}
        self.num = 0
    def dict_update(self, d):
        self.dict_album.update(d)
    def tracks_to_dict(self):
        return self.tracks
    def __len__(self):
        return len(self.tracks)
    def display_info(self):
        self.dict_update({"genre":self.genre, "label":self.label})
        self.dict_update({"tracks":self.tracks})
        return self.dict_album
    def __iter__(self):
        return self
    def __next__(self):
        if self.num < len(self.dict_album):
            print({list(self.display_info().keys())[self.num]:list(self.display_info().values())[self.num]})
            self.num += 1
        else:
            raise StopIteration

class Track(Album):
    def __init__(self, _title, _release_year, _author, _genre, _label, _tracks, _track_number):
        Album.__init__(self, _title, _release_year, _author, _genre, _label, _tracks)
        self.track_number = _track_number
    def track_from_dict(self):
        return {list(self.tracks.values())[self.track_number-1]:list(self.tracks.keys())[self.track_number-1]}

class Movie(Media):
    def __init__(self, _title, _release_year, _author,  _publisher, _genre, _time):
        Media.__init__(self, _title, _release_year, _author)
        self.publisher = _publisher
        self.genre = _genre
        self.time = _time
        self.dict_movie = {"title":_title,"release year":_release_year, "author":_author}
    def dict_update(self, d):
        self.dict_movie.update(d)
    def display_info(self):
        self.dict_update({"publisher":self.publisher, "genre":self.genre, "time":self.time})
        return self.dict_movie

class Library:
    def __init__(self, *args):
        #super().__init__(*args)
        self.medias = list(args)
    def display_all(self):
        return [media.display_info() for media in self.medias]
    def add_media(self, media):
        self.medias.append(media)
    def remove_media(self, title):
        for media in self.medias:
            if title==media.display_info()['title']:
                self.medias.remove(media)
    def search(self, keyword):
        for media in self.medias:
            if media.__class__.__name__ == 'Album':
                for track in media.tracks_to_dict():
                    if keyword.lower() in track.lower():
                        return media.display_info()['title'], track
            else:
                if keyword.lower() in media.display_info()['title'].lower():
                    return media.display_info()['title']
    def list_medias(self, order_by):
        if order_by=='title':
            return sorted(self.display_all(), key=lambda x: x['title'])
        if order_by=='release year':
            return sorted(self.display_all(), key=lambda x: x['release year'])
    def mongo_connect(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client["projet_POO"]
        self.media = self.db["media"]
    def save_to_mongo(self):
        self.mongo_connect()
        self.media.insert_many(self.display_all())
    def load_from_mongo(self):
        self.mongo_connect()
        self.lst_docs = []
        for doc in self.media.find({}):
            self.lst_docs.append(doc)
        return self.lst_docs
    def reload_library(self, _lst):
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

library = Library()

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




