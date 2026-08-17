import random

print(random.random())#0 to 1

import random
print(random.randint(1,5))

import random
name=input("enter your name:")
password=input("enter your password:")
skincare_products=["dot&key","kyliecosmetics","rhode","rarebeauty","cetaphil"]
my_choice=input("enter your required product:")
if my_choice not in skincare_products:
    print("the product is not available")
    exit()
else:
    print("the product is available")
customer_requirement=int(input("enter your requirement:"))
stocks_available=random.randint(1,200)
price=random.randint(1,20000)
print("currently available",stocks_available)
if customer_requirement>=stocks_available:
        print("stock is not available")
else:
        print("congratulations!.the stock is available")
        print("hello",name,"your requirement of products are available")
        print("The amount to be paid for the requirement:",price)        