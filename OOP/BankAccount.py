class BankAccount:
        def __init__(self, int_rate, balance):
            self.rate = int_rate			
            self.account_balance = balance

        def deposit(self, amount):
            self.account_balance += amount
        def withdraw(self, amount):
           self.account_balance -= amount
           if self.account_balance<=0:
               self.account_balance=5
               print("Insufficient funds: Charging a $5 fee")
        def display_account_info(self):
            print(" Balance:$",self.account_balance,)
        def yield_interest(self):
           self.deposit(self.account_balance*self.rate)
            
user1=BankAccount(0.3,150)
user2=BankAccount(20,200)
user1.deposit(20)
user1.deposit(10)
user1.deposit(5)
user1.withdraw(20)
user1.yield_interest()
user1.display_account_info()