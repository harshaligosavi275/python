from bank_Account import *
kiran = BankAccount(1000,"kiran")
tom = BankAccount(2000,"tom")

kiran.getBalance()
tom.getBalance()

kiran.deposit(3000)
tom.deposit(1000)

kiran.withDraw(30000)
kiran.transfer(100,tom)


jim = InterestRewardAcct(1000,"jim")
jim.getBalance()
jim.deposit(100)
jim.transfer(200,kiran)

tina = SavingAccount(1000,"tina")
tina.getBalance()
tina.deposit(100)
tina.transfer(1000,tom)
