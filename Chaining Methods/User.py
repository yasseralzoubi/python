class User:
    def __init__(self, first_name,last_name,email,phone_number,balance=0):
        self.balance=balance
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone_number=phone_number

    def make_withdrawal(self,amount):
        if self.balance == 0 :
            print("insufficat balance")
        elif self.balance < amount :
            print("not enought balance")
        else:
            self.balance-=amount
            
        return self
    def display_user_balance(self):
        print(self.balance)

    def make_depsit(self,amount):
        self.balance+=amount
        return self  
    

user1= User("mohammad","smaer","das@dad","0597045",5000)

user1.make_withdrawal(500000).display_user_balance()

user2= user("yasser","alzoubi","@hotma","0555655",2000)


user3=user("ahmad","khaled","@hotmail",3000)