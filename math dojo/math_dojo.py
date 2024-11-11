class MathDojo:
    def __init__(self):
        self.result=0

    def add(self,num,*nums):
        self.result +=num
        return self


    def subtract(self,num,*nums):
        self.result -= num
        return self
    
math1= MathDojo()
math1.add(5).subtract(6).add(7)
print(math1.result)
        


        


