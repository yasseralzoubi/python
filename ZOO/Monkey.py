from Animal import Animal

class Monkey (Animal):
    def __init__(self, animal_name, age, health_level, happiness_level,jump_length):
        super().__init__(animal_name, age, health_level, happiness_level)
        self.jump_length=jump_length

    def display_info(self):
        #super().display_info()
        print("jump length:" + str(self.jump_length))