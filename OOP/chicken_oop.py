class Chicken:
    total_eggs = 0

    def __init__(self, species, name):
        self.species = species
        self.name = name
        self. eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return f"{self.name} layed an egg"


c1 = Chicken(name="Alice", species="partridge Silkie")
c2 = Chicken(name="Amelia", species="speckled sussex")
print(Chicken.total_eggs)
c1.lay_egg()
print(Chicken.total_eggs)
c2.lay_egg()
c2.lay_egg()
print(Chicken.total_eggs)
