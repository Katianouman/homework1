class BankAccount:
    def __init__(self,account_number,account_holder):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=0.0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
        else:
            print("lsufficient funds")
    def get_balance(self):
        return self.balance
class SavingsAccount(BankAccount) :
    def __init__(self,account_number,account_holder,interest_rate):
        super().__init__(account_number,account_holder)
        self.interest_rate=interest_rate
    def apply_interest(self):
        interest_amount=self.balance*(self.interest_rate/100)
        self.balance+=interest_amount
    def print(self):
        print(f"Current balance: ${self.balance},interest rate:{self.interest_rate}%")
bank_account=BankAccount("123456789","katia")
bank_account.deposit(1000)
print(f"Balance after deposit:${bank_account.get_balance()}")
bank_account.withdraw(500)
print(f"Balance after withdrawal:${bank_account.get_balance()}")
savings_account=SavingsAccount("987654321","aya",2.5)
savings_account.deposit(2000)
savings_account.apply_interest()
savings_account.print()

