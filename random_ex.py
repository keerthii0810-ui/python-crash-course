import random

print(random.random())#0 to 1

import random
print(random.randint(1,5))

import random
name=input("enter your name:")
password=input("enter your password:")
customer_requirement=int(input("enter your requirement:"))
stocks_available=random.randint(1,200)
price=random.randint(1,20000)
print("currently available",stocks_available)
if customer_requirement>=stocks_available:
        print("stock is not available")
else:
        print("stock is available")
        print("hello",name,"your requirement of products are available")
print("The amount to be paid for the requirement:",price)        