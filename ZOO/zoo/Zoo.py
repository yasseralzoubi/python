from Lion import Lion
from Bear import Bear

class Zoo:

    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name, age , health, happ, speed):
        self.animals.append( Lion(name,  age, health, happ, speed) )

    def add_tiger(self, name, age , health, happ, fur):
        self.animals.append( Bear(name, age , health, happ, fur) )

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala" , 25, 60, 60, 70)
zoo1.add_lion("Simba", 20, 80, 90 , 100)
zoo1.add_tiger("Rajah",30,50,50, "Thin")
zoo1.add_tiger("Shere Khan", 10, 80,80,"Thick")


zoo1.print_all_info()

