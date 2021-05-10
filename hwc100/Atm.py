class ATM():
    def __init__(self,cardNo,pin):
        self.cardNo=cardNo
        self.pin=pin
    
    def checkBalance(self):
        print("your balance is: ",10000)
    
    def withdraw(self,amount):
        newAmount=10000-amount
        
        if newAmount<0:
            print("You can't withdraw due to low balance!!")
        else:
            print("You have withdrawn: ",str(amount))
            print("Your new balance is: ",str(newAmount))
          
def main():
    card=input("Enter your card no: ")
    pin=input("Enter your pin: ")

    newUser=ATM(card, pin)
    print("Choose activity:\n1.Withdrawl\n2.Balance Enquiry")
    activity=int(input("Enter Activity Number: "))
    if activity==1:
        amount=int(input("Enter the amount you want to withdraw: "))
        newUser.withdraw(amount)
    elif activity==2:
        newUser.checkBalance()
    else:
        print("Enter a valid Activity Number: ")

if __name__=="__main__":
    main()