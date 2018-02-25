class Kettle(object):

    power_source = "Electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have
the same characteristics
Object: an instance of class
Instantiate: Create an instance of a class
Method: a function defined in a class
Attribute: a variable bound to an instance of a class
__init__ method act as constructor"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)


print("*" * 80)
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)  # Error because hamilton instance has no attribute power. This is the dynamic nature of PYTHON

print("Switching to atomic")
Kettle.power_source = "Atomic"
print(Kettle.power_source)

print("Switching kenwood power_source to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
