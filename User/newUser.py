class User:
    def __init__(self, first_name,last_name,email,phone_number,balance=0):
        self.balance=balance
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone_number=phone_number

    def make_withdrawal(self,amount):
        self.balance-=amount
        return self.balance
    
    def display_user_balance(self):
        print(self.balance)

    def make_deposit(self,amount):
        self.balance+=amount
        return self .balance
    


user1= User("mohammad","smaer","das@dad","0597045",150)

user1.make_deposit(200)
user1.make_deposit(300)
user1.make_deposit(500)
user1.make_withdrawal(700)
user1.display_user_balance()

user2= User("yasser","alzoubi","@hotma","0555655",2000)

user2.make_deposit(4000)
user2.make_deposit(7000)
user2.make_withdrawal(1000)
user2.make_withdrawal(1000)
user2.display_user_balance()


user3=User("ahmad","khaled","@hotmail",3000)

user3.make_deposit(15000)
user3.make_withdrawal(1000)
user3.make_withdrawal(2000)
user3.make_withdrawal(6000)
user3.display_user_balance()