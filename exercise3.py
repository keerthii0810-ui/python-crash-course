#odd numbers from 1 to 20
for i in range(1,21,2):
    print(i)
    
#table of 57
for i in range(1,11):
    print(57*i)
    
#all multiples of 3 from 1 to 50 skip 15
for i in range(1,51):
    if i%3==0:
        if i==15:
            continue
        print(i)  
        
#take integers a and b as input. find and print the first number divisible by both a and b in the range 1 to 100 that is divisible by both a and b. 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
for i in range(1,101):
    if i % a == 0 and i % b == 0:
        print("The first number divisible by both", a, "and", b, "is:", i)
        break
