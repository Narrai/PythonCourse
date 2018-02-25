class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work but I am flying")
        else:
            print("I think I'll just walk")


class Ducks(object):

    def __init__(self):
        self._wing = Wing(1.8)   # this is composition

    def walk(self):
        print("waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack, quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("waddle, waddle, I waddle too")

    def swim(self):
        print("Come on it, but it's a bit chilly this far south")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

"""Python is dynamically typed language, it doesn't care about type but attributes"""
if __name__ == '__main__':
    donald = Ducks()
    donald.fly()
    # test_duck(donald)
    #
    # percy = Penguin()
    # test_duck(percy)