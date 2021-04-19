from src.Customers import Customers


class AddCustomer :

    def AddCustomer(self):
        print("\nYou can now add a new customer to customer book")

        while True:
            try:
                newCustomer = int(input("\nEnter the phone number of the customer to add: "))
                print("\nYou have successfully added: ", newCustomer, "to your customer book")
                break
            except ValueError:
                print("\n Please enter a number.")
                print()
