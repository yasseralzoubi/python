
class Animal:

    def __init__(self , name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        

    def display_info(self):
        print("My animal is: " + str(self.name) , "and age is :" + str(self.age) , "and his health is " + str(self.health), "and his happiness is  " + str(self.happiness) )

    def feed(self):
        self.health +=10
        self.happiness +=10

Tiger=Animal("Ali", 25,60,60)
Tiger.display_info()
Tiger.feed()
Tiger.display_info()