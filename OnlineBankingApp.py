import math

class BankingSystem(object):
    def init(self):
        print("Welcome to the online banking application!!")
        global name # username
        global pin # password - in banking system it is mainly pin
        global cb # current balance
        
    def signin(self):
        self.name = str(input("Please create your username"))
        self.pin = str(input("Please create your 6 digit pin"))
        if len(self.pin) == 6:
            self.pin = self.pin
        else:
            print("The pin must be in 6 digits")
            self.newpin = str(input("Please create your 6 digit pin"))
            if len(self.newpin) != 6:
                print("The pin must be in 6 digits")
                self.signin()
            else:
                self.pin = self.newpin
        print("Thank you for creating your bank account")

    def forgotpin(self):
        self.recoverpin = str(input("Please create your 6 digit pin"))
        if len(self.recoverpin) != 6:
            print("The pin must be in 6 digits")
            self.forgotpin()
        else:
            print("The new pin has been restored, please log in again!")
            self.pin = self.recoverpin
            self.login()

    def depositinterest(self,p,r,t):
        # A = P(e^(rt)) - formula to calculate the compound interest
        self.p = float(p)
        self.r = float(r)
        self.t = float(t)
        e = math.exp(self.r*self.t)
        # Calculation
        a = self.p*e # future value of your investement
        return a

    def login(self):
        # name1 represents username
        # pin1 represents user's password/pin
        self.name1 = str(input("Please enter your username"))
        self.pin1 = str(input("Please enter your password"))
        # check wheather username and password match or not
        if self.name1 == self.name and self.pin1 == self.pin:
            print(f"Welcome to the online banking application {self.name}")
            print("Please choose the menu down here")
            listmenu = ["1-Deposit", "2-Withdraw", "3-Transfer", "4-Check Balance", "5-Deposite Interest Rate", "6-Calculate Compound Interest"]
            for b in listmenu:
                print(b)
            self.choose = int(input("Please enter your choice: "))
            self.dpst = 0 # represents deposit
            self.widrw = 0 # represents withdraw
            self.chblnc = 0 # represents check balance
            if self.choose == 1:
                self.dpst = int(input("Enter the amount of your deposit"))
                self.chblnc = self.dpst
                print(f"Your current balance is {self.chblnc}")
            elif self.choose == 2:
                self.widrw = int(input("Enter the amount of your money that you want to withdraw"))
                if self.widrw > self.chblnc:
                    print("Your current balance is not sufficient for this transaction")
                    self.login()
                else:
                    self.chblnc = self.chblnc - self.widrw
                    print(f"{self.widrw} has been withdrawn from your account and your current balance is {self.chblnc}")       
            elif self.choose == 3:
                self.dest = str(input("Please enter the account number of your destination in 8 digits"))        
                if len(self.dest) == 8:
                    self.amnt = int(input("Please enter the amount of money you want to transfer"))
                    if self.amnt > self.chblnc:
                        print("Your current balance is not sufficient for this transaction")
                        self.login()
                    else:
                        self.chblnc = self.chblnc -self.amnt
                        print(f"The transaction of {self.amnt} has been transfered to {self.dest}. Your current balance is {self.chblnc}")
                else:
                    print("The transaction has been rejected as the destination account is invalid")
                    self.login()
            elif self.choose == 4:
                print(f"Your current balance is {self.chblnc}")
            elif self.choose == 5:
                if self.chblnc > 50000:
                    self.rate = 3
                elif self.chblnc > 30000:
                    self.rate = 2
                else:
                    self.rate = 1.5
                print(f"Your current deposite interest rate is {self.rate}%")
            elif self.choose == 6:
                listoption = ["1-Calculate your compound interest based on your current balance", "2-Calculate your compound interest based on your deposite."]
                for i in listoption:
                    print(i)
                self.choice = int(input("Please enter your choice from above options"))
                self.timing = str(input("How many years you want to invest your money"))
                if self.choice == 1:
                    if self.chblnc > 50000:
                        self.ratex = 3/100
                    elif self.chblnc > 30000:
                        self.ratex = 2/100
                    else:
                        self.ratex = 1.5/100
                    print(f"Your current balance in {self.timing}will be")
                    print(self.depositinterest(self.chblnc, self.ratex,self.timing))
                elif self.choice == 2:
                    self.money = int(input("Please enter the money you would like to deposite."))
                    if self.money > 50000:
                        self.ratex = 3/100
                    elif self.money > 30000:
                        self.ratex = 2/100
                    else:
                        self.ratex = 1.5/100
                    print(f"Your current balance in {self.timing}will be")
                    print(self.depositinterest(self.money, self.ratex,self.timing))
                else:
                    print("Option is not available! Back to main menu")
                    self.login()
        else:
            print("Either of your username or pin/password is wrong! Did you create your account?")
            list1 = ["1-Yes", "2-No"]
            for i in list1:
                print(i)
            self.inp = int(input("Please, enter your choice: "))
            if self.inp == 1:
                list2 = ["1-Do you want to attempt to login again?", "2-You forget your pin!"]
                for e in list2:
                    print(e)
                self.theanswer = int(input("Please, enter your choice: "))
                if self.theanswer == 1:
                    self.login()
                elif self.theanswer == 2:
                    self.forgotpin()
                else:
                    print("Option is not available")
                    self.login()
            elif self.inp == 2:
                print("Please create your account")
                self.signin()        
            else:
                print("Option is not available")
                self.login()
        self.exit()
                
    def mainmenu(self):
        self.listmenu = ["1-sign in","2-log in"]
        for i in self.listmenu:
            print(i)
        self.optionone = int(input("Please select an option"))
        if self.optionone == 1:
            self.signin()
        elif self.optionone == 2:
            self.login()
        else:
            print("Option is not available")                 
            self.mainmenu()
        self.exit()
            
    def exit(self):
        self.answer = str(input("Do you still want to conduct the transaction? Please type: Yes or No"))
        if self.answer == "Yes":
            self.login()
        elif self.answer == "No":
            print("Thank you for uwing this application!")
        else:
            print("Option is not available")
            self.mainmenu()
           
            
if __name__ == "__main__":
    BankingSystem().mainmenu()
    