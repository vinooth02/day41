class Dog:
    def make_sound(self):
        return "Bark!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

if __name__ == "__main__":
    animals=[Dog(), Cat(), Cow()]

    for animal in animals:
        print(animal.make_sound())
