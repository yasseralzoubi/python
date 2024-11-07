from BankAccount import *

class User:
    def __init__(self, first_name,last_name,email,phone_number,balance=0,intrate=0.01):
        
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone_number=phone_number
        self.account=BankAccount(balance,intrate)

    def make_withdrawal(self,amount):
        self.account.balance-=amount
        return self
    
    def display_user_balance(self):
        print(self.account.balance)

    def make_deposit(self,amount):
        self.account.balance+=amount
        return self 
    

user1= User("mohammad","smaer","das@dad","0597045",150)
user1.make_deposit(200000).make_deposit(300).make_deposit(500).make_withdrawal(700).display_user_balance()


user2= User("yasser","alzoubi","@hotma","0555655",2000)

user2.make_deposit(4000).make_deposit(7000).make_withdrawal(1000).make_withdrawal(1000).display_user_balance()



user3=User("ahmad","khaled","@hotmail",3000)

user3.make_deposit(15000).make_withdrawal(1000).make_withdrawal(2000).make_withdrawal(6000).display_user_balance()



