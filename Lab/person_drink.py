import animal


class Student(object):
    def __init__(self, name, age, major):
        self._name = name
        self._age = age
        self._major = major

    def __str__(self):
        return "Name: {0._name}, Age: {0._age}, Major: {0._major}".format(self)


class Faculty(object):
    def __init__(self, name, age, rank):
        self._name = name
        self._age = age
        self._rank = rank

    def __str__(self):
        return "Name: {0._name}, Age: {0._age}, Rank: {0._rank}".format(self)


class Manager(object):
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    def __str__(self):
        return "Name: {0._name}, Age: {0._age}, Salary: ${0._salary}".format(self)


class Engineer(object):
    def __init__(self, name, age, field, salary):
        self._name = name
        self._age = age
        self._field = field
        self._salary = salary

    def __str__(self):
        return "Name: {0._name}, Age: {0._age}, Field: {0._field}, Salary: ${0._salary}".format(self)


class Food(object):
    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price

    def __str__(self):
        return "Name: {0._name}, Weight: {0._weight}, Total Price: ${0._price}".format(self)


class Drink(object):
    def __init__(self, name, bottles, price):
        self._name = name
        self._bottles = bottles
        self._price = bottles * price

    def __str__(self):
        return "Name: {0._name}, Number of bottles: {0._bottles}, Total price: ${0._price}".format(self)


class Desert(object):
    def __init__(self, name, boxes, price):
        self._name = name
        self._boxes = boxes
        self._price = boxes * price

    def __str__(self):
        return "Name: {0._name}, Number of boxes: {0._boxes}, Total price: ${0._price}".format(self)


class Game(object):
    def __init__(self, name, types):
        self._name = name
        self._types = types

    def __str__(self):
        return "Name: {0._name}, Type: {0._types}".format(self)


def trip_to_party(l_mixed):
    for item in l_mixed:
        print(item)
        print("=" * 45)


def animal_joins_party(l_list):
    for i in l_list:
        print(i)
        print("*" * 50)


if __name__ == "__main__":
    s = Student("Nar", 33, "Computer Science")
    f = Faculty("Dr. Subash", 42, "Doctorate")
    m = Manager("Mohan", 40, 80000)
    e = Engineer("Greg", 50, "Civil Engineering", 70000)
    fo = Food("Chawmin Combo", 2, 10)
    d = Drink("Pepsi", 2, 2)
    de = Desert("Pecan Pie", 3, 3.50)
    g = Game("Cricket", "outdoor")

    # heterogeneous list
    mixed_list = [s, f, m, e, fo, d, de, g]
    trip_to_party(mixed_list)

    # animal list
    l = animal.Lion("Lion", 5)
    b = animal.Bird("Bird", 10)
    g = animal.Giraffe("Giraffe", 8)
    z = animal.Zebra("Zebra", 12)
    c = animal.Crocodile("Crocodile", 20)
    animal_list = [l, b, g, z, c]

    print("\n\nPrinting two list together")
    # two list putting together
    two_list = mixed_list + animal_list
    animal_joins_party(two_list)



