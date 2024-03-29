class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            names = ", ".join(self.mammals)
        elif species == "fish":
            names = ", ".join(self.fishes)
        elif species == "bird":
            names = ", ".join(self.birds)

        return f"{species} in {self.name}: {names}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
n = int(input())

zoo = Zoo(zoo_name)

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

species_to_print = input()
print(zoo.get_info(species_to_print))