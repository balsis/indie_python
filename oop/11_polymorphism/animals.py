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

    def quack(self):
        print("I'm a fish, and I can't quack")

animals = [RoboticBird(), Duck(), Fish()]
for animal in animals:
    animal.swim()
    animal.quack()