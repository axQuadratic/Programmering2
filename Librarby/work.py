import datetime as dt
import random as r

class Work:
    def __init__(self, title : str, year : int, production : bool, location : str, present : bool):
        self.title = title
        self.creation_year = year
        self.in_production = production
        self.location = location
        self.in_library = present

    def get_age(self):
        return int(dt.datetime.year) - self.creation_year
    
    def borrow(self):
        if self.in_library:
            self.in_library = False
            return 0
        return 1
    
    def restore(self):
        if not self.in_library:
            self.in_library = True
            return 0
        return 1
    
class Literature(Work):
    def __init__(self, title : str, year: int, production : bool, location : str, present : bool, publisher : str):
        super().__init__(title, year, production, location, present)
        self.publisher = publisher

class Book(Literature):
    def __init__(self, title : str, year : int, production : bool, location : str, present : bool, publisher : str, author : str, edition : int):
        super().__init__(title, year, production, location, present, publisher)
        self.author = author
        self.edition = edition

    def read(self):
        r.seed(''.join(map(bin, bytearray(str(self.__dict__), "utf8"))))
        if r.randint(0, 1):
            print("That was an amazing read!")
        else:
            print("That was a horrible read!")

class Fiction(Book):
    def __init__(self, title : str, year : int, production : bool, location : str, present : bool, publisher : str, author : str, edition : int, genre : str):
        super().__init__(title, year, production, location, present, publisher, author, edition)
        self.genre = genre

class Nonfiction(Book):
    def __init__(self, title : str, year : int, production : bool, location : str, present : bool, publisher : str, author : str, edition : int, subject : str):
        super().__init__(title, year, production, location, present, publisher, author, edition)
        self.subject = subject

class Audiobook(Literature):
    def __init__(self, title : str, year : int, production : bool, location : str, present : bool, publisher : str, source : Book, reader : str):
        super().__init__(title, year, production, location, present, publisher)
        self.source = source
        self.reader = reader

class Magazine(Literature):
    def __init__(self, title : str, year : int, production : bool, location : str, present : bool, publisher : str, issue : int):
        super().__init__(title, year, production, location, present, publisher)
        self.issue = issue

class Visual(Work):
    def __init__(self, title: str, year: int, production: bool, location: str, present: bool, subject : str, style : str):
        super().__init__(title, year, production, location, present)
        self.subject = subject
        self.style = style

class Movie(Visual):
    def __init__(self, title: str, year: int, production: bool, location: str, present: bool, subject: str, style: str, director : str):
        super().__init__(title, year, production, location, present, subject, style)
        self.director = director

class Anime(Visual):
    def __init__(self, title: str, year: int, production: bool, location: str, present: bool, subject: str, style: str, studio : str):
        super().__init__(title, year, production, location, present, subject, style)
        self.studio = studio

class Hentai(Anime):
    def __init__(self, title: str, year: int, production: bool, location: str, present: bool, subject: str, style: str, studio: str, has_tentacles : bool):
        super().__init__(title, year, production, location, present, subject, style, studio)
        self.lead_actor_age = 11
        self.has_tentacles = has_tentacles
        