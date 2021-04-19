from src.Customers import Customers


class LogIn:

    def __init__(self):
        self.Config = None

    def getPassword(self,phoneNumber):
        customers = Customers()
        customerData = customers.loadCustomers()
        password = ""
        counter = 0
        while password == "" and counter < len(customerData):
            if phoneNumber == customerData[counter][0]:
                password = customerData[counter][3]
            counter += 1
        return password

    def logOn(self):
        phoneNumber = input("Enter your mobile number ")
        password = self.getPassword(phoneNumber)
        if password == "":
            print("You are not a user")
        else:
            if input("Enter password ") == password:
                print("Welcome - You are logged in")
            else:
                print("Incorrect Password - the account has been locked")

    def display(self):
        return self.logOn()

    def getCustomers(self):
        return self.getCustomers()

