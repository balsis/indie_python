class Duck:
    def swim(self):
        print("I'm a duck, and I can swim.")

    def quack(self):
        print("I'm a duck, and I can quack.")


class RoboticBird:
    def swim(self):
        print("I'm a robotic bird, and I can swim.")

    def quack(self):
        print("I'm a robotic bird, and I can quack.")


class Fish:
    def swim(self):
        print("I'm a fish, and I can swim")


def make_swim(animal):
    animal.swim()


animals = [Duck(), Fish(), RoboticBird()]
for animal in animals:
    make_swim(animal)