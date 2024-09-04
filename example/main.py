from factory import AbstractFactory

print("Factory 1")
factory = AbstractFactory.find_factory("1")
print(factory.create_product_a().do_something())
print(factory.create_product_b().do_something())

print("Factory 2")
factory = AbstractFactory.find_factory("2")
print(factory.create_product_a().do_something())
print(factory.create_product_b().do_something())