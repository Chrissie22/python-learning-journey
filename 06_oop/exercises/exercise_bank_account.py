class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"deposit of {amount} was successful")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} was successful.")
        else:
            print(f"insufficient funds! Cannot withdraw {amount}.")
    def check_balance(self):
        print(f"Account Owner: {self.owner_name}")
        print(f"Current Balance: {self.balance}")
        
Account1 = BankAccount("Christabel", 100)

Account1.check_balance()
Account1.deposit(50)
Account1.withdraw(30)
Account1.withdraw(500)
Account1.check_balance()
          
            
        
        
        