import datetime
import json
import os
from random import randrange
from abc import ABC, abstractmethod

from movie import Movie, ActionMovie, DramaMovie
from trailer import Trailer, ActionTrailer, DramaTrailer

# AbstractFactory
class MediaFactory(ABC):
    @classmethod
    def find_production_company(cls, genre):
        match genre:
            case "Action":
                return Tigersgate()
            case "Drama":
                return A25Films()
            case _:
                return None

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
        with open(os.path.join(os.path.curdir, "hollywood.json")) as hollywood:
            hollywood_talent = json.load(hollywood)
            title = hollywood_talent["Title"]["Action"]["Adjectives"][randrange(10)] + " " + hollywood_talent["Title"]["Action"]["Nouns"][randrange(10)]
            regisseur = hollywood_talent["Regisseurs"]["ActionRegisseurs"][randrange(10)]
            lead_actor = hollywood_talent["Actors"]["ActionActors"][randrange(10)]
        action_movie = ActionMovie(title, regisseur, lead_actor, [])
        action_movie.add_recorded_scene(self.record_explosion())
        action_movie.add_recorded_scene(self.record_villain_monologue_over_rising_music())
        action_movie.add_recorded_scene(self.record_car_crash())
        action_movie.add_recorded_scene(self.record_explosion())
        return action_movie


    def create_trailer(self, movie) -> Trailer:
        return ActionTrailer(movie, datetime.datetime(randrange(2024, 2030), randrange(1, 12), randrange(1, 28)), randrange(1, 9))

    @classmethod
    def hire_stuntman(cls):
        pass

    @classmethod
    def record_explosion(cls):
        return "explosion"

    @classmethod
    def record_car_crash(cls):
        return "car_crash"

    @classmethod
    def record_villain_monologue_over_rising_music(cls):
        return "villain_monologue_over_rising_music"

# ConcreteFactory2
class A25Films(MediaFactory):
    def create_movie(self) -> Movie:
        with open(os.path.join(os.path.curdir, "hollywood.json")) as hollywood:
            hollywood_talent = json.load(hollywood)
            title = hollywood_talent["Title"]["Drama"]["Adjectives"][randrange(10)] + " " + hollywood_talent["Title"]["Drama"]["Nouns"][randrange(10)]
            regisseur = hollywood_talent["Regisseurs"]["DramaRegisseurs"][randrange(10)]
            lead_actor = hollywood_talent["Actors"]["DramaActors"][randrange(10)]
        drama_movie = DramaMovie(title, regisseur, lead_actor, [])
        drama_movie.add_recorded_scene(self.record_dramatic_reading())
        drama_movie.add_recorded_scene(self.record_closeup())
        drama_movie.add_recorded_scene(self.record_shaky_cam_footage())
        drama_movie.add_recorded_scene(self.record_closeup())
        return drama_movie

    def create_trailer(self, movie) -> Trailer:
        return DramaTrailer(movie, datetime.datetime(randrange(2024, 2030), randrange(1, 12), randrange(1, 28)), randrange(1, 9))

    @classmethod
    def record_closeup(cls):
        return "closeup"

    @classmethod
    def record_dramatic_reading(cls):
        return "dramatic_reading"

    @classmethod
    def record_shaky_cam_footage(cls):
        return "shaky_cam_footage"