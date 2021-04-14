from src.Customers import Customers


class LogIn:
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

    def logIn(self):
        phoneNumber = input("Enter your mobile number ")
        password = self.getPassword(phoneNumber)
        if password == "":
            print("You are not a user")
        else:
            if input("Enter password ") == password:
                print("Welcome", phoneNumber, "- You are logged in")
            else:
                print("Incorrect Password - the account has been locked")
