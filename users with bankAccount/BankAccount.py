class BankAccount:
    def __init__(self, balance=0, int_rate = 0.01): 
        self.intrest_rate=int_rate
        self.balance=balance


#     def deposit(self, amount):
#         self.balance+=amount
#         return self
#     def withdraw(self, amount):
#         self.balance-=amount
#         return self
#     def display_account_info(self):
#         print (self.balance,self.intrest_rate)
#     def yield_interest(self):
#         if self.balance>0:
#             yields=self.balance*self.intrest_rate
#             print(f"intrest rate {yields}")
#         return self  



# Acount1= BankAccount(1000)
# Acount1.deposit(100).deposit(200).deposit(300).withdraw(500).yield_interest().display_account_info()
# Acount2= BankAccount(5000,0.02)
# Acount2.deposit(500).deposit(300).withdraw(400).withdraw(300).withdraw(600).withdraw(1000).yield_interest().display_account_info()