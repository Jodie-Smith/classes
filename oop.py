class Account:
    numCreated = 0
    # will keep track of how many bank accounts have been created

    # everything that belongs inside of a class has to be indented
    # constructor. has to be called __init__ to be a construtor in python
    # self is explicit parameter that says the very first parameter that gets passed into it is that thing (e.g that persons account balance + the deposit)
    def __init__(self, initial):
        # things that start with a double underscore are private
        self.__balance = initial
        self.semiPrivate = "hello from account"
        Account.numCreated += 1
        self.__testItem = "yes"

    def deposit(self, amt):
        self.__balance += amt
        return

    def withdraw(self, amt):
        self.__balance -= amt
        return

    def getbalance(self):
        return self.__balance

    def get_holder_name(self):
        return self.__holder_name

    def set_holder_name(self, name):
        self.__holder_name = name
        return


    def __str__(self):
        return "Account has balance " + str(self.getbalance())
        # overriding happens when something that has been inhereted, we override it and make it better. This __str__ has overridden a method

    def __add__(self, other):
        return self.getbalance() + other.getbalance()


def main():
    homer = Account(350)
    print(homer.getbalance())


if __name__ == "__main__":
    main()

# will make it so that the homer print only shows up in this file. take out the def and conditional (and indent), and it will show up in the initatiob file also.

# main()