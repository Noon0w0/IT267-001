#this fille is inside bank packge
#call module
#from customer import Customer
#from account import Account

from bank.customer import Customer
from bank.account import Account


cus1 = customer.Customer()
cus1_acc = account.Account()

cus1 = Customer()
cus1.new_customer()

cus1_acc = Account()
cus1_acc.open_account(cus1.name,"Saving",'12-234-456',500)

print("**** Open Bank Account Detail ****")
print(cus1.cus_info())
print(cus1_acc.display_balance())
#print(cus1.cus_info())