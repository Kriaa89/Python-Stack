from ninja import Ninja
from pet import Pet

my_pet = Pet("Buddy", "Dog", ["sit", "roll", "over"])
ninja = Ninja ("Abdallah" , "kriaa", ["bone", "grandor"], "food", my_pet)

ninja.walk()
ninja.feed()
ninja.bathe()