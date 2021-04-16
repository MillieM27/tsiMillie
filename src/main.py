from src.LogIn import LogIn
from src.AddContact import AddContact


class Main:
    def main():
        logIn = LogIn()
        logIn.logIn()
        addContact = AddContact()
        addContact.AddContact()


if __name__ == '__main__':
    Main.main()
