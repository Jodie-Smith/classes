from oop import Account

#this is what inheritance is
#Saving_Account is a kind of Account
#Saving_Account is what we would call a derived class (subclass)
#Account is a base class (superclass)
class Saving_Account(Account):
    # pass #nothing inside it, just says pass (no operation placeholder), just to satisfy the fact that something must be indented inside the class

#overriding from oop

    def __init__(self, inital, interest_rate):
        super().__init__(inital)
        self._interest_rate = interest_rate

    def __str__(self):
        savings_info = self.__get_holder_name
        savings_info += "Savings "
        savings_info += super().__str__()
        return savings_info

    def calculate_interest(self):
        return self.getbalance() * self._interest_rate