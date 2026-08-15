roll_number=[101,105,102,101,108,105,110]
unique_rolls = set(roll_number)
print(unique_rolls)
for i in unique_rolls:
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")
        
        
#ask user to enter employee ID and search it inside records
records=[(101,"alice",50000),(102,"bob",60000),(103,"janice",70000)]
employee_id=int(input("enter your employee id: "))
for employee in records:
 if employee_id==employee[0]:
    print("found")
    break
else:
    print("not found")
    