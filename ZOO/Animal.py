from Zoo import Zoo

class Animal(Zoo):
    def __init__(self,animal_name,age,health_level,happiness_level):
        self.name=animal_name
        self.age=age
        self.health=health_level
        self.happiness=happiness_level


    def display_info(self):
        print("Animal name:" + str(self.name),"/Animal age:" + str(self.age),"/Health level:" + str(self.health),"/Happiness level:" + str(self.happiness))

    def health_happiness(self):
        self.health +=10
        self.happiness+=10


Animals1=Animal("tiger",25,50,50)
Animals1.display_info()
Animals1.health_happiness()
Animals1.display_info()
    
        