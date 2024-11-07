from Animal import Animal

class Bear(Animal):
    def __init__(self, name, age, health, happiness,fur_thickness):
        super().__init__(name, age, health, happiness)
        self.fur_thickness=fur_thickness



Bears1=Bear("sdads",25, 60 , 60, "thin")
Bears1.display_info()