import random
name=input("Enter your name: ")
password=input("Enter your password: ")
skincare_brand=["dot&key","kyliecosmetics","rhode","rarebeauty","cetaphil"]
print("Available brands: ")
for brand in skincare_brand:
 print(brand)
skincare_products=["sunscreen","perfume","lipbalm","lipstick","facewash"]
print("Available products: ")
for product in skincare_products:
 print(product)
price_products=[700,2200,600,1200,650]
my_choice1=input("Enter your required brand: ")
my_choice2=input("Enter your required product: ")
if my_choice2 in skincare_products:
    index=skincare_products.index(my_choice2)
    print("skincare_product:",skincare_products[index])
if my_choice1 not in skincare_brand:
    print("the product is not available")
    exit()
else:  
    print("the product is available")
customer_requirement=int(input("Enter your requirement: "))
index=skincare_brand.index(my_choice1)
price=price_products[index]*customer_requirement
stocks_available=random.randint(1,200)
print("Currently available: ",stocks_available)
if customer_requirement>=stocks_available:
        print("stock is not available")
else:
        print("Congratulations!...the stock is available")
        print("Hello",name,"your requirement of products are available.")
        print("The amount to be paid for the requirement:",price)        