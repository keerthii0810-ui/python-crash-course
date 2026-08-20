import random

print(random.random())#0 to 1

import random
print(random.randint(1,5))

import random
name=input("enter your name:")
password=input("enter your password:")
skincare_brand=["dot&key","kyliecosmetics","rhode","rarebeauty","cetaphil"]
skincare_products=["sunscreen","perfume","lipbalm","lipstick","facewash"]
price_products=[700,2200,600,1200,650]
my_choice=input("enter your required brand:")
if my_choice not in skincare_brand:
    print("the product is not available")
    exit()
else:
    index=skincare_brand.index(my_choice)
    print("skincare_product:",skincare_products[index])
    price=price_products[index]   
    print("the product is available")
customer_requirement=int(input("enter your requirement:"))
stocks_available=random.randint(1,200)
print("currently available",stocks_available)
if customer_requirement>=stocks_available:
        print("stock is not available")
else:
        print("congratulations!.the stock is available")
        print("hello",name,"your requirement of products are available")
        print("The amount to be paid for the requirement:",price)        