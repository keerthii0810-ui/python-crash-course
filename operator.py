#arithmetic operators
print(10 + 5) # addition
print(10 - 5) # subtraction
print(10 * 5) # multiplication
print(10 / 5) # division
print(10 % 3) # modulus
print(10 ** 2) # exponentiation
print(10 // 3) # floor division


#assignment operators
a = 10
a+=10
print(a)
a-=6
print(a)
a*=2
print(a)
a/=4
print(a)
a%=3
print(a)
a**=2
print(a)
a//=2
print(a)

#operator precedence
a=2+4*2
print(a)
b=(2-4)*2
print(b)
c=(5*5)//2+3
print(c)

#comparison operators
a=10
b=20
print(a==b)
print(a<b)
print(a>b)
print(a!=b)
print(a<=b)
print(a>=b)

#logical operators
a=2<2
b=2>=5
print(a or b)#either a or b is true then it will return true
print(a and b)#both a and b should be true then it will return true
print(not a)#if a is true then it will return false and if a is false then it will return true
print(not b)#if b is true then it will return false and if b is false then it will return true

#conditional statements
total_marks=int(input("enter total marks:"))
if total_marks>=90:
    print("Grade: A")
elif total_marks>=80:
    print("Grade: B")
elif total_marks>=70:
    print("Grade: C")
else:
    print("Grade: D")
print("end of program")

