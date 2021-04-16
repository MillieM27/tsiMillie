from src.Customers import Customers

class AddContact :

    def AddContact(self):
        print("\nYou can now add a new customer to customer book")

        while True:
            try:
                customerNumber = int(input("\nEnter the phone number of the customer to add: "))
                print("\nYou have successfully added: ", customerNumber, "to your customer book")
                break
            except ValueError:
                print("\n Please enter a number.")
                print()
