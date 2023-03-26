# Challenge 5: handling a bank account:

class user:
    def __init__(self, title, balance, accountno):
        self.title = title
        self.balance = balance
        self.accountno = accountno
    def getbalance(self):
         return self.balance
    def deposite(self):
         amount = float(input('enter the amount to be deposited'))
         self.balance = self.balance + amount
         print('deposite is successful and the balance in the account is %f' % self.balance)
    def withdraw(self):
         amount = float(input('enter the amount to withdraw'))
         self.amount = amount
         if self.amount > self.balance:
              print('Insufficient Funds | Balance Available: Rs',self.balance)
         else:
              self.balance = self.balance - self.amount
              print('Account balance has been updated: Rs',self.balance)
    def enquiry(self):
         print('balance in the account is %f' % self.balance)

class SavingsAccount(user):
    def __init__(self, title, balance, accountno, interestRate):
          super().__init__(title, balance, accountno)
          self.interestRate = interestRate
    def interestAmount(self):
         return(self.interestRate*self.Balance)/100
name=input('Enter customer name: ')
balance=float(input('enter your amount'))
acc=int(input('enter your accountno'))
itr=float(input('interestRate'))
customer1=SavingsAccount(name,balance,acc,itr)
print(customer1.getbalance())
customer1.deposite()
print(customer1.getbalance())
customer1.withdraw()
print(customer1.getbalance())