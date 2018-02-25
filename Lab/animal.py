from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @abstractmethod
    def habit(self):
        pass

    def __str__(self):
        return "Name: {0._name}, Age: {0._age}".format(self)


class Lion(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._diet = ['deer', 'buffallo', 'zebras']

    def habit(self):
        print("Lion lives in den")

    def __str__(self):
        return super().__str__() + " Diet: {0._diet}".format(self)

    def add_diet(self, diet):
        self._diet.append(diet)


class Bird(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._diet = ['corn', 'millet']

    def habit(self):
        print("Bird lives in nest")

    def __str__(self):
        return super().__str__() + " Diet: {0._diet}".format(self)


class Giraffe(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._diet = ['grass', 'shrubs', 'leaves']

    def habit(self):
        print("Giraffe lives in forest")

    def __str__(self):
        return super().__str__() + " Diet: {0._diet}".format(self)


class Zebra(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._diet = ['shrubs', 'twigs', 'leaves']

    def habit(self):
        print("Zebra lives in forest")

    def __str__(self):
        return super().__str__() + " Diet: {0._diet}".format(self)


class Crocodile(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._diet = ['fish', 'frog', 'bird']

    def habit(self):
        print("Crocodile lives in land and water")

    def __str__(self):
        return super().__str__() + " Diet: {0._diet}".format(self)

if __name__ == "__main__":
    l = Lion("Lion", 8)
    b = Bird("Bird", 10)
    g = Giraffe("Giraffe", 5)
    z = Zebra("Zebra", 25)
    c = Crocodile("Crocodile", 50)

    # list of Animal
    animal_list = [l, b, g, z, c]
    for animal in animal_list:
        print(animal)
        animal.habit()
        print("*" * 25)

