from abc import ABC, abstractmethod

# AbstractProductA
class Movie(ABC):
    @abstractmethod
    def __init__(self, title, regisseur, lead_actor, recorded_scenes):
        self.title = title
        self.regisseur = regisseur
        self.lead_actor = lead_actor
        self.recorded_scenes = recorded_scenes

    @abstractmethod
    def display(self) -> str:
        pass

    @property
    @abstractmethod
    def recorded_scenes(self):
        return self.recorded_scenes

    @recorded_scenes.setter
    def recorded_scenes(self, value):
        self._recorded_scenes = value

    @abstractmethod
    def add_recorded_scene(self, scene):
        self.recorded_scenes.append(scene)


# ConcreteProductA1
class ActionMovie(Movie):
    def __init__(self, title, regisseur, lead_actor, recorded_scene):
        super().__init__(title, regisseur, lead_actor, recorded_scene)
        self.genre = "Action"

    def display(self)-> str:
        return f"The weight of the world rests on the shoulders of {self.lead_actor} in {self.regisseur}'s high-octane action film {self.title}. A ticking clock and a relentless enemy force drive them on a perilous mission, filled with daring escapes, explosive confrontations, and breathtaking stunts. With time running out, {self.lead_actor} must overcome impossible odds to save humanity from impending doom."

    def recorded_scenes(self):
        return self.recorded_scenes

    def add_recorded_scene(self, scene):
        self.recorded_scenes.append(scene)

# ConcreteProductA2
class DramaMovie(Movie):

    def __init__(self, title, regisseur, lead_actor, recorded_scenes):
        super().__init__(title, regisseur, lead_actor, recorded_scenes)
        self.genre = "Drama"

    def display(self)-> str:
        return f"The young Sidney (portrayed by {self.lead_actor}) explores the complexities of mortality in {self.title} by {self.regisseur} . A person grappling with a terminal illness, as their life dwindles away in front of their eyes. They embarks on a painful journey of self-discovery, confronting past regrets and seeking forgiveness from those they wronged. The film delves deep into the raw emotions of facing death, the power of reconciliation, and the enduring strength of the human spirit. A masterpiece by {self.regisseur}."

    def recorded_scenes(self):
            return self.recorded_scenes

    def add_recorded_scene(self, scene):
        self.recorded_scenes.append(scene)