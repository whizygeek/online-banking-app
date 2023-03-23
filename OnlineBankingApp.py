import math

class BankingSystem(object):
    def init(self):
        print("Welcome to the online banking application!!")
        global name # username
        global pin # password - in banking system it is mainly pin
        global cb # current balance
        
    def signin(self):
        name = str(input("Please create your username"))
        pin = str(input("Please create your 6 digit pin"))
        if len(pin) == 6:
            pin = pin
        else:
            print("The pin must be in 6 digits")
            newpin = str(input("Please create your 6 digit pin"))
            if len(newpin) != 6:
                print("The pin must be in 6 digits")
                self.signin()
            else:
                pin = newpin
        print("Thank you for creating your bank account")

    def forgotpin(self):
        recoverpin = str(input("Please create your 6 digit pin"))
        if len(recoverpin) != 6:
            print("The pin must be in 6 digits")
            self.forgotpin()
        else:
            print("The new pin has been restored, please log in again!")
            pin = recoverpin

    def depositinterest(self,p,r,t):
        # A = P(e^(rt)) - formula to calculate the compound interest
        self.p = float(p)
        self.r = float(r)
        self.t = float(t)
        e = math.exp(self.r*self.t)
        # Calculation
        a = self.p*e # future value of your investement
        return a

if __name__ == "__main__":
    BankingSystem()
    