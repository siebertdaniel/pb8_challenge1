from abc import ABC, abstractmethod

class AbstractProductB(ABC):
    @abstractmethod
    def do_something(self) -> str:
        pass

class ConcreteProductB1(AbstractProductB):
    def do_something(self) -> str:
        return "ConcreteProductB1"

class ConcreteProductB2(AbstractProductB):
    def do_something(self) -> str:
        return "ConcreteProductB2"