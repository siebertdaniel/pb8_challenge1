from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    @abstractmethod
    def do_something(self) -> str:
        pass

class ConcreteProductA1(AbstractProductA):
    def do_something(self) -> str:
        return "ConcreteProductA1"

class ConcreteProductA2(AbstractProductA):
    def do_something(self) -> str:
        return "ConcreteProductA2"