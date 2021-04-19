from src.LogIn import LogIn
from src.AddCustomer import AddCustomer


class Main:
    def main():
        logOn = LogIn()
        logOn.logOn()
        addCustomer = AddCustomer()
        addCustomer.AddCustomer()


if __name__ == '__main__':
    Main.main()
