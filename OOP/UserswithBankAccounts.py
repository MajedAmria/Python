
class BankAccount:
        def __init__(self, int_rate, balance):
            self.rate = int_rate			
            self.account_balance = balance


class UserWithBank :
        def __init__(self, name, email_address,int_rate,balance):
                    self.name = name		
                    self.email = email_address	
                    self.account = BankAccount(int_rate, balance)
        def make_deposit(self, amount):	
            self.account.account_balance += amount

        def display(self):
            print("User:",self.name," Balance:",self.account.account_balance,"$")

        def make_withdrawal(self,amount):
            self.account.account_balance -= amount
user=UserWithBank("majed","gmail.com",0.5,150)
user.display()