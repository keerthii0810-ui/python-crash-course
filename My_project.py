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
    brand_index=skincare_brand.index(my_choice1)
    if index==brand_index:
     print("skincare_product:",skincare_products[index])
     print("the product is availabe")
    else:
     print("the product is not available")
     exit()
else:
    print("invalid choice")
    exit()
if my_choice1  in skincare_brand:
    index=skincare_brand.index(my_choice1)
    print("the brand is available")
else:  
    print("the brand is not available")
    exit()
customer_requirement=int(input("Enter your requirement: "))
index=skincare_brand.index(my_choice1)
price=price_products[index]*customer_requirement
stocks_available=random.randint(1,500)
print("Currently available stock : ",stocks_available)
if customer_requirement>stocks_available:
        print("stock is not  available")
        exit()
else:
        print("Congratulations!...the stock is available")
        print("Hello",name,"your requirement of products are available.")
        print("The amount to be paid for the requirement:",price)        
after_purchase=stocks_available-customer_requirement
if after_purchase==0:
    print("Out of stock")
    exit()
else:
    print("The stock after purchase:",after_purchase)

