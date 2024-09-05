import datetime
from abc import ABC, abstractmethod

from movie import Movie, ActionMovie, DramaMovie
from trailer import Trailer, ActionTrailer, DramaTrailer

# AbstractFactory
class MediaFactory(ABC):
    @classmethod
    def find_production_company(cls, genre):
        if genre == "Action":
            return Tigersgate()
        elif genre == "Drama":
            return A25Films()
        else:
            return ""

    @abstractmethod
    def create_movie(self) -> Movie:
        pass

    @abstractmethod
    def create_trailer(self, movie) -> Trailer:
        pass

# ConcreteFactory1
class Tigersgate(MediaFactory):
    def create_movie(self) -> Movie:
        self.hire_stuntman()
        self.record_explosion()
        self.record_car_crash()
        return ActionMovie("Thunder Shark 3", "Michael Bay", "Bruce Willis", 126)


    def create_trailer(self, movie) -> Trailer:
        movie = self.create_movie()
        self.record_villain_monologue_over_rising_music()
        return ActionTrailer(movie, datetime.datetime(2025, 4, 20, ), 4)

    @classmethod
    def hire_stuntman(cls):
        pass

    @classmethod
    def record_explosion(cls):
        pass

    @classmethod
    def record_car_crash(cls):
        pass

    @classmethod
    def record_villain_monologue_over_rising_music(cls):
        pass

# ConcreteFactory2
class A25Films(MediaFactory):
    def create_movie(self) -> Movie:
        self.record_closeup()
        self.record_shaky_cam_footage()
        return DramaMovie("Tragic Clown Diary", "Christopher Nolan", "Leonardo DiCaprio", 182)

    def create_trailer(self, movie) -> Trailer:
        self.record_dramatic_reading()
        return DramaTrailer(self.create_movie(), datetime.datetime(2024, 10, 14), 7)

    def record_closeup(self):
        pass

    def record_dramatic_reading(self):
        pass

    def record_shaky_cam_footage(self):
        pass