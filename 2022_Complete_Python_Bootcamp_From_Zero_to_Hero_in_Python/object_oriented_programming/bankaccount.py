
class bankaccount:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
          self.balance = self.balance + amount



    def withdraw(self,amount):
        if (self.balance > amount):
          self.balance = self.balance - amount
        else:
          print ("You dont have enough balance in your account")

mybankaccount =  bankaccount("sanjit",1000)
mybankaccount.deposit(100)
print (str(mybankaccount.balance))
mybankaccount.deposit(200)
print (str(mybankaccount.balance))
mybankaccount.deposit(300)
print (str(mybankaccount.balance))
mybankaccount.deposit(400)
print (str(mybankaccount.balance))
print ("============================")
mybankaccount.withdraw(600)
print (str(mybankaccount.balance))
mybankaccount.withdraw(1000)
print (str(mybankaccount.balance))
mybankaccount.withdraw(2000)
print (str(mybankaccount.balance))
