class Atm():
    def __init__(self,balance,cardNumber,pinNumber):
        self.balance=balance
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber

    def withDrawCash(self):
        enter=int(input("Enter your pin"))
        if(enter==self.pinNumber):
            amount=int(input("Enter the amount you want to withdraw"))
            self.balance-=amount
            print(self.balance)
        else:
            print("THEFT DETECTED")
    def depositAmount(self):
        amount=int(input("Enter the amount you want to deposit"))
        amount2=int(input("Confirm the amount"))
        if(amount==amount2):
            self.balance+=amount
            print(self.balance)
        else:
            print("CONFIRM AMOUNT")

john = Atm(20000,12345678901817,1234)
john.withDrawCash()
john.depositAmount()
       

        