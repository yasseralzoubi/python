from Animal import Animal

class Lion(Animal):

    def __init__(self, name, age, health, happiness,speed):
        super().__init__(name, age, health, happiness)
        self.speed = speed


Simba = Lion("Simba", 25, 60,50 , 60)
Simba.display_info()

    