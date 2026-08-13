#understanding the list
from turtle import clear

price_amount=1000,2000,3000,4000,5000#assigning the price amount to a variable
print(price_amount[0]) #accessing the first element of the list
print(price_amount[-1]) #accessing the last element of the list
for i in price_amount: #iterating through the list
    print(i) #printing the elements of the list
    print("The price amount is:",i) #printing the elements of the list with a message
        
#storing a list of items in a variable.
brand="gucci","louis vuitton","prada","chanel","versace"#assigning the list of brands to a variable
price_amount=1000,2000,3000,4000,5000#assign the price amount to a variable
list=[brand,price_amount]#assigning the lists to a variable
for brand in list:
    print(brand)#printing the list of brands and price amounts
       
    #using different methods to access the elements of the list
    marks=[10,20,30,40,50]#assigning the list of marks to a variable
    print(marks.index(30))#accessing the index of the element 30 in the list
    print(marks.count(30))#counting the occurrences of the element 30 in the list
    print(marks.sort())#sorting the list in ascending order
    print(marks.reverse())#reversing the list
    print(marks.append(60))#adding an element to the end of the list
    print(marks.insert(2,25))#inserting an element at a specific index in the list
    print(marks.remove(40))#removing an element from the list
    print(marks.pop())#removing the last element from the list
    print(marks.clear())#removing all elements from the list
    print(marks.copy())#creating a copy of the list
    print(marks.extend([70,80,90]))#adding multiple elements to the end of the list
    print(len(marks))#finding the length of the list
    print(clear(marks))#removing all elements from the list
    print(type(marks))#finding the type of the list
    print(marks[0:2])#accessing a range of elements from the list
    print(marks[-2:])#accessing the last two elements of the list
    print(marks[::2])#accessing every second element of the list
    print(marks[::-1])#accessing the elements of the list in reverse order
    print(marks[:])
    
    