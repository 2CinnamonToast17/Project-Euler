import random


class Zombie:
    pop = []

    def __init__(self, name):
        self.name = name
        Zombie.pop.append(name)


class Walker(Zombie):
    pop1 = []

    def __init__(self, name):
        super().__init__(name)
        print("A Walker has been resurrected".format(self.name))
        Walker.pop1.append(name)

    def how_many(cls):
        print("We have {:d} Walkers.".format(len(cls.pop1)))


class Runner(Zombie):
    pop2 = []

    def __init__(self, name):
        super().__init__(name)
        print("A Runner has been resurrected".format(self.name))
        Runner.pop2.append(name)

    def how_many(cls):
        print("We have {:d} Runners.".format(len(cls.pop2)))


class Crawler(Zombie):
    pop3 = []

    def __init__(self, name):
        super().__init__(name)
        print("A Crawler has been resurrected".format(self.name))
        Crawler.pop3.append(name)

    def how_many(cls):
        print("We have {:d} Crawlers.".format(len(cls.pop3)))


y = random.randint(3, 100000000)
for z in range(0, y):
    x = random.randint(1, 3)

    if x == 1:
        idk1 = Walker("")

    if x == 2:
        idk2 = Runner("")

    if x == 3:
        idk3 = Crawler("")


idk1.how_many()

idk2.how_many()

idk3.how_many()
