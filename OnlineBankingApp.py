import math

def init(self):
    print("Welcome to the online banking application!!")
    global name # username
    global pin # password - in banking system it is mainly pin
    global cb # current balance
    
def signin():
    name = str(input("Please create your username"))
    pin = str(input("Please create your 6 digit pin"))
    if len(pin) == 6:
        pin = pin
    else:
        print("The pin must be in 6 digits")
        newpin = str(input("Please create your 6 digit pin"))
        if len(newpin) != 6:
            print("The pin must be in 6 digits")
            signin()
        else:
            pin = newpin
    print("Thank you for creating your bank account")


if __name__ == "__main__":
    signin()
    