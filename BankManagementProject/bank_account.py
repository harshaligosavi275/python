#hold different types of bank accounts
class BankAccount:
    def __init__(self,initialAmount,acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f'\nAccount {self.name} created.\nBalance = ${self.balance:.2f}');
        
    def getBalance(self):
        print(f'Account {self.name} balance = ${self.balance:.2f}')
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'\nAfter deposit {amount}\nAccount {self.name} balance = ${self.balance:.2f}')
        
    
    def viableTransaction(self,amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(f'\nSorry account {self.name} only has a balance of ${self.balance:.2f}')
        
    def withDraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f'\n WithDraw complete.')
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw Interrupted: {error}')
            
    
     #  now transfer money from one account to another account.
    def transfer(self, amount,account):
        try:
            #  to get the emoji's (window key + .)
             print('\n**************Begining Transfer.. 🚀')
             self.viableTransaction(amount)
             self.withDraw(amount)
             account.deposit(amount)
             print('\nTransfer Complete! ✅****************')
        except BalanceException as error:
            print(f'\n Transfer Interrupted:❌ {error}') 
                 
# -----------------------------------------
class BalanceException(Exception):
    pass


# ---------------------------------------------------------

class InterestRewardAcct(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print(f'\nDeposit Complete')
        self.getBalance()
        
        
# --------------------------------------------------
class SavingAccount(InterestRewardAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
        
    def withDraw(self, amount):
        try:
            self.viableTransaction(amount +self.fee)
            self.balance = self.balance -(amount + self.fee)
            print('\nWithDraw completed.')
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw Interrupted: {error}')
