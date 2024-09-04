from abc import ABC, abstractmethod

# AbstractProductB
class Trailer(ABC):
    @abstractmethod
    def __init__(self, movie, release_date, length):
        self.movie = movie
        self.release_date = release_date
        self.length = length

    @abstractmethod
    def get_release_date(self) -> str:
        pass

    @abstractmethod
    def display(self) -> str:
        pass

# ConcreteProductB1
class ActionTrailer(Trailer):
    def __init__(self, movie, release_date, length):
        super().__init__(movie, release_date, length)

    def get_release_date(self) -> str:
        return self.release_date

    def display(self) -> str:
        return f"{self.movie.regisseur} plunges us into a world of adrenaline as {self.movie.lead_actor} races against time to save the world. With breathtaking stunts and unexpected twists, {self.movie.title} will get your heart racing. This spectacle will release in cinemas on {self.release_date.strftime('%d.%m.%Y')}"


# ConcreteProductB2
class DramaTrailer(Trailer):
    def __init__(self, movie, release_date, length):
        super().__init__(movie, release_date, length)

    def get_release_date(self) -> str:
        return self.release_date

    def display(self) -> str:
        return f"{self.movie.regisseur}'s {self.movie.title} explores the complexities of mortality through the live of {self.movie.lead_actor}'s character Sidney. A painful tale of death and forgiveness. Prepare to be moved by the raw emotions and unforgettable performances. See it in cinemas starting on {self.release_date.strftime('%d.%m.%Y')}"