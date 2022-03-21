
class BankAccount:
        def __init__(self, int_rate, balance):
            self.rate = int_rate			
            self.account_balance = balance

        def make_deposit(self, amount):	
            self.account_balance += amount
            return self
        def display(self):
            print("Balance:",self.account_balance,"$","Rate: ",self.rate )

        def make_withdrawal(self,amount):
            self.account_balance -= amount
            return self

class UserWithBank :
        def __init__(self, name, email_address,int_rate,balance):
                    self.name = name		
                    self.email = email_address	
                    self.account = BankAccount(int_rate, balance)
       

user=UserWithBank("majed","gmail.com",0.5,150)
user.account.make_deposit(150).make_withdrawal(50).make_deposit(100).display()
