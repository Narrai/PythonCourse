import pickle


class SavingsAccount(object):
    Rate = 0.02

    def __init__(self, name, pin, balance=0.0):
        self._name = name
        self._pin = pin
        self._balance = balance

    def __str__(self):
        result = "Name: " + self._name + '\n'
        result += "Pin: " + self._pin + '\n'
        result += "Balance: " + self._balance
        return result

    def get_balance(self):
        return self._balance

    def get_name(self):
        return self._name

    def get_pin(self):
        return self._pin

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount < 0:
            return
        elif self._balance < amount:
            return "Insufficient balance"
        else:
            self._balance -= amount
            return None

    def compute_interest(self):
        interest = self._balance * SavingsAccount.Rate
        self.deposit(interest)
        return interest


class Bank(object):

    def __init__(self, filename=None):
        self._accounts = {}
        self.filename = filename

        if filename is not None:
            file_object = open(filename, 'rb')
            while True:
                try:
                    account = pickle.load(file_object)
                    self.add(account)
                except EOFError:
                    file_object.close()
                    break

    def add(self, account):
        self._accounts[account.get_pin()] = account

    def remove(self, pin):
        return self._accounts.pop(pin, None)

    def get(self, pin):
        return self._accounts.get(pin, None)

    def compute_interest(self):
        total = 0
        for account in self._accounts.values():
            total += account.compute_interest()
            return total

    def __str__(self):
        return '\n'.join(map(str, self._accounts.values()))

    def save(self, filename=None):
        if filename is not None:
            self.filename = filename
        elif self.filename is None:
            return None
        file_object = open(filename, 'wb')
        for account in self._accounts.values():
            pickle.dump(account, file_object)
        file_object.close()
