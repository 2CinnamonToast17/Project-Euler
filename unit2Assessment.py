# farmhouse with a cow, sheep, chicken, goat, cat, dog, and chicken, and human


class animal:

    # sets up new "Animal" with these fields
    def __init__(self, name, sound, legs,):
        self.name = name
        self.sound = sound
        self.legs = legs


# inherits name, sound, legs from animal. Adds field: job
class workers(animal):
    def __init__(self, name, sound, legs, job):
        super().__init__(name, sound, legs)
        self.job = job


# inherits name, sound, legs from animal. Adds field: sleep
class recreation(animal):
    def __init__(self, name, sound, legs, sleep):
        super().__init__(name, sound, legs)
        self.sleep = sleep


#  sets all fields to different names
cow = workers("Izzy the Cow", "Moo", "I Have 4 Legs", "I produce milk and meat")
sheep = workers("Sean the Sheep", "Baa", " I have 4 legs", "I produce wool")
chicken = workers("Charlie the Chicken", "Cluck", "I have two legs", "I produce eggs and meat")
goat = workers("Billy the Goat", "Meeeh", "I have 4 legs", "I produce milk and meat")
cat = recreation("Cowie the Cat", "Meow", "I have 4 legs", "I sleep wherever I want")
dog = recreation("Duke The Dog", "Ruff", " I have 4 legs", " I sleep in the doghouse")
human = workers("Frank the Farmer", "Yeehaw", "I walk on two legs", "I run this farm")
