from bank import Bank


class ATM(object):

    SECRET_CODE = "CloseItDown"

    def __init__(self, bank1):
        self._account = None
        self._bank = bank1
        self._methods = {"1": self._get_balance, "2": self._deposit, "3": self._withdraw, "4": self._quit}

    def run(self):
        while True:
            name = input("Enter your name: ")
            if name == ATM.SECRET_CODE:
                break
            pin = input("Enter your pin: ")
            self._account = self._bank.get(pin)
            if self._account is None:
                print("Error, unrecognized PIN")
            elif self._account.get_name() != name:
                print("Error, unrecognized name")
                self._account = None
            else:
                self._process_account()

    def _process_account(self):
        while True:
            print("1 View you balance")
            print("2 Make a deposit")
            print("3 Make a withdrawal")
            print("4 Quit\n")
            number = input("Enter a number: ")
            the_method = self._methods.get(number, None)
            if the_method is None:
                print("Unrecognized number")
            else:
                the_method()
                if self._account is None:
                    break

    def _get_balance(self):
        print("Your balance is $", self._account.get_balance())

    def _deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self._account.deposit(amount)

    def _withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        message = self._account.withdraw(amount)
        if message:
            print(message)

    def _quit(self):
        self._bank.save()
        self._account = None
        print("Have a nice day!")

if __name__ == "__main__":
    bank = Bank("bank1.dat")
    atm = ATM(bank)
    atm.run()
