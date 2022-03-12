from saving_account import Saving_Account

wilma_saving = Saving_Account(100, 1.5)
wilma_saving.deposit(400)
wilma_saving.set_holder_name("Wilma")
print(wilma_saving.getbalance())
print(wilma_saving)
#fix later, test yourself

#how to override an attribute/behaviour (see savings account file)
# we will try to override this: from oop     def __str__(self):
#         return "Account has balance " + str(self.getbalance())