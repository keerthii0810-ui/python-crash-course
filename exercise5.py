def even_number(number):
    evn_number=number%2==0
    return(evn_number)
print(even_number(2))

#waf to count the vowels in a string
def vowels(string):
    count=0
    for ch in string:
        if ch in "aeiouAEIOU":
         count +=1
    return(count)
print(vowels("keerthana")) 


#waf to find average where list of marks is passed as parameter
def average(list_of_marks):
   average_marks= sum(list_of_marks)/len(list_of_marks)
   return(average_marks)
print(average([10,20,30]))
