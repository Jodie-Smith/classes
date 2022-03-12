from oop import Account

lisa_account = Account(1000)
lisa_account.deposit(200)
print("Lisa's balance is", lisa_account.getbalance())

bart_account = Account(50)
print("Bart's balance is", bart_account.getbalance())

lisa_account.withdraw(75)
bart_account.deposit(75)

print("Lisa's balance is", lisa_account.getbalance())
print("Bart's balance is", bart_account.getbalance())


# special methods

print(lisa_account)
print(bart_account)

# prints <oop.Account object at 0x10081ffd0> & <oop.Account object at 0x10081fd00>
# this is because, every parameter we pass turns it into a string. so what you need to do is create a new function __str__ in the class file

# now that __str__ has been added it prints out balance plus added message. comment out the __str__ function to see difference

total_balance = lisa_account.getbalance() + bart_account.getbalance()
print(total_balance)

total_balance2 = lisa_account + bart_account
print(total_balance2)