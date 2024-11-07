from Animal import Animal

class Bear(Animal):
    def __init__(self, animal_name, age, health_level, happiness_level,fur_thickness):
        super().__init__(animal_name, age, health_level, happiness_level)
        self.fur_thickness=fur_thickness


#    def display_info(self):
#        print("Animal name:" + str(self.name),"/Animal age:" + str(self.age),"/Health level:" + str(self.health),"/Happiness level:" + str(self.happiness)," Fur thickness:" + str(self.fur_thickness))


Bears1=Bear("sdads","25", 60 , 60, "thin")
Bears1.display_info()