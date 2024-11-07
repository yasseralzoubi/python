from Animal import Animal

class Lion(Animal):
    def __init__(self, animal_name, age, health_level, happiness_level,speed):
        super().__init__(animal_name, age, health_level, happiness_level)
        self.speed=speed

    def display_info(self):
        #super().display_info()
        print("speed:" + str(self.speed))


SimbaChild = Lion("Sibmba Child" , 25 , 60 , 60 , 50)
SimbaChild.display_info()