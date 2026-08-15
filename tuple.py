#tuple is immutable
marks=(10,20,30,40,50)#assigning the tuple of marks to a variable
print(marks,type(marks))#printing the tuple and its type
print(marks[0])#accessing the first element of the tuple
print(marks.index(30))#accessing the index of the element 30 in the tuple
print(marks.count(30))#counting the occurrences of the element 30 in the tuple
#marks[2]=100#this will raise an error because tuples are immutable
print(marks.append(60))#this will raise an error because tuples are immutable
#it can be written without parenthesis as well


