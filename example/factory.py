from abc import ABC, abstractmethod

from product_a import AbstractProductA, ConcreteProductA1, ConcreteProductA2
from product_b import AbstractProductB, ConcreteProductB1, ConcreteProductB2

class AbstractFactory(ABC):
    @classmethod
    def find_factory(cls, concrete):
        match concrete:
            case "1":
                return ConcreteFactory1()
            case "2":
                return ConcreteFactory2()
            case _:
                return None

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()