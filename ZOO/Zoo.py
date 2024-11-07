from Lion import Lion
from Bear import Bear


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
# [   Lion(Nala),  Lion(Simba), Bear(Rajah), Bear(Shere)   ]
    def add_lion(self, lion):
        self.animals.append( lion )

    def add_bear(self, bear):
        self.animals.append( bear )


    def print_animals(self):
        print(self.animals)

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        #print(self.animals)
        #for animal in self.animals:
        #    animal.display_info()

