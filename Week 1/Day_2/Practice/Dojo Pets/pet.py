class Pet:
    def __init__(self, name, type, tricks, health=100, energy=100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy +=5
        self.energy += 10

    def play(self):
        self.health += 5
    def noise(self):
        print(f"{self.name} make a noise!")  # to test the function 