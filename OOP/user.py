class User:
    def __init__(self, name, email_address,balance):
                self.name = name		
                self.email = email_address		
                self.account_balance = balance

    def make_deposit(self, amount):	
        self.account_balance += amount

    def display(self):
        print("User:",self.name," Balance:",self.account_balance,"$")

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def transfer_money(self,other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)

    


user1=User("majed","gmail.com",150)
user2=User("shady","gmail.com",200)
user3=User("ahmed","gmail.com",100)
""""
user1.make_deposit(10)
user1.make_deposit(20)
user1.make_deposit(30)
user1.make_withdrawal(20)
user1.display()
user2.make_deposit(20)
user2.make_deposit(30)
user2.make_withdrawal(20)
user2.make_withdrawal(20)
user2.display()
user3.make_deposit(30)
user3.make_withdrawal(20)
user3.make_withdrawal(20)
user3.make_withdrawal(20)
user3.display()"""
user1.transfer_money(user3,20)
user1.display()
user3.display()